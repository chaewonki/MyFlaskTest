import pytest
from flaskapp import app  # Import the actual app, no need for create_app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    # Test the index route
    response = client.get('/')
    assert response.status_code == 200
    assert b"Add Item" in response.data  # Check if there's an 'Add Item' button or link in index.html

def test_add_item(client):
    # Test adding an item via POST request
    response = client.post('/add_item', data={'item': 'Test Item'})
    assert response.status_code == 302  # Should redirect after posting

    # Follow the redirect to check the final result
    response = client.get('/')
    assert b"Test Item" in response.data  # Ensure that the added item appears on the index page

def test_delete_item(client):
    # First, add an item to delete
    client.post('/add_item', data={'item': 'Item to Delete'})

    # Now, delete that item
    response = client.get('/delete_item/0')  # Item at index 0
    assert response.status_code == 302  # Should redirect after deletion

    # Follow the redirect to check the final result
    response = client.get('/')
    assert b"Item to Delete" not in response.data  # Ensure the item is removed from the index
