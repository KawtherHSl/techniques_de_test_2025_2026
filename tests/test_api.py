"""Tests de l'API triangulator"""


import struct
from unittest.mock import patch

import pytest
import requests
import requests_mock

from triangulator.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


def test_api_valid(client):
    """Test que l'API valide"""
    ps_data = struct.pack('<Iffff', 2, 0.0, 0.0, 1.0, 1.0)
    with requests_mock.Mocker() as m:
        m.get("http://pointsetmanager/pointset/1", content=ps_data)
        response = client.get("/triangulate/1")
    assert response.status_code == 200
    assert len(response.data) > 0

def test_api_not_found(client):
    """Test que l'API not found"""
    with requests_mock.Mocker() as m:
        m.get("http://pointsetmanager/pointset/99", status_code=404)
        response = client.get("/triangulate/99")
    assert response.status_code == 404


def test_api_empty_pointset(client):
    """Test que PointSet vide"""
    ps_data = struct.pack('<I', 0)
    with requests_mock.Mocker() as m:
        m.get("http://pointsetmanager/pointset/2", content=ps_data)
        response = client.get("/triangulate/2")
    assert response.status_code == 400
    assert b"empty" in response.data


def test_api_manager_unavailable(client):
    """Test que PointSetManager indisponible"""
    with patch("triangulator.app.requests.get", 
               side_effect=requests.exceptions.ConnectTimeout
               ):
        response = client.get("/triangulate/3")
    assert response.status_code == 503
    assert b"unavailable" in response.data

