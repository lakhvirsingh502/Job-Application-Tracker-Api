from fastapi import Depends, HTTPException, FastAPI, APIRouter, Query
from app.database import get_db
from app.models.user import User
from app.models.application import application
from sqlalchemy.orm import Session
from app.schemas.user import CreateUser, CreateLogin, UserResponse
from app.schemas.application import Createapplication, Update
from app.dependencies.current_user import get_user
from app.dependencies.get_role import get_role

router = APIRouter()
@router.get("/admin/applications" )
def show(user = Depends(get_role), db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    return db.query(application).all()
@router.get("/admin/users", response_model=list[UserResponse])
def show(user = Depends(get_role), db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    return db.query(User).all()

@router.delete("/admin/application/delete/{id}")
def deletion(id:int,user = Depends(get_role), db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    appl = db.query(application).filter(application.id == id).first()
    if appl is None:
        raise HTTPException(
            status_code=404,
            detail = "application not found."
        )
    db.delete(appl)
    db.commit()
    return{
        "message" : "Deleted Successfully."
    }
    
@router.delete("/admin/user/delete/{id}")
def deletion(id:int,user = Depends(get_role), db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "application not found."
        )
    db.delete(user)
    db.commit()
    return{
        "message" : "Deleted Successfully."
    }