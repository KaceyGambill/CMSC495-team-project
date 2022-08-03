
import pytest
from flask import current_app
import time
from app import app
#8822-b

# Create client and app contexts for testing flask
# Functions
@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"  # Error!
            yield client

##########****** Functional tests ******#############

# # Test flask app index page function
# def test_index_page(client):
#    response = client.get('/')
#    assert response.status_code == 200
#
# # Test flask app jobs page function
# def test_jobs_page(client):
#    response = client.get('/jobs')
#
#    assert response.status_code == 200
#    assert b'jobs' in response.data
#
# # Test flask app resume page function
# def test_resume_page(client):
#    response = client.get('/resume')
#
#    assert response.status_code == 200
#    assert b'resume' in response.data
#
# # Test flask app interview page function
# def test_interview_page(client):
#    response = client.get('/interview')
#
#    assert response.status_code == 200
#    assert b'interview' in response.data

##########****** Performance tests ******#############

# Test flask app index page function performance
def test_interview_page_performance(client):
    start = time.time()
    response = client.get('/interview')
    if response.status_code == 200:
        stop = time.time()
    else:
        print(response)
    total_time = stop - start
    assert total_time < .015

# Test flask app index page function performance
def test_resume_page_performance(client):
    start = time.time()
    response = client.get('/resume')
    if response.status_code == 200:
        stop = time.time()
    else:
        print(response)
    total_time = stop - start
    assert total_time < .015

# Test flask app index page function performance
def test_jobs_page_performance(client):
    start = time.time()
    response = client.get('/jobs')
    if response.status_code == 200:
        stop = time.time()
    else:
        print(response)
    total_time = stop - start
    assert total_time < .015

#Test flask app index page function performance
def test_index_page_performance(client):
    start = time.time()
    response = client.get('/')
    if response.status_code == 200:
        stop = time.time()
    else:
        print(response)
    total_time = stop - start
    assert total_time < .015




