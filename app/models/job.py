from sqlalchemy.orm import relationship
from app.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

created_at = Column(
    DateTime,
    default=datetime.utcnow
)

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String)
    role = Column(String)
    status = Column(String)
    location = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="jobs")
