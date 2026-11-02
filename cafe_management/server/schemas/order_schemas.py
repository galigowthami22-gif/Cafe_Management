from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int = Field(default=1, gt=0)


class OrderItemResponse(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    order_type: str = Field(..., description="dine-in, takeaway, or online")
    table_number: Optional[int] = None
    status: Optional[str] = "Pending"


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderResponse(OrderBase):
    id: int
    customer_id: int
    total_amount: float
    created_at: datetime
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True


class LoyaltyPointBase(BaseModel):
    points: int
    description: Optional[str] = None


class LoyaltyPointCreate(LoyaltyPointBase):
    pass


class LoyaltyPointResponse(LoyaltyPointBase):
    id: int
    customer_id: int
    created_at: datetime

    class Config:
        from_attributes = True
