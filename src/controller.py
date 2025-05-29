from fastapi import APIRouter
from src.model import Item
from src.view import ItemCreateRequest, ItemCreateResponse, ItemReadResponse

router = APIRouter()

@router.post("/items/", response_model=ItemCreateResponse)
async def create_item(request: ItemCreateRequest):
    item_name = Item.create(request.name)
    return ItemCreateResponse(message="Item added", item=item_name)

@router.get("/items/", response_model=ItemReadResponse)
async def read_items():
    items = Item.read()
    return ItemReadResponse(items=items)
