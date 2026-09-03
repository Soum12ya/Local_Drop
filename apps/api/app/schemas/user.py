from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    phone: str
    name: str | None = None
    email: str | None = None


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    avatar_url: str | None = None


class UserResponse(BaseModel):
    id: int
    phone: str
    name: str | None
    email: str | None
    avatar_url: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )