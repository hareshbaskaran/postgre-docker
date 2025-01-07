from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.connection import get_db
from models.message import Message
from schemas.message import MessageCreate, MessageResponse

router = APIRouter()


@router.post("/", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    curr_msg = Message(username=message.username, message=message.message)
    db.add(curr_msg)
    db.commit()
    db.refresh(curr_msg)
    return curr_msg


@router.get("/", response_model=list[MessageResponse])
def get_messages(db: Session = Depends(get_db)):
    msgs = db.query(Message).all()
    return msgs
