from pydantic import BaseModel
from typing import List

class ItemCreateRequest(BaseModel):
    """Request model for creating an item"""
    name: str

class ItemCreateResponse(BaseModel):
    """Response model for item creation"""
    message: str
    item: str

class ItemReadRequest(BaseModel):
    """Request model for reading items (empty as no parameters needed)"""
    pass

class ItemReadResponse(BaseModel):
    """Response model for reading items"""
    items: List[str]
