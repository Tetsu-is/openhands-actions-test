from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .controller import router

app = FastAPI(title="OpenHands Actions API")

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静的ファイルの設定（必要に応じて）
# static_dir = Path(__file__).parent / "static"
# if static_dir.exists():
#     app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# コントローラーからルーターをインクルード
app.include_router(router)

# ルートパスへのアクセスをアイテム一覧にリダイレクト
@app.get("/")
async def root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/items")
