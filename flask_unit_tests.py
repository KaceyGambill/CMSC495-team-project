import pytest
from flask import current_app

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"  # Error!
            yield client


def test_index_page(client):
   response = client.get('/')

   assert response.status_code == 200
   assert b'Welcome!' in response.data

def test_jobs_page(client):
   response = client.get('/jobs')

   assert response.status_code == 200
   assert b'jobs' in response.data

def test_resume_page(client):
   response = client.get('/resume')

   assert response.status_code == 200
   assert b'resume' in response.data

def test_resume_page(client):
   response = client.get('/interview')

   assert response.status_code == 200
   assert b'interview' in response.data