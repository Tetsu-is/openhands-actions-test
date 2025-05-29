import pytest
from model import Item


@pytest.fixture
def item_instance():
    """テスト用のItemインスタンスを作成"""
    item = Item()
    yield item
    item.clear()


def test_create_item(item_instance):
    """アイテム作成のテスト"""
    result = item_instance.create("テストアイテム")
    assert result is True

    items = item_instance.read()
    assert "テストアイテム" in items


def test_read_empty_items(item_instance):
    """空の状態でのアイテム読み込みテスト"""
    items = item_instance.read()
    assert items == []


def test_read_multiple_items(item_instance):
    """複数アイテムの読み込みテスト"""
    item_instance.create("アイテム1")
    item_instance.create("アイテム2")
    item_instance.create("アイテム3")

    items = item_instance.read()
    assert len(items) == 3
    assert "アイテム1" in items
    assert "アイテム2" in items
    assert "アイテム3" in items


def test_read_returns_copy(item_instance):
    """readメソッドがコピーを返すことのテスト"""
    item_instance.create("テストアイテム")

    items1 = item_instance.read()
    items2 = item_instance.read()

    # 異なるオブジェクトであることを確認
    assert items1 is not items2
    # 内容は同じであることを確認
    assert items1 == items2


def test_clear_items(item_instance):
    """アイテムクリアのテスト"""
    item_instance.create("アイテム1")
    item_instance.create("アイテム2")

    assert len(item_instance.read()) == 2

    item_instance.clear()
    assert len(item_instance.read()) == 0
