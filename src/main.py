from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from view import ItemCreateRequest, ItemCreateResponse, ItemReadResponse
from controller import create_item_controller, read_items_controller

app = FastAPI(title="OpenHands Actions API")

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/items/", response_model=ItemCreateResponse)
async def create_item(request: ItemCreateRequest) -> ItemCreateResponse:
    """アイテム作成エンドポイント"""
    return create_item_controller(request)


@app.get("/items/", response_model=ItemReadResponse)
async def read_items() -> ItemReadResponse:
    """アイテム読み込みエンドポイント"""
    return read_items_controller()
