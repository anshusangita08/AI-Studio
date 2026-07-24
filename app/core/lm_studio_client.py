"""
LM Studio client for communicating with local LLM models.
"""

from __future__ import annotations

import json
import time
import requests
from typing import Any, Dict, Optional

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

    def __init__(self, timeout: int | None = None):
        lm_config = config.get("lm_studio", {})

        self.base_url = lm_config.get(
            "endpoint",
            "http://localhost:1234"
        )

        self.timeout = (
            timeout
            if timeout is not None
            else lm_config.get("timeout", 30)
        )
        logger.info(
            f"LM Studio timeout: {self.timeout}s"
        )
        # No persistent session required

    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text using LM Studio model.

        Args:
            prompt (str): The text prompt to send to the LLM.
            **kwargs: Additional generation parameters.

        Returns:
            str: Generated text from the LLM.

        Raises:
            LMStudioConnectionError
            LMStudioTimeoutError
            LMStudioResponseError
        """

        request_data = {
            "model": config.get("lm_studio", {}).get("model"),
            "prompt": prompt,
            **kwargs,
        }

        # Remove None values
        request_data = {
            k: v for k, v in request_data.items()
            if v is not None
        }

        try:
            start_time = time.time()

            logger.debug(
                f"Sending LM Studio request ({len(prompt)} chars)"
            )

            logger.debug("LM Studio payload: %s", request_data)
            
            print("=" * 60)
            print(request_data)
            print("=" * 60)
            print(request_data["model"])
            print(len(prompt))
            print(prompt[:500])
            response = requests.post(
                f"{self.base_url}/v1/completions",
                json=request_data,
                timeout=self.timeout,
            )

            try:
                response.raise_for_status()
            except requests.HTTPError as exc:
                status = exc.response.status_code if exc.response is not None else None

                if status == 408:
                    raise LMStudioTimeoutError("LM Studio request timed out") from exc

                if status is not None and status >= 500:
                    raise LMStudioConnectionError(
                        f"LM Studio server error: {status}"
                    ) from exc

                # raise LMStudioResponseError(
                #     f"LM Studio API returned status code {status if status is not None else 'unknown'}"
                # ) from exc

                raise LMStudioResponseError(
                    f"LM Studio API returned {status}: {response.text}"
                )

            try:
                data = response.json()
            except json.JSONDecodeError as exc:
                raise LMStudioResponseError(
                    "Invalid JSON response from LM Studio"
                ) from exc

            choices = data.get("choices", [])

            if not choices:
                raise LMStudioResponseError(
                    "LM Studio API returned empty choices array"
                )

            choice = choices[0]

            generated_text = choice.get("text")

            if generated_text is None:
                generated_text = (
                    choice.get("message", {})
                        .get("content", "")
                )

            generated_text = generated_text.strip()

            if not generated_text:
                raise LMStudioResponseError(
                    "LM Studio returned an empty response."
                )

            elapsed = time.time() - start_time

            logger.debug(
                f"Successfully generated text in {elapsed:.2f}s"
            )

            return generated_text

        except requests.Timeout as exc:
            raise LMStudioTimeoutError(
                "LM Studio request timed out"
            ) from exc

        except requests.RequestException as exc:
            raise LMStudioConnectionError(
                f"Failed to connect to LM Studio at {self.base_url}: {exc}"
            ) from exc

        except LMStudioError:
            raise

        except Exception as exc:
            logger.exception("Unexpected error in LM Studio client")

            raise LMStudioError(
                f"Unexpected error communicating with LM Studio: {exc}"
            ) from exc

        
    def health_check(self) -> LMStudioHealthResult:
        try:
            response = requests.get(
                f"{self.base_url}/v1/models",
                timeout=self.timeout,
            )

            if response.ok:
                return LMStudioHealthResult(
                    is_healthy=True,
                    message="LM Studio server reachable",
                    details={
                        "endpoint": self.base_url,
                        "status_code": response.status_code,
                    },
                )

            return LMStudioHealthResult(
                is_healthy=False,
                message=f"LM Studio returned {response.status_code}",
                details={
                    "endpoint": self.base_url,
                    "status_code": response.status_code,
                },
            )

        except requests.Timeout:
            return LMStudioHealthResult(
                is_healthy=False,
                message="LM Studio request timed out",
            )

        except requests.RequestException as exc:
            return LMStudioHealthResult(
                is_healthy=False,
                message=str(exc),
            )
        except Exception as exc:
            logger.exception("Unexpected error during LM Studio health check")

            return LMStudioHealthResult(
                is_healthy=False,
                message=f"Unexpected error: {exc}",
            )

    # ------------------------------------------------------------------
    # Placeholder methods for future media generation
    # ------------------------------------------------------------------

    async def generate_image(self, prompt: str, **kwargs) -> bytes:
        """
        Generate an image from a text prompt using LM Studio.

        This method is currently a placeholder and will raise NotImplementedError.
        It is intended to be implemented once the LM Studio API supports image generation
        or when a suitable backend is integrated.

        Args:
            prompt (str): Text prompt describing the desired image.
            **kwargs: Additional parameters for the generation request.

        Returns:
            bytes: Raw image data.

        Raises:
            NotImplementedError: Always, until implementation is added.
        """
        raise NotImplementedError(
            "Image generation via LM Studio is not yet implemented. "
            "This method will be updated once a compatible endpoint or backend is available."
        )

    async def generate_audio(self, prompt: str, **kwargs) -> bytes:
        """
        Generate an audio clip from a text prompt using LM Studio.

        This method is currently a placeholder and will raise NotImplementedError.
        It is intended to be implemented once the LM Studio API supports audio generation
        or when a suitable backend is integrated.

        Args:
            prompt (str): Text prompt describing the desired audio content.
            **kwargs: Additional parameters for the generation request.

        Returns:
            bytes: Raw audio data.

        Raises:
            NotImplementedError: Always, until implementation is added.
        """
        raise NotImplementedError(
            "Audio generation via LM Studio is not yet implemented. "
            "This method will be updated once a compatible endpoint or backend is available."
        )

    async def generate_video(self, prompt: str, **kwargs) -> bytes:
        """
        Generate a video clip from a text prompt using LM Studio.

        This method is currently a placeholder and will raise NotImplementedError.
        It is intended to be implemented once the LM Studio API supports video generation
        or when a suitable backend is integrated.

        Args:
            prompt (str): Text prompt describing the desired video content.
            **kwargs: Additional parameters for the generation request.

        Returns:
            bytes: Raw video data.

        Raises:
            NotImplementedError: Always, until implementation is added.
        """
        raise NotImplementedError(
            "Video generation via LM Studio is not yet implemented. "
            "This method will be updated once a compatible endpoint or backend is available."
        )
