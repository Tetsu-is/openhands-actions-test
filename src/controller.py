from fastapi import APIRouter, Depends
from src.model import Item, ItemStore, get_item_store
from src.view import ItemCreateRequest, ItemCreateResponse, ItemReadResponse

# Create a router for item-related endpoints
router = APIRouter()

@router.post("/items/", response_model=ItemCreateResponse)
async def create_item(request: ItemCreateRequest, store: ItemStore = Depends(get_item_store)):
    """
    Create a new item endpoint.

    This endpoint receives an ItemCreateRequest, uses the Item model to create
    a new item in the store, and returns an ItemCreateResponse.

    Args:
        request: The request containing the item name
        store: The ItemStore instance (injected by FastAPI)

    Returns:
        An ItemCreateResponse with a success message and the created item
    """
    item_name = await Item.create(request.name, store)
    return ItemCreateResponse(message="Item added", item=item_name)

@router.get("/items/", response_model=ItemReadResponse)
async def read_items(store: ItemStore = Depends(get_item_store)):
    """
    Read all items endpoint.

    This endpoint uses the Item model to read all items from the store
    and returns them in an ItemReadResponse.

    Args:
        store: The ItemStore instance (injected by FastAPI)

    Returns:
        An ItemReadResponse containing all items
    """
    items = await Item.read(store)
    return ItemReadResponse(items=items)
