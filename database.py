from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings


# Retrieve the database URL from the settings configuration
DATABASE_URL = settings.DATABASE_URL
# Create an SQLAlchemy engine instance based on the database URL
engine = create_engine(DATABASE_URL)
# Create a session maker instance for SQLAlchemy sessions, configured with the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Declare a base class for declarative class definitions
Base = declarative_base()

def get_db():
    """
    Function to yield a SQLAlchemy session.
    Yields:
    - db: SessionLocal - A SQLAlchemy session instance.
    Notes:
    - The session is automatically closed after usage due to the 'finally' block.
    """
    db = SessionLocal()
    try:
        yield db # Provide the session to the caller
    finally:
        db.close() # Close the session when done to release resources
