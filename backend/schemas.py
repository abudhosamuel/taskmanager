from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

# ------------------------------------
# ENUMS
# ------------------------------------
class TaskStatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

# ------------------------------------
# USER SCHEMAS
# ------------------------------------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    is_admin: bool = False  # Optional admin flag

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_admin: Optional[bool] = None

class UserOut(UserBase):
    id: int
    is_admin: bool = False

    class Config:
        from_attributes = True

# ------------------------------------
# TASK SCHEMAS
# ------------------------------------
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    user_id: int
    status: TaskStatusEnum = TaskStatusEnum.pending

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatusEnum] = None

class TaskOut(TaskBase):
    id: int
    status: TaskStatusEnum
    user_id: int

    class Config:
        from_attributes = True

# ------------------------------------
# AUTH TOKEN
# ------------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str
