# import unittest
#
# from app import app
#
# class AppTestCase(unittest.TestCase):
#     def setUp(self):
#         self.ctx = app.app_context()
#         self.ctx.push()
#         self.client = app.test_client()
#
#     def tearDown(self):
#         self.ctx.pop()
#
#     def test_home(self):
#         response = self.client.post("/")
#         assert response.status_code == 200
#         assert "POST method called" == response.get_data(as_text=True)
#
# if __name__ == "__main__":
#     unittest.main()

import pytest
from app import homepage

@pytest.fixture()
def app():
    app = homepage()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_index_page(self, client):
   response = client.get('/')

   assert response.status_code == 200
   assert b'Welcome!' in response.data

if __name__=="__main__":