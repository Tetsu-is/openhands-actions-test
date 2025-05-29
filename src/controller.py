from model import item_model
from view import ItemCreateRequest, ItemCreateResponse, ItemReadResponse


def create_item_controller(request: ItemCreateRequest) -> ItemCreateResponse:
    """アイテム作成のコントローラー

    Args:
        request (ItemCreateRequest): アイテム作成リクエスト

    Returns:
        ItemCreateResponse: アイテム作成レスポンス
    """
    # modelを使ってデータの永続化領域を操作
    success = item_model.create(request.name)

    if success:
        # viewクラスを使ってレスポンスデータ構造を作成
        return ItemCreateResponse(
            message="Item added",
            item=request.name
        )
    else:
        # エラーケース（現在の実装では常に成功するが、将来の拡張のため）
        return ItemCreateResponse(
            message="Failed to add item",
            item=request.name
        )


def read_items_controller() -> ItemReadResponse:
    """アイテム読み込みのコントローラー

    Returns:
        ItemReadResponse: アイテム読み込みレスポンス
    """
    # modelを使ってデータを読み出し
    items = item_model.read()

    # viewクラスを使ってレスポンスデータ構造を作成
    return ItemReadResponse(items=items)
