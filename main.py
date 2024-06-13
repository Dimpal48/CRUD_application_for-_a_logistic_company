from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db, engine
from models import Base
from schemas import ConfigurationCreate, Configuration, ConfigurationUpdate
import crud
import exceptions

app = FastAPI()

Base.metadata.create_all(bind=engine)

"""
    Endpoint to create a new configuration.

    Parameters:
    - config: ConfigurationCreate - Pydantic schema defining the new configuration data.
    - db: Session = Depends(get_db) - SQLAlchemy database session dependency.

    Returns:
    - Configuration: Created configuration data as per the schema.
    """

@app.post("/create_configuration", response_model=Configuration)
    
def create_configuration(config: ConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_configuration(db, config)

    """
    Endpoint to retrieve a configuration by country code.

    Parameters:
    - country_code: str - Country code to uniquely identify the configuration.
    - db: Session = Depends(get_db) - SQLAlchemy database session dependency.

    Returns:
    - Configuration: Retrieved configuration data as per the schema.

    Raises:
    - HTTPException 404: If the configuration with the specified country code is not found.
    """

@app.get("/get_configuration/{country_code}", response_model=Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code)
    if db_config is None:
        raise exceptions.ConfigurationNotFoundException(country_code)
    return db_config
    """
    Endpoint to update an existing configuration.

    Parameters:
    - config: ConfigurationUpdate - Pydantic schema defining the updated configuration data.
    - db: Session = Depends(get_db) - SQLAlchemy database session dependency.

    Returns:
    - Configuration: Updated configuration data as per the schema.

    Raises:
    - HTTPException 404: If the configuration to be updated is not found.
    """

@app.post("/update_configuration", response_model=Configuration)
def update_configuration(config: ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.update_configuration(db, config)
    if db_config is None:
        raise exceptions.ConfigurationNotFoundException(config.country_code)
    return db_config
    """
    Endpoint to delete a configuration by country code.

    Parameters:
    - country_code: str - Country code to uniquely identify the configuration.
    - db: Session = Depends(get_db) - SQLAlchemy database session dependency.

    Returns:
    - Configuration: Deleted configuration data as per the schema.

    Raises:
    - HTTPException 404: If the configuration to be deleted is not found.
    """

@app.delete("/delete_configuration/{country_code}", response_model=Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.delete_configuration(db, country_code)
    if db_config is None:
        raise exceptions.ConfigurationNotFoundException(country_code)
    return db_config
