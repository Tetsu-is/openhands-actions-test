class Item:
    # Class variable to store items (acting as a database)
    _item_list = []

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def create(cls, name: str) -> bool:
        """
        Create a new item and add it to the item list

        Args:
            name: The name of the item to create

        Returns:
            bool: True if the item was successfully created
        """
        cls._item_list.append(name)
        return True

    @classmethod
    def read(cls) -> list[str]:
        """
        Read all items from the item list

        Returns:
            list[str]: A list of all item names
        """
        return cls._item_list.copy()

    @classmethod
    def delete(cls, name: str) -> bool:
        """
        Delete an item from the item list

        Args:
            name: The name of the item to delete

        Returns:
            bool: True if the item was found and deleted, False otherwise
        """
        if name in cls._item_list:
            cls._item_list.remove(name)
            return True
        return False
