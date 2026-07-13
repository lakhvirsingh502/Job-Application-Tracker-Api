from fastapi import Depends, HTTPException, FastAPI, APIRouter, Query
from app.database import get_db
from app.models.user import User
from app.models.application import application
from sqlalchemy.orm import Session
from app.schemas.user import CreateUser, CreateLogin
from app.schemas.application import Createapplication, Update
from app.dependencies.current_user import get_user
from app.dependencies.get_role import get_role

router = APIRouter()
@router.get("/user/list/applications")
def show(category:str = None,search:str=None,sort="asc",skip:int=Query(0,ge=0),limit:int=Query(10, ge=1,le=10),
         user = Depends(get_user),db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    query = db.query(application).filter(application.user_id == user.id)
    if category:
        query = query.filter(application.category == category)
    if search:
        query = query.filter(application.status.ilike(f"%{search}%"))
    if sort == "desc":
        query = query.order_by(application.job_title.desc())
    else:
        query = query.order_by(application.job_title.asc())
    return query.offset(skip).limit(limit).all()
@router.put("/user/application/update/{id}")
def create_update(id :int,st:Update, user = Depends(get_user), db:Session = Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "User not found."
        )
    appl = db.query(application).filter(application.user_id == user.id,application.id == id).first()
    if appl is None:
        raise HTTPException(
            status_code=404,
            detail = "application not found."
        )
    appl.job_title = st.job_title
    appl.status = st.status
    appl.location = st.location
    db.commit()
    db.refresh(appl)
    return {
        "message" : "Update Successfully."
    }
@router.delete("/user/application/delete/{id}")
def deletion(id:int,user = Depends(get_user), db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
        status_code=404,
        detail="User not found."
        )
    appl = db.query(application).filter(application.user_id==user.id, application.id == id).first()
    if appl is None:
        raise HTTPException(
            status_code = 404,
            detail = "application not found."
        )
    db.delete(appl)
    db.commit()
    return{
        "message" : "Deleted successfully."
    }


        

    


