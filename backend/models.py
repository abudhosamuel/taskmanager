# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Boolean
from sqlalchemy.orm import relationship
from backend.database import Base
import enum

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)  # updated field
    is_admin = Column(Boolean, default=False)

    tasks = relationship("Task", back_populates="assignee")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    deadline = Column(DateTime)

    user_id = Column(Integer, ForeignKey("users.id"))
    assignee = relationship("User", back_populates="tasks")
