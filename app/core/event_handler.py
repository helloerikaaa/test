from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.services.models import DataModel


def _startup_model(app: FastAPI) -> None:
    model = DataModel()
    app.state.model = model


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("La applicación está creando el modelo")
        _startup_model(app)
    return startup

def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Se está destruyendo el modelo")
        _shutdown_model(app)
    return shutdown
