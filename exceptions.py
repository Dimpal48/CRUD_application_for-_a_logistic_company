from fastapi import HTTPException

class ConfigurationNotFoundException(HTTPException):
    """
    Custom HTTPException subclass for handling cases where a configuration for a specific
    country code is not found.

    Attributes:
    - country_code: str - The country code for which the configuration was not found.
    """
    def __init__(self, country_code: str):
        """
        Initialize the exception with a 404 status code and a detailed message.

        Parameters:
        - country_code: str - The country code that was not found in the configuration.
        """
        super().__init__(status_code=404, detail=f"Configuration for country code '{country_code}' not found.")
