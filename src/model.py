from typing import List
import asyncio
from fastapi import Depends

class ItemStore:
    """
    Thread-safe data store for items using asyncio.Lock for concurrency control.

    This class provides a safe way to store and retrieve items in an asynchronous
    environment like FastAPI. It uses asyncio.Lock to ensure that only one
    operation can modify the items list at a time.
    """
    def __init__(self):
        self._items: List[str] = []
        self._lock = asyncio.Lock()

    async def add_item(self, name: str) -> str:
        """
        Add an item to the store in a thread-safe manner.

        Args:
            name: The name of the item to add

        Returns:
            The name of the added item
        """
        async with self._lock:
            self._items.append(name)
            return name

    async def get_items(self) -> List[str]:
        """
        Get all items from the store in a thread-safe manner.

        Returns:
            A copy of the items list to prevent external modification
        """
        async with self._lock:
            return self._items.copy()

# Create a singleton instance for dependency injection
_item_store = ItemStore()

def get_item_store() -> ItemStore:
    """
    Dependency injection function to get the ItemStore singleton.

    This function is used with FastAPI's dependency injection system to provide
    the same ItemStore instance to all endpoints that need it.

    Returns:
        The singleton ItemStore instance
    """
    return _item_store

class Item:
    """
    Domain model class for Item with static methods to interact with the ItemStore.

    This class provides a clean API for creating and reading items, while delegating
    the actual storage operations to the ItemStore.
    """
    @staticmethod
    async def create(name: str, store: ItemStore = Depends(get_item_store)) -> str:
        """
        Create a new item.

        Args:
            name: The name of the item to create
            store: The ItemStore to use (injected by FastAPI)

        Returns:
            The name of the created item
        """
        return await store.add_item(name)

    @staticmethod
    async def read(store: ItemStore = Depends(get_item_store)) -> List[str]:
        """
        Read all items.

        Args:
            store: The ItemStore to use (injected by FastAPI)

        Returns:
            A list of all items
        """
        return await store.get_items()
