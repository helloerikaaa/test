import pickle
from loguru import logger


def load_model(path: str):
    try:
        model = pickle.load(open(path, "rb"))
        logger.info("El modelo se cargó correctamente")
    except Exception as e:
        logger.error(f"Error al cargar el model {e}")
    
    return model
