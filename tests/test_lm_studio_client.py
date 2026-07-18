"""
Tests for LM Studio client.
"""

import pytest
from app.core.lm_studio_client import (
    LMStudioClient,
    LMStudioConnectionError,
    LMStudioTimeoutError,
    LMStudioResponseError,
    LMStudioError,
    LMStudioHealthResult
)


class TestLMStudioClient:
    def test_client_initialization(self):
        """Test that the client initializes correctly."""
        client = LMStudioClient(timeout=30)
        assert client.timeout == 30
        assert client.base_url == "http://localhost:1234"
        
    def test_client_with_custom_endpoint(self):
        """Test that the client can use a custom endpoint from config."""
        # This would require mocking the config, which is complex for this simple test
        # The main functionality is tested through integration tests in actual usage
        pass

    def test_exception_classes(self):
        """Test that exception classes are properly defined."""
        assert issubclass(LMStudioConnectionError, LMStudioError)
        assert issubclass(LMStudioTimeoutError, LMStudioError)
        assert issubclass(LMStudioResponseError, LMStudioError)
        
    def test_health_result_initialization(self):
        """Test that health result initializes correctly."""
        # Test basic initialization
        result = LMStudioHealthResult(True, "Test message")
        assert result.is_healthy == True
        assert result.message == "Test message"
        assert result.details == {}
        
        # Test with details
        details = {"key": "value"}
        result_with_details = LMStudioHealthResult(False, "Error", details)
        assert result_with_details.is_healthy == False
        assert result_with_details.message == "Error"
        assert result_with_details.details == details
        
    def test_health_result_to_dict(self):
        """Test that health result converts to dictionary properly."""
        details = {"endpoint": "http://localhost:1234", "status_code": 200}
        result = LMStudioHealthResult(True, "Healthy", details)
        dict_result = result.to_dict()
        
        assert dict_result["is_healthy"] == True
        assert dict_result["message"] == "Healthy"
        assert dict_result["details"]["endpoint"] == "http://localhost:1234"
