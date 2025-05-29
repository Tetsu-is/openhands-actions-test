from pydantic import BaseModel
from typing import List


class ItemCreateRequest(BaseModel):
    """アイテム作成リクエストのデータ構造"""
    name: str


class ItemCreateResponse(BaseModel):
    """アイテム作成レスポンスのデータ構造"""
    message: str
    item: str


class ItemReadRequest(BaseModel):
    """アイテム読み込みリクエストのデータ構造"""
    # GETリクエストなので特にパラメータは不要
    pass


class ItemReadResponse(BaseModel):
    """アイテム読み込みレスポンスのデータ構造"""
    items: List[str]
