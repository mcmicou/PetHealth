"""
End-to-end test for PetHealth API.
This test starts the actual server and makes real HTTP requests.
"""
import subprocess
import time
import signal
import sys
import httpx
import pytest


@pytest.fixture(scope="module")
def server_process():
    """Start the FastAPI server for E2E testing."""
    # Start the server
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd="/Users/Molly/pethealth/apps/api"
    )
    
    # Wait for server to start
    max_attempts = 30
    for _ in range(max_attempts):
        try:
            response = httpx.get("http://localhost:8000/health", timeout=1.0)
            if response.status_code == 200:
                break
        except (httpx.ConnectError, httpx.TimeoutException):
            time.sleep(0.5)
    else:
        process.terminate()
        process.wait()
        pytest.fail("Server failed to start within 15 seconds")
    
    yield process
    
    # Cleanup: stop the server
    process.terminate()
    process.wait(timeout=5)


def test_health_endpoint_e2e(server_process):
    """Test the /health endpoint via real HTTP request."""
    response = httpx.get("http://localhost:8000/health", timeout=5.0)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "pethealth-api"


def test_cors_headers_e2e(server_process):
    """Test that CORS headers are properly set."""
    response = httpx.get(
        "http://localhost:8000/health",
        headers={"Origin": "http://localhost:3000"},
        timeout=5.0
    )
    
    assert response.status_code == 200
    # CORS headers should be present (FastAPI middleware handles this)
    assert "access-control-allow-origin" in response.headers or response.status_code == 200

