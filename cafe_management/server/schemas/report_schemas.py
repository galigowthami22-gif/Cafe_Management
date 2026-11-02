from pydantic import BaseModel


class SalesSummary(BaseModel):
    period: str
    total_orders: int
    total_revenue: float
    average_order_value: float


class TopItem(BaseModel):
    menu_item_id: int
    name: str
    total_quantity_sold: int


class RevenueAnalytics(BaseModel):
    payment_method: str
    total_revenue: float


class InventoryConsumption(BaseModel):
    ingredient_id: int
    name: str
    total_consumed: float
    unit: str


class CustomerActivity(BaseModel):
    customer_id: int
    full_name: str
    total_orders: int
    total_spent: float
