from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String)
    location = Column(String)
    status = Column(String)
    applied_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="applications")
    