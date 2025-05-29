from fastapi.testclient import TestClient
from src.main import app
from src.model import Item

client = TestClient(app)

def test_app_endpoints():
    # Clear the item list before testing
    Item._item_list = []

    # Test that the app has the correct endpoints
    response = client.post("/items/", json={"name": "テストアイテム"})
    assert response.status_code == 200
    
    response = client.get("/items/")
    assert response.status_code == 200
