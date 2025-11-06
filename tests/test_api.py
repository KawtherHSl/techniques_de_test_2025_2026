import pytest
from triangulator.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_api_returns_501(client):
    response = client.get('/triangulation/123e4567-e89b-12d3-a456-426614174000')
    assert response.status_code == 501
