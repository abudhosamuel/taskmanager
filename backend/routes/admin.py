# backend/routes/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas
from backend.database import get_db

from backend.utils.auth_utils import get_current_user


router = APIRouter()


# Utility: require current user to be admin
def require_admin(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user


# Admin: assign task to any user
@router.post("/admin/assign-task", response_model=schemas.TaskOut)
def assign_task_to_user(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: models.User = Depends(require_admin)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
        user_id=task.user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Task assigned successfully", "task": new_task}
