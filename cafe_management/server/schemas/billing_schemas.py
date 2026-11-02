from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class InvoiceBase(BaseModel):
    order_id: int
    subtotal: float
    tax_amount: float
    total_amount: float
    payment_method: Optional[str] = None
    payment_status: str


class InvoiceResponse(InvoiceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PaymentRequest(BaseModel):
    payment_method: str = Field(..., description="Cash, UPI, or Card")
