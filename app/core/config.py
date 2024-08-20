from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Definición de la clase de configuración
class Settings(BaseSettings):
    """
    Clase que define la configuración de la aplicación.

    Attributes:
        mongodb_uri (str): URI de conexión a la base de datos MongoDB.
        mongodb_database (str): Nombre de la base de datos MongoDB.
    """
    mongodb_uri: str = os.getenv("MONGODB_URI")
    mongodb_database: str = os.getenv("MONGODB_DATABASE")

# Función decorada para cachear la instancia de la configuración
@lru_cache()
def get_settings():
    """
    Función que devuelve una instancia de la clase de configuración.

    Returns:
        Settings: Instancia de la clase de configuración.
    """
    return Settings()