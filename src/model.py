from typing import List

class Item:
    _item_list: List[str] = []  # Class variable to store items

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def create(cls, name: str) -> str:
        """
        Create a new item and add it to the item list

        Args:
            name: The name of the item to create

        Returns:
            The name of the created item
        """
        cls._item_list.append(name)
        return name

    @classmethod
    def read(cls) -> List[str]:
        """
        Read all items from the item list

        Returns:
            A list of all item names
        """
        return cls._item_list.copy()
