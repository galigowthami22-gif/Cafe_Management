from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FeedbackBase(BaseModel):
    customer_id: int
    order_id: Optional[int] = None
    rating: int = Field(..., ge=1, le=5)
    comments: Optional[str] = None
    is_complaint: bool = False


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(BaseModel):
    status: str = Field(..., description="Pending, Investigating, Resolved")
    resolution_notes: str


class FeedbackResponse(FeedbackBase):
    id: int
    status: str
    resolution_notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
