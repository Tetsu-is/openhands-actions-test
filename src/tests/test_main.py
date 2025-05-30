from fastapi.testclient import TestClient
from src.main import app
from src.model import Item

client = TestClient(app)

def setup_function():
    # Reset the item list before each test
    Item._item_list = []

def test_create_item():
    response = client.post("/api/items/", json={"name": "テストアイテム"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item added", "item": "テストアイテム"}

def test_read_items():
    # 最初にアイテムを追加
    client.post("/api/items/", json={"name": "テストアイテム1"})
    client.post("/api/items/", json={"name": "テストアイテム2"})
    
    # アイテムを取得して検証
    response = client.get("/api/items/")
    assert response.status_code == 200
    assert "テストアイテム1" in response.json()["items"]
    assert "テストアイテム2" in response.json()["items"]
