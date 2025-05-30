from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .model import Item
from .view import (
    ItemCreateRequest, ItemCreateResponse,
    ItemReadResponse, ItemDeleteRequest, ItemDeleteResponse
)

# テンプレートディレクトリの設定
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

router = APIRouter()

# API エンドポイント
from fastapi import HTTPException

@router.post("/api/items/", response_model=ItemCreateResponse)
async def create_item_api(item_request: ItemCreateRequest):
    """
    Create a new item via API

    Args:
        item_request: The request containing the item name

    Returns:
        ItemCreateResponse: A response indicating the item was created

    Raises:
        HTTPException: If validation fails
    """
    try:
        # Use the model to create the item
        Item.create(item_request.name)

        # Return a response using the view model
        return ItemCreateResponse(message="Item added", item=item_request.name)
    except ValidationError as e:
        raise HTTPException(
            status_code=400,
            detail="アイテム名は1文字以上15文字以下で入力してください"
        )

@router.get("/api/items/", response_model=ItemReadResponse)
async def read_items_api():
    """
    Read all items via API

    Returns:
        ItemReadResponse: A response containing all items
    """
    # Use the model to read all items
    items = Item.read()

    # Return a response using the view model
    return ItemReadResponse(items=items)

# HTML テンプレートを使用したエンドポイント
@router.get("/items", response_class=HTMLResponse)
async def read_items_html(request: Request):
    """
    Read all items and render HTML template
    """
    items = Item.read()
    return templates.TemplateResponse(
        request,
        "item_list.html",
        {"items": items}
    )

@router.get("/items/create", response_class=HTMLResponse)
async def create_item_form(request: Request, message: str = None):
    """
    Render the item creation form
    """
    return templates.TemplateResponse(
        request,
        "item_create.html",
        {"message": message}
    )

from pydantic import ValidationError

@router.post("/items/", response_class=HTMLResponse)
async def create_item_submit(request: Request, name: str = Form(...)):
    """
    Process the item creation form submission
    """
    try:
        # Validate using the Pydantic model
        item_request = ItemCreateRequest(name=name)

        # Use the model to create the item
        Item.create(item_request.name)

        # Redirect to the items list page
        return RedirectResponse(url="/items", status_code=303)
    except ValidationError as e:
        # Return to the form with error message
        return templates.TemplateResponse(
            request,
            "item_create.html",
            {"message": "アイテム名は1文字以上15文字以下で入力してください", "error": True}
        )

@router.delete("/items/", response_class=HTMLResponse)
async def delete_item_html(request: Request, items: str):
    """
    Delete an item by name

    Args:
        request: The request object
        items: The name of the item to delete

    Returns:
        HTMLResponse: Redirect to the items list page
    """
    # Use the model to delete the item
    Item.delete(items)

    # Redirect to the items list page
    return RedirectResponse(url="/items", status_code=303)

@router.delete("/api/items/", response_model=ItemDeleteResponse)
async def delete_item_api(item_request: ItemDeleteRequest):
    """
    Delete an item via API

    Args:
        item_request: The request containing the item name to delete

    Returns:
        ItemDeleteResponse: A response indicating whether the item was deleted
    """
    # Use the model to delete the item
    success = Item.delete(item_request.name)

    # Return a response using the view model
    if success:
        return ItemDeleteResponse(message="Item deleted successfully", deleted=True)
    else:
        return ItemDeleteResponse(message="Item not found", deleted=False)
