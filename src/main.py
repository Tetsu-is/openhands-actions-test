from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controller import router

app = FastAPI(title="OpenHands Actions API")

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# コントローラーのルーターを登録
app.include_router(router)
