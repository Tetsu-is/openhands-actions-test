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
@app.delete("/items/{item_name}")
async def delete_item(item_name: str):
    if item_name in data_store:
        data_store.remove(item_name)
        return {"message": "Item deleted", "item": item_name}
    return {"message": "Item not found", "item": item_name}
