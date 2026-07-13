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

@router.post("/user/application")
def create_application(st:Createapplication, db:Session=Depends(get_db), user = Depends(get_user)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "User not found."
        )
    new_application = application(
        job_title = st.job_title,
        location = st.location,
        status = st.status
    )
    user.applications.append(new_application)
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return {
        "message" : "application created successfully."
    }



        

    


