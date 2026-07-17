import os
import pytest
from fastapi import Depends
from dotenv import load_dotenv
from app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base

load_dotenv()

Database_url = os.getenv("Database_Url")
engine = create_engine(Database_url)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def test_get_db():
    db = TestingSessionLocal()
    try :
        yield db
    finally:
        db.close()
app.dependency_overrides[get_db] = test_get_db

@pytest.fixture
def client():
    Base.metadata.create_all(bind = engine)
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def user_register(client):
    response = client.post("/register",json={
        "name":"Vasudev",
        "password" : "123456",
        "role" : "user"
    })
    return response

@pytest.fixture
def user_header(client):
     client.post("/register",json={
        "name":"Vasudev",
        "password" : "123456",
        "role" : "user"})

     response = client.post("/login", json={
        "name":"Vasudev",
        "password": "123456"
    })
     header = response.json()["Token"]
     return {
         "Authorization" : f"Bearer {header}"
     }
@pytest.fixture
def user_create_application(client,user_header):
    response = client.post("/user/application",json={
               "job_title" : "QC",
                "location" : "Bramptom",
                 "status":"applied." },headers=user_header)
    
@pytest.fixture
def admin_user(client):
    response = client.post("/register",json={
        "name":"Krishna",
        "password":"123456",
        "role":"admin"
    })

@pytest.fixture
def admin_header(client,admin_user):
    response = client.post("/login",json={
        "name" : "Krishna",
        "password":"123456"
    })
    token = response.json()["Token"]
    return {
        "Authorization" : f"Bearer {token}"
    }
@pytest.fixture
def admin_create_application(client,admin_header):
    response = client.post("/user/application", json={
        "job_title" : "Python Developer",
        "location" : "Brampton",
        "status" : "Selected."
    })

    
    
