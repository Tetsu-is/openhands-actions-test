from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_root_redirect():
    """Test that the root path redirects to /items"""
    response = client.get("/")
    assert str(response.url).endswith("/items")

def test_items_list_html():
    """Test that the items list HTML endpoint returns a valid HTML page"""
    response = client.get("/items")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "アイテム一覧" in response.text

def test_item_create_form():
    """Test that the item creation form HTML endpoint returns a valid HTML page"""
    response = client.get("/items/create")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "新しいアイテムを作成" in response.text
    assert '<form action="/items/" method="post">' in response.text

def test_item_create_submit():
    """Test that submitting the item creation form works correctly"""
    # First, get the current items
    response = client.get("/api/items/")
    initial_items = response.json()["items"]

    # Submit a new item
    response = client.post(
        "/items/",
        data={"name": "Test Item"},
        follow_redirects=False
    )

    # Check that we get redirected to the items list
    assert response.status_code == 303
    assert response.headers["location"] == "/items"

    # Check that the item was added
    response = client.get("/api/items/")
    new_items = response.json()["items"]
    assert len(new_items) == len(initial_items) + 1
    assert "Test Item" in new_items

def test_item_delete():
    """Test that deleting an item via the HTML endpoint works correctly"""
    # First, create an item
    client.post(
        "/items/",
        data={"name": "Item To Delete"},
        follow_redirects=False
    )

    # Verify the item exists
    response = client.get("/api/items/")
    assert "Item To Delete" in response.json()["items"]

    # Delete the item
    response = client.delete(
        "/items/",
        params={"items": "Item To Delete"},
        follow_redirects=False
    )

    # Check that we get redirected to the items list
    assert response.status_code == 303
    assert response.headers["location"] == "/items"

    # Verify the item was deleted
    response = client.get("/api/items/")
    assert "Item To Delete" not in response.json()["items"]

def test_item_delete_nonexistent():
    """Test deleting a non-existent item via the HTML endpoint"""
    # Get current items
    response = client.get("/api/items/")
    initial_items = response.json()["items"]

    # Delete a non-existent item
    response = client.delete(
        "/items/",
        params={"items": "Non-Existent Item"},
        follow_redirects=False
    )

    # Check that we still get redirected to the items list
    assert response.status_code == 303
    assert response.headers["location"] == "/items"

    # Verify no items were deleted
    response = client.get("/api/items/")
    assert response.json()["items"] == initial_items
