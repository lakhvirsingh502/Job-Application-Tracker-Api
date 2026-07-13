from pydantic import BaseModel

class Createapplication(BaseModel):
    job_title : str
    status : str
    location : str

class Update(BaseModel):
    job_title : str
    status : str
    location : str

