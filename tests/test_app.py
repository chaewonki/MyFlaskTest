# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test that index page loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'My Item List' in rv.data

def test_add_item(client):
    """Test adding an item"""
    rv = client.post('/add_item', data=dict(
        item='Test Item'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Item' in rv.data

def test_delete_item(client):
    """Test deleting an item"""
    # First add an item
    client.post('/add_item', data=dict(
        item='Test Item'
    ), follow_redirects=True)
    
    # Then delete it
    rv = client.get('/delete_item/0', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Item' not in rv.data