from datetime import datetime

from pydantic import BaseModel, Field


class TableBase(BaseModel):
    table_number: str
    capacity: int = Field(..., gt=0)


class TableCreate(TableBase):
    pass


class TableResponse(TableBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class ReservationBase(BaseModel):
    customer_id: int
    table_id: int
    reservation_time: datetime
    number_of_guests: int = Field(..., gt=0)


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(BaseModel):
    status: str = Field(..., description="Pending, Approved, Cancelled, Completed")


class ReservationResponse(ReservationBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
