from fastapi import FastAPI
from routes import message
from models.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI app setup
app = FastAPI()

# Routers
app.include_router(message.router, prefix="/messages", tags=["Messages"])
