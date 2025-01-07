from models.database import PostgreSession

## Manages db session lifecycle efficiently

def get_db():
    db = PostgreSession() ## Create a db session
    try:
        yield db ## Injects db session into router (only when needed)
    finally:
        db.close() ## Cleans up / Closes the db session
