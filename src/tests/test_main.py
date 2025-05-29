from fastapi.testclient import TestClient
from main import app
from model import item_model
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_data():
    """各テストの前後でデータをクリアする"""
    item_model.clear()
    yield
    item_model.clear()


def test_create_item():
    response = client.post("/items/", json={"name": "テストアイテム"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item added", "item": "テストアイテム"}


def test_read_items():
    # 最初にアイテムを追加
    client.post("/items/", json={"name": "テストアイテム1"})
    client.post("/items/", json={"name": "テストアイテム2"})
    
    # アイテムを取得して検証
    response = client.get("/items/")
    assert response.status_code == 200
    assert "テストアイテム1" in response.json()["items"]
    assert "テストアイテム2" in response.json()["items"]


def test_read_empty_items():
    """空の状態でアイテムを取得するテスト"""
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"items": []}
