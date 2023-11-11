from starlette.config import Config
from starlette.datastrcutures import Secret

config = Config(".env")

APP_VERSION: str = config("APP_VERSION")
APP_NAME: str = config("APP_NAME")
APP_PREFIX: str = "/api"

# Configuración de las peticiones
API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
