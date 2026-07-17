from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.models.user import User
from .current_user import get_user
from sqlalchemy.orm import Session
from app.database import get_db


def get_role(user = Depends(get_user), db : Session = Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "User not found."
        )
    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail = "You are not authorized to do this action."
        )
    return user
