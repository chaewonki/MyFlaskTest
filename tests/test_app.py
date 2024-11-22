# tests/test_app.py
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flaskapp.app import app, items


@pytest.fixture
def client():
    app.config["TESTING"] = True
    # Clear items before each test
    items.clear()
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Test that index page loads correctly"""
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"My Item List" in rv.data


def test_add_item(client):
    """Test adding an item"""
    rv = client.post("/add_item", data=dict(item="Test Item"), follow_redirects=True)
    assert rv.status_code == 200
    assert b"Test Item" in rv.data


def test_delete_item(client):
    """Test deleting an item"""
    # First add an item
    client.post("/add_item", data=dict(item="Test Item"), follow_redirects=True)

    # Then delete it
    rv = client.get("/delete_item/0", follow_redirects=True)
    assert rv.status_code == 200
    assert b"Test Item" not in rv.data
