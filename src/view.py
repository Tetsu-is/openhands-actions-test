from pydantic import BaseModel, Field, field_validator
from typing import List

class ItemCreateRequest(BaseModel):
    """Request model for creating an item"""
    name: str = Field(..., description="アイテム名（1文字以上15文字以下）")

    @field_validator('name')
    @classmethod
    def validate_name_length(cls, v):
        if len(v) < 1 or len(v) > 15:
            raise ValueError("アイテム名は1文字以上15文字以下で入力してください")
        return v

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

class ItemDeleteRequest(BaseModel):
    """Request model for deleting an item"""
    name: str

class ItemDeleteResponse(BaseModel):
    """Response model for item deletion"""
    message: str
    deleted: bool
