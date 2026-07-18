"""
LM Studio client for communicating with local LLM models.
"""

from __future__ import annotations

import asyncio
import json
import time
from typing import Any, Dict, Optional

import aiohttp
from app.core.config import config
from app.core.logging import logger


class LMStudioError(Exception):
    """Base exception for LM Studio client errors."""
    pass


class LMStudioConnectionError(LMStudioError):
    """Raised when connection to LM Studio fails."""
    pass


class LMStudioTimeoutError(LMStudioError):
    """Raised when request to LM Studio times out."""
    pass


class LMStudioResponseError(LMStudioError):
    """Raised when LM Studio returns an invalid response."""
    pass


class LMStudioHealthResult:
    """Structured result for LM Studio health checks."""
    
    def __init__(self, is_healthy: bool, message: str = "", details: Optional[Dict[str, Any]] = None):
        self.is_healthy = is_healthy
        self.message = message
        self.details = details or {}
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary for easy serialization."""
        return {
            "is_healthy": self.is_healthy,
            "message": self.message,
            "details": self.details
        }


class LMStudioClient:
    """
    Lightweight client for communicating with LM Studio (local LLM server).
    """

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.base_url = config.get("lm_studio", {}).get("endpoint", "http://localhost:1234")
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        """Async context manager entry."""
        if not self.session:
            self.session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            await self.session.close()

    async def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text using LM Studio model.
        
        Args:
            prompt (str): The text prompt to send to the LLM
            **kwargs: Additional parameters for the generation request
            
        Returns:
            str: Generated text from the LLM
			
        Raises:
            LMStudioConnectionError: If connection fails
            LMStudioTimeoutError: If request times out
            LMStudioResponseError: If response is invalid or empty
        """
        if not self.session:
            raise LMStudioError("Client session not initialized. Use async context manager.")
            
        # Prepare the request data
        request_data = {
            "prompt": prompt,
            **kwargs
        }
        
        try:
            start_time = time.time()
            logger.debug(f"Sending request to LM Studio at {self.base_url} with prompt: {prompt[:100]}...")
            
            async with self.session.post(
                f"{self.base_url}/v1/completions",
                json=request_data,
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            ) as response:
                
                if response.status == 408:
                    raise LMStudioTimeoutError("LM Studio request timed out")
                    
                if response.status >= 500:
                    raise LMStudioConnectionError(f"LM Studio server error: {response.status}")
                    
                if response.status != 200:
                    raise LMStudioResponseError(
                        f"LM Studio API returned status code {response.status}"
                    )
                
                try:
                    data = await response.json()
                except json.JSONDecodeError as exc:
                    raise LMStudioResponseError("Invalid JSON response from LM Studio") from exc
                
                # Extract the generated text from response
                if "choices" not in data or len(data["choices"]) == 0:
                    raise LMStudioResponseError(
                        "LM Studio API returned empty choices array"
                    )
                
                generated_text = data["choices"][0].get("text", "").strip()
                end_time = time.time()
                
                logger.debug(f"Successfully generated text in {end_time - start_time:.2f}s")
                return generated_text
                
        except aiohttp.ClientError as exc:
            raise LMStudioConnectionError(
                f"Failed to connect to LM Studio at {self.base_url}: {str(exc)}"
            ) from exc
        except asyncio.TimeoutError:
            raise LMStudioTimeoutError("LM Studio request timed out") from None
        except Exception as exc:
            logger.error(f"Unexpected error in LM Studio client: {exc}")
            raise LMStudioError(f"Unexpected error communicating with LM Studio: {str(exc)}") from exc

    async def health_check(self) -> LMStudioHealthResult:
        """
        Perform a health check on the LM Studio server.
        
        Verifies that the server is reachable, responds successfully,
        and has at least one model available if supported by API.
        
        Returns:
            LMStudioHealthResult: Structured result of the health check
        """
        try:
            # Test basic connectivity to endpoint first
            async with self.session.get(
                f"{self.base_url}/v1/models", 
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            ) as response:
                
                if response.status == 404:
                    # /v1/models might not exist, so try a basic health check endpoint
                    logger.debug("Models endpoint returned 404, trying basic health check")
                    async with self.session.get(
                        f"{self.base_url}/health", 
                        timeout=aiohttp.ClientTimeout(total=self.timeout)
                    ) as health_response:
                        
                        if health_response.status == 200:
                            return LMStudioHealthResult(
                                is_healthy=True,
                                message="LM Studio server reachable and responding",
                                details={
                                    "endpoint": self.base_url,
                                    "status_code": health_response.status,
                                    "model_check": "health_endpoint"
                                }
                            )
                        else:
                            logger.warning(f"Health check endpoint returned {health_response.status}")
                            return LMStudioHealthResult(
                                is_healthy=False, 
                                message=f"LM Studio server not responding properly at {self.base_url}",
                                details={
                                    "endpoint": self.base_url,
                                    "status_code": health_response.status,
                                    "model_check": "health_endpoint"
                                }
                            )
                elif response.status == 200:
                    # Server is reachable, now check models if available in the response
                    try:
                        models_data = await response.json()
                        model_count = len(models_data.get("data", [])) if isinstance(models_data, dict) else 0
                        
                        return LMStudioHealthResult(
                            is_healthy=True,
                            message="LM Studio server reachable with models available",
                            details={
                                "endpoint": self.base_url,
                                "status_code": response.status,
                                "model_count": model_count,
                                "model_check": "models_endpoint"
                            }
                        )
                    except (json.JSONDecodeError, Exception) as e:
                        # If we can't parse the models data but status is 200, it's still healthy
                        return LMStudioHealthResult(
                            is_healthy=True,
                            message="LM Studio server reachable",
                            details={
                                "endpoint": self.base_url,
                                "status_code": response.status,
                                "model_check": "models_endpoint"
                            }
                        )
                else:
                    # Some other status code, probably unhealthy
                    return LMStudioHealthResult(
                        is_healthy=False, 
                        message=f"LM Studio server returned unexpected status: {response.status}",
                        details={
                            "endpoint": self.base_url,
                            "status_code": response.status,
                            "model_check": "models_endpoint"
                        }
                    )
                
        except aiohttp.ClientError as exc:
            # Connection failed completely, most likely due to network or server being down
            logger.warning(f"Connection error during health check: {exc}")
            return LMStudioHealthResult(
                is_healthy=False,
                message=f"Failed to connect to LM Studio at {self.base_url}: {str(exc)}",
                details={
                    "endpoint": self.base_url,
                    "error_type": "connection_error"
                }
            )
        except asyncio.TimeoutError:
            # Request timed out, likely server not responding or network issue
            logger.warning(f"Timeout during health check to {self.base_url}")
            return LMStudioHealthResult(
                is_healthy=False,
                message=f"LM Studio request timed out at {self.base_url}",
                details={
                    "endpoint": self.base_url,
                    "error_type": "timeout"
                }
            )
        except Exception as exc:
            # Other unexpected error during health check
            logger.error(f"Unexpected error during LM Studio health check: {exc}")
            return LMStudioHealthResult(
                is_healthy=False,
                message=f"Error performing LM Studio health check: {str(exc)}",
                details={
                    "endpoint": self.base_url,
                    "error_type": "unexpected_error"
                }
            )
