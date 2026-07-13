from fastapi import FastAPI
from app.routers import admin,application,auth,user
from app.database import engine, Base
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Job Tracker Api",
              version="1.0.0")

app.include_router(admin.router)
app.include_router(application.router)
app.include_router(auth.router)
app.include_router(user.router)