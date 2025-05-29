from typing import List, Optional


class Item:
    """ドメインモデルクラス - アプリケーション内で扱うItemを表現する"""

    def __init__(self):
        # データベースの役割をする配列
        self._item_list: List[str] = []

    def create(self, item_name: str) -> bool:
        """Itemを追加するメソッド

        Args:
            item_name (str): 追加するアイテムの名前

        Returns:
            bool: 追加が成功した場合True
        """
        self._item_list.append(item_name)
        return True

    def read(self) -> List[str]:
        """Itemを読み込むメソッド

        Returns:
            List[str]: 格納されているアイテムのリスト
        """
        return self._item_list.copy()

    def clear(self) -> None:
        """テスト用: アイテムリストをクリアする"""
        self._item_list.clear()


# シングルトンインスタンス
item_model = Item()
