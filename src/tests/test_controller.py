from fastapi.testclient import TestClient
from src.main import app
from src.model import Item

client = TestClient(app)

def test_create_item():
    # Clear the item list before testing
    Item._item_list = []

    # Test creating an item
    response = client.post("/items/", json={"name": "テストアイテム"})

    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"message": "Item added", "item": "テストアイテム"}

    # Verify the item was added to the model
    assert "テストアイテム" in Item._item_list

def test_read_items():
    # Clear the item list and add test items
    Item._item_list = []
    test_items = ["テストアイテム1", "テストアイテム2"]
    for item in test_items:
        Item.create(item)

    # Test reading items
    response = client.get("/items/")

    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"items": test_items}
