from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from models.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, index=True)
    message = Column(String, nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
