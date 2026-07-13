from jose import jwt
import os
from dotenv import load_dotenv
load_dotenv()
Secret_key = os.getenv("SECRET_KEY")
def create_token(id : int):
    data = {
        "user_id" : id
    }
    return jwt.encode(
        data,
        Secret_key,
        algorithm="HS256"
    )

def access_token(token):
    return jwt.decode(
        token,
        Secret_key,
        algorithms="HS256"
    )
