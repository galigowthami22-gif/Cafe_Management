from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    role: str
    salary: float = Field(default=0.0, ge=0)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    role: Optional[str] = None
    salary: Optional[float] = Field(None, ge=0)
    is_active: Optional[bool] = None


class EmployeeResponse(EmployeeBase):
    id: int
    hire_date: datetime
    is_active: bool

    class Config:
        from_attributes = True


class AttendanceBase(BaseModel):
    status: str = Field(..., description="Present, Absent, Half-Day, or Leave")


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):
    id: int
    employee_id: int
    date: datetime

    class Config:
        from_attributes = True
