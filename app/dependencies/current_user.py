from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.models.user import User
from app.database import get_db
from app.auth.jwt_handler import access_token
security = HTTPBearer()
def get_user(credentials = Depends(security), db = Depends(get_db)):
    token = credentials.credentials
    data = access_token(token)
    user = db.query(User).filter(User.id == data["user_id"]).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "User not found."
        )
    return user