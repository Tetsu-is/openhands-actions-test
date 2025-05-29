from fastapi import APIRouter
from src.model import Item
from src.view import ItemCreateRequest, ItemCreateResponse, ItemReadResponse

router = APIRouter()

@router.post("/items/", response_model=ItemCreateResponse)
async def create_item(item_request: ItemCreateRequest):
    """
    Create a new item

    Args:
        item_request: The request containing the item name

    Returns:
        A response indicating the item was added successfully
    """
    item_name = Item.create(item_request.name)
    return ItemCreateResponse(message="Item added", item=item_name)

@router.get("/items/", response_model=ItemReadResponse)
async def read_items():
    """
    Read all items

    Returns:
        A response containing all items
    """
    items = Item.read()
    return ItemReadResponse(items=items)
