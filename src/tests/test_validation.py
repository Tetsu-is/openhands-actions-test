import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.model import Item, ValidationError

client = TestClient(app)

def test_item_validation_model():
    """Test the validation in the Item model"""
    # Test valid item name
    assert Item.validate_name("Valid Item") is None  # Should not raise an exception

    # Test empty item name
    with pytest.raises(ValidationError):
        Item.validate_name("")

    # Test too long item name
    with pytest.raises(ValidationError):
        Item.validate_name("This is a very long item name that exceeds the limit")

    # Test edge cases
    assert Item.validate_name("A") is None  # 1 character (minimum)
    assert Item.validate_name("ABCDEFGHIJKLMNO") is None  # 15 characters (maximum)
    with pytest.raises(ValidationError):
        Item.validate_name("ABCDEFGHIJKLMNOP")  # 16 characters (exceeds maximum)

def test_api_validation():
    """Test the validation in the API endpoints"""
    # Test valid item name
    response = client.post("/api/items/", json={"name": "Valid Item"})
    assert response.status_code == 200
    assert response.json()["message"] == "Item added"

    # Test empty item name
    response = client.post("/api/items/", json={"name": ""})
    assert response.status_code == 422  # Pydantic validation returns 422
    assert "アイテム名は1文字以上15文字以下で入力してください" in response.text

    # Test too long item name
    response = client.post("/api/items/", json={"name": "This is a very long item name that exceeds the limit"})
    assert response.status_code == 422  # Pydantic validation returns 422
    assert "アイテム名は1文字以上15文字以下で入力してください" in response.text

def test_form_validation():
    """Test the validation in the form submission"""
    # Test valid item name
    response = client.post("/items/", data={"name": "Valid Item"}, follow_redirects=False)
    assert response.status_code == 303  # Redirect status code

    # Test empty item name
    response = client.post("/items/", data={"name": ""})
    assert response.status_code == 200  # Returns the form with an error message
    assert "アイテム名は1文字以上15文字以下で入力してください" in response.text

    # Test too long item name
    response = client.post("/items/", data={"name": "This is a very long item name that exceeds the limit"})
    assert response.status_code == 200  # Returns the form with an error message
    assert "アイテム名は1文字以上15文字以下で入力してください" in response.text
