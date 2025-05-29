from src.model import Item

def test_item_create():
    # Clear the item list before testing
    Item._item_list = []

    # Test creating an item
    item_name = "テストアイテム"
    result = Item.create(item_name)

    # Verify the result
    assert result == item_name
    assert item_name in Item._item_list

def test_item_read():
    # Clear the item list and add test items
    Item._item_list = []
    test_items = ["テストアイテム1", "テストアイテム2"]
    for item in test_items:
        Item.create(item)

    # Test reading items
    result = Item.read()

    # Verify the result
    assert result == test_items
    # Ensure the returned list is a copy
    assert result is not Item._item_list
