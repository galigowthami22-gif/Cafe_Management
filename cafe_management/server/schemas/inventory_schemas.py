from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class SupplierBase(BaseModel):
    name: str
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class SupplierCreate(SupplierBase):
    pass


class SupplierResponse(SupplierBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class IngredientBase(BaseModel):
    name: str
    unit: str
    minimum_stock_level: float = Field(default=10.0)
    supplier_id: Optional[int] = None


class IngredientCreate(IngredientBase):
    stock_level: float = Field(default=0.0)


class IngredientResponse(IngredientBase):
    id: int
    stock_level: float
    created_at: datetime

    class Config:
        from_attributes = True


class StockTransactionCreate(BaseModel):
    transaction_type: str = Field(..., description="IN or OUT")
    quantity: float = Field(..., gt=0)
    remarks: Optional[str] = None


class StockTransactionResponse(StockTransactionCreate):
    id: int
    ingredient_id: int
    created_at: datetime

    class Config:
        from_attributes = True
