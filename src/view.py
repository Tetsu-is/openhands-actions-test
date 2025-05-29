from pydantic import BaseModel

class ItemCreateRequest(BaseModel):
    name: str

class ItemCreateResponse(BaseModel):
    message: str
    item: str

class ItemReadResponse(BaseModel):
    items: list
