from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    role = Column(String, default="user")
    applications = relationship("application", back_populates="user")
    

