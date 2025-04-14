from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="OpenHands Actions API")

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# アイテムのモデルを定義
class Item(BaseModel):
    name: str

data_store = []

@app.post("/items/")
async def create_item(item: Item):
    data_store.append(item.name)
    return {"message": "Item added", "item": item.name}

@app.get("/items/")
async def read_items():
    return {"items": data_store}
