from fastapi import Depends, HTTPException, FastAPI, APIRouter
from app.database import get_db
from app.models.user import User
from app.models.application import application
from sqlalchemy.orm import Session
from app.schemas.user import CreateUser, CreateLogin
from app.schemas.application import Createapplication
from app.auth.password import create_hash_password, verify_password
from app.auth.jwt_handler import access_token, create_token


router = APIRouter()

@router.post("/register")
def create_user(st:CreateUser, db:Session=Depends(get_db)):
    existing_user = db.query(User).filter(User.name == st.name).first()
   
    if existing_user :
        raise HTTPException(
            status_code=400,
            detail = "User already exist."
        )
    hashed_password = create_hash_password(st.password)
    new_user = User(
        name = st.name,
        password = hashed_password,
        role = st.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message" : "User created successfully."
    }

@router.post("/login")
def create_login(st:CreateLogin, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.name == st.name).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "User not found."
        )
    password = verify_password(st.password, user.password)
    if not password:
        raise HTTPException(
            status_code = 403,
            detail="Invalid credentials."
        )
    token = create_token(user.id)

    return {
        "Token" : token
    }



