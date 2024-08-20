import motor.motor_asyncio
from .config import get_settings

# Obtener la configuración de la aplicación
settings = get_settings()

# Crear una conexión asíncrona a la base de datos MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
db = client[settings.mongodb_database]