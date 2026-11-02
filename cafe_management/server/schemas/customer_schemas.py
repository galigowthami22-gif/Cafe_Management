from datetime import datetime

from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str = "admin"


class CustomerCreate(CustomerBase):
    password: str


class CustomerResponse(CustomerBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
