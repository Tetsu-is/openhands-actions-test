class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class Item:
    # Class variable to store items (acting as a database)
    _item_list = []

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def validate_name(name: str) -> None:
        """
        Validate the item name

        Args:
            name: The name to validate

        Raises:
            ValidationError: If the name is invalid
        """
        if not isinstance(name, str):
            raise ValidationError("アイテム名は文字列である必要があります")

        if len(name) < 1 or len(name) > 15:
            raise ValidationError("アイテム名は1文字以上15文字以下で入力してください")

    @classmethod
    def create(cls, name: str) -> bool:
        """
        Create a new item and add it to the item list

        Args:
            name: The name of the item to create

        Returns:
            bool: True if the item was successfully created

        Raises:
            ValidationError: If the name is invalid
        """
        # Validate the name before creating
        cls.validate_name(name)

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
