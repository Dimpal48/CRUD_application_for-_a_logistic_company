from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Configuration(Base):
    """
    SQLAlchemy model representing a configuration entity stored in the database.
    """
    __tablename__ = "configurations" # Table name in the database
    id = Column(Integer, primary_key=True, index=True)# Primary key column for unique identifier
    country_code = Column(String, unique=True, index=True, nullable=False)# Column for country code with uniqueness constraint
    requirements = Column(JSON, nullable=False)# Column to store configuration requirements in JSON format
