from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

# -------------------------
# Login
# -------------------------


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# -------------------------
# Orders
# -------------------------


class OrderCreate(BaseModel):
    customer: str = Field(..., min_length=3, max_length=100)
    product: str = Field(..., min_length=2, max_length=100)
    quantity: int = Field(..., gt=0)


class OrderUpdate(BaseModel):
    customer: str = Field(..., min_length=3, max_length=100)
    product: str = Field(..., min_length=2, max_length=100)
    quantity: int = Field(..., gt=0)
    status: Literal["Pending", "Processing", "Completed", "Cancelled"]


class OrderResponse(BaseModel):
    id: int
    customer: str
    product: str
    quantity: int
    status: str

    model_config = ConfigDict(from_attributes=True)
