from sqlalchemy.orm import Session
from models import Configuration
from schemas import ConfigurationCreate, ConfigurationUpdate

def create_configuration(db: Session, config: ConfigurationCreate):
    """
    Create a new configuration in the database.

    Parameters:
    - db: Session - SQLAlchemy session instance.
    - config: ConfigurationCreate - Pydantic schema defining the configuration data to create.

    Returns:
    - Configuration: Created Configuration object.
    """
    db_config = Configuration(country_code=config.country_code, requirements=config.requirements)
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_configuration(db: Session, country_code: str):
    """
    Retrieve a configuration from the database by country code.

    Parameters:
    - db: Session - SQLAlchemy session instance.
    - country_code: str - Country code to uniquely identify the configuration.

    Returns:
    - Configuration: Retrieved Configuration object, or None if not found.
    """
    return db.query(Configuration).filter(Configuration.country_code == country_code).first()

def update_configuration(db: Session, config: ConfigurationUpdate):
    """
    Update an existing configuration in the database.

    Parameters:
    - db: Session - SQLAlchemy session instance.
    - config: ConfigurationUpdate - Pydantic schema defining the updated configuration data.

    Returns:
    - Configuration: Updated Configuration object, or None if the configuration was not found.
    """
    db_config = db.query(Configuration).filter(Configuration.country_code == config.country_code).first()
    if db_config:
        db_config.requirements = config.requirements
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_configuration(db: Session, country_code: str):
    """
    Delete a configuration from the database by country code.

    Parameters:
    - db: Session - SQLAlchemy session instance.
    - country_code: str - Country code to uniquely identify the configuration.

    Returns:
    - Configuration: Deleted Configuration object, or None if the configuration was not found.
    """
    db_config = db.query(Configuration).filter(Configuration.country_code == country_code).first()
    if db_config:
        db.delete(db_config)
        db.commit()
    return db_config
