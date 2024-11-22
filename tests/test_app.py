import pytest
from flaskapp import create_app

@pytest.fixture
def app():
    # Create a test version of the app
    app = create_app()
    app.testing = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    # Test the index route
    response = client.get('/')
    assert response.status_code == 200
    assert b"Add Item" in response.data  # Assuming your index.html contains an 'Add Item' button

def test_add_item(client):
    # Test adding an item via POST request
    response = client.post('/add_item', data={'item': 'Test Item'})
    assert response.status_code == 302  # Should redirect after posting
    assert b"Test Item" in response.data  # Should appear in the index view
