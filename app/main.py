from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Database setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Define Message model
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    message = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Pydantic models
class MessageCreate(BaseModel):
    username: str
    message: str

@app.post("/messages/")
def create_message(message: MessageCreate):
    db = SessionLocal()
    new_message = Message(username=message.username, message=message.message)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    db.close()
    return {"message": "Message stored successfully"}

@app.get("/messages/")
def get_messages():
    db = SessionLocal()
    messages = db.query(Message).all()
    db.close()
    return messages
