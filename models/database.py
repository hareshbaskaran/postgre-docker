from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import Settings

# Database setup
Base = declarative_base()
settings = Settings.create_settings()
engine = create_engine(settings.DATABASE_URL)
PostgreSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
