from pydantic import BaseModel

class CreateUser(BaseModel):
    name : str
    password : str
    role : str

class CreateLogin(BaseModel):
    name : str
    password : str

class UserResponse(BaseModel):
    name : str

    class config:
        from_attributes = True


    
    