from fastapi import APIRouter
from .model import Item
from .view import ItemCreateRequest, ItemCreateResponse, ItemReadResponse

router = APIRouter()

@router.post("/items/", response_model=ItemCreateResponse)
async def create_item(item_request: ItemCreateRequest):
    """
    Create a new item

    Args:
        item_request: The request containing the item name

    Returns:
        ItemCreateResponse: A response indicating the item was created
    """
    # Use the model to create the item
    Item.create(item_request.name)

    # Return a response using the view model
    return ItemCreateResponse(message="Item added", item=item_request.name)

@router.get("/items/", response_model=ItemReadResponse)
async def read_items():
    """
    Read all items

    Returns:
        ItemReadResponse: A response containing all items
    """
    # Use the model to read all items
    items = Item.read()

    # Return a response using the view model
    return ItemReadResponse(items=items)
