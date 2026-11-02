from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    price: float = Field(..., gt=0)
    is_available: bool = True


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    is_available: Optional[bool] = None


class MenuItemResponse(MenuItemBase):
    id: int
    image_url: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
