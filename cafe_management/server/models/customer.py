from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from server.config.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String(50), nullable=False, default="admin")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    otp_code = Column(String(10), nullable=True)
    otp_expiry = Column(DateTime(timezone=True), nullable=True)

    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")
    loyalty_points = relationship("LoyaltyPoint", back_populates="customer", cascade="all, delete-orphan")
    feedback = relationship("Feedback", back_populates="customer", cascade="all, delete-orphan")
