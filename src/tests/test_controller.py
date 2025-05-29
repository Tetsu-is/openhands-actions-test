import pytest
from controller import create_item_controller, read_items_controller
from view import ItemCreateRequest, ItemCreateResponse, ItemReadResponse
from model import item_model


@pytest.fixture(autouse=True)
def clear_data():
    """各テストの前後でデータをクリアする"""
    item_model.clear()
    yield
    item_model.clear()


def test_create_item_controller():
    """create_item_controllerのテスト"""
    request = ItemCreateRequest(name="テストアイテム")
    response = create_item_controller(request)

    assert isinstance(response, ItemCreateResponse)
    assert response.message == "Item added"
    assert response.item == "テストアイテム"

    # モデルにも正しく保存されていることを確認
    items = item_model.read()
    assert "テストアイテム" in items


def test_read_items_controller_empty():
    """空の状態でのread_items_controllerのテスト"""
    response = read_items_controller()

    assert isinstance(response, ItemReadResponse)
    assert response.items == []


def test_read_items_controller_with_data():
    """データがある状態でのread_items_controllerのテスト"""
    # 事前にデータを追加
    item_model.create("アイテム1")
    item_model.create("アイテム2")

    response = read_items_controller()

    assert isinstance(response, ItemReadResponse)
    assert len(response.items) == 2
    assert "アイテム1" in response.items
    assert "アイテム2" in response.items


def test_create_and_read_integration():
    """作成と読み込みの統合テスト"""
    # アイテムを作成
    create_request = ItemCreateRequest(name="統合テストアイテム")
    create_response = create_item_controller(create_request)

    assert create_response.message == "Item added"
    assert create_response.item == "統合テストアイテム"

    # アイテムを読み込み
    read_response = read_items_controller()

    assert len(read_response.items) == 1
    assert "統合テストアイテム" in read_response.items
