import pytest
from triangulator.app import create_app
import requests_mock
import struct

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_api_valid(client):
    
    ps_data = struct.pack('<Iffff', 2, 0.0, 0.0, 1.0, 1.0)

    with requests_mock.Mocker() as m:
        m.get("http://pointsetmanager/pointset/1", content=ps_data)
        response = client.get("/triangulate/1")

    assert response.status_code == 200
    assert len(response.data) > 0

def test_api_not_found(client):
    with requests_mock.Mocker() as m:
        m.get("http://pointsetmanager/pointset/99", status_code=404)
        response = client.get("/triangulate/99")

    assert response.status_code == 404
