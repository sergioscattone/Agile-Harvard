# tests/test_app.py

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client


def get_context_variable(response_data):
    # Helper function to extract a variable from the template context
    start = response_data.find(b'{{') + 2
    end = response_data.find(b'}}')
    variable = response_data[start:end].strip()
    return variable


def testing_framework_works():
    assert True


def test_login_page(client):
    """Test welcome page"""
    rv = client.get('/login')
    assert rv.status_code == 200


# def test_welcome_title(client):
#     """Test welcome title"""
#     rv = client.get('/')
#     assert b'Welcome' in rv.data


def test_incorrect_page(client):
    rv = client.post('/sites')
    assert rv.status_code == 404


# if there is no login then return not allowed
def test_not_allowed_exercise_page(client):
    rv = client.post('/exercises')
    assert rv.status_code == 404


# check that there is at least 1 exercise in the list
def test_check_exercises_number(client):
    rv = client.post('/exercises')
    exercises = get_context_variable(rv.data)
    assert len(exercises) >= 1


def test_exercise_bicep_curl_details_page(client):
    rv = client.get('/exercises/Bicep_Curl')
    assert rv.status_code == 200


def test_exercise_jackknife_situps_details_page(client):
    rv = client.get('/exercises/Jacknife_Situps')
    assert rv.status_code == 200


def test_exercise_jogging_details_page(client):
    rv = client.get('/exercises/Jogging')
    assert rv.status_code == 200


def test_exercise_hiking_details_page(client):
    rv = client.get('/exercises/Hiking')
    assert rv.status_code == 200


def test_exercise_table_tennis_page(client):
    rv = client.get('/exercises/Table_Tennis')
    assert rv.status_code == 200
