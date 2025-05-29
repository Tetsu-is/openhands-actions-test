from view import ItemCreateRequest, ItemCreateResponse, ItemReadRequest, ItemReadResponse


def test_item_create_request():
    """ItemCreateRequestのテスト"""
    request = ItemCreateRequest(name="テストアイテム")
    assert request.name == "テストアイテム"


def test_item_create_response():
    """ItemCreateResponseのテスト"""
    response = ItemCreateResponse(message="Item added", item="テストアイテム")
    assert response.message == "Item added"
    assert response.item == "テストアイテム"


def test_item_read_request():
    """ItemReadRequestのテスト"""
    request = ItemReadRequest()
    # GETリクエストなので特にパラメータはない
    assert request is not None


def test_item_read_response():
    """ItemReadResponseのテスト"""
    items = ["アイテム1", "アイテム2", "アイテム3"]
    response = ItemReadResponse(items=items)
    assert response.items == items


def test_item_read_response_empty():
    """空のItemReadResponseのテスト"""
    response = ItemReadResponse(items=[])
    assert response.items == []
