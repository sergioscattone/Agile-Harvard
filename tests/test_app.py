# tests/test_app.py

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client


def get_context_variable(response_data, variable_name):
    # Helper function to extract a variable from the template context
    start = response_data.find(b'{{') + 2
    end = response_data.find(b'}}')
    variable = response_data[start:end].strip()
    return variable


def testing_framework_works():
    assert True


def test_welcome_page(client):
    """Test welcome page"""
    rv = client.get('/')
    assert rv.status_code == 200


def test_welcome_title(client):
    """Test welcome title"""
    rv = client.get('/')
    assert b'Welcome' in rv.data


# check submit page exists
def test_exercise_page(client):
    """Test list page"""
    rv = client.post('/exercise')
    assert rv.status_code == 200


# check that there is at least 1 exercise in the list
def test_check_exercises_number(client):
    rv = client.post('/exercise')
    sites = get_context_variable(rv.data, b'sites')
    assert len(sites) >= 1


def test_exercise_bicep_curl_details_page(client):
    rv = client.get('/site/Bicep_Curl')
    assert rv.status_code == 200


def test_exercise_jackknife_situps_details_page(client):
    rv = client.get('/site/Jacknife_Situps')
    assert rv.status_code == 200

def test_exercise_jogging_details_page(client):
    rv = client.get('/site/Jogging')
    assert rv.status_code == 200

def test_exercise_hiking_details_page(client):
    rv = client.get('/site/Hiking')
    assert rv.status_code == 200

def test_exercise_table_tennis_page(client):
    rv = client.get('/site/Table_Tennis')
    assert rv.status_code == 200