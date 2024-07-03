# tests/test_app.py

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client


def testing_framework_works():
    assert True


def test_welcome(client):
    """Test welcome page"""
    rv = client.get('/')
    assert b'Welcome' in rv.data
