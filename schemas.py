from pydantic import BaseModel
from typing import Dict, Any

class ConfigurationCreate(BaseModel):
    """
    Model for creating a new configuration. 
    It includes the country code and a dictionary of requirements.
    """
    country_code: str 
    requirements: Dict[str, Any] # Dictionary of requirements specific to the configuration

class ConfigurationUpdate(BaseModel):
    """
    Model for updating an existing configuration. 
    It includes the country code and a dictionary of updated requirements.
    """
    country_code: str
    requirements: Dict[str, Any]

class Configuration(BaseModel):
    """
    Model representing a configuration in the system. 
    It includes an ID, country code, and a dictionary of requirements.
    """
    id: int
    country_code: str
    requirements: Dict[str, Any]

    class Config:
        orm_mode = True # Enable ORM mode to support mapping of database objects
