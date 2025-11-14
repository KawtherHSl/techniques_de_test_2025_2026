import pytest
from triangulator.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_api_not_found(client):
    response = client.get('/triangulation/unknown-id')
    assert response.status_code == 404

def test_api_success(client):
    response = client.get('/triangulation/triangulable')
    assert response.status_code == 200

def test_api_returns_501(client):
    response = client.get('/triangulation/collinear')
    assert response.status_code == 501




