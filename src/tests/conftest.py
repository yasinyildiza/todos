import fastapi.testclient
import pytest

from todos import app

@pytest.fixture
def test_client():
    client = fastapi.testclient.TestClient(app)

    yield client
