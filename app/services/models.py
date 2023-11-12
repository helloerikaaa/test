from typing import List

import os
import json
import numpy as np
import pandas as pd
from loguru import logger

from app.models.metadata import MetadataResult
from app.models.prediction import PredictionResult
from app.services.load_model import load_model
from app.models.payload import Payload, payload_to_list


class MLModel(object):
    def __init__(self):
        self.model = load_model("modelo.pth")
        self.metadata = "metada.json"

    def _preprocess(self, payload: Payload) -> List:
        logger.info("Aquí se pre procesan los datos")
    
    def _post_process(self, prediction: np.ndarray) -> PredictionResult:
        logger.info("Aquí se hace el post procesamiento de los datos")


    def _predict(self, payload: Payload) -> np.ndarray:
        prediction_result = self.model.predict(payload)
        prediction_result = self.model.predict_proba(payload)

        return prediction_result
    
    def predict(self, payload: Payload)-> np.ndarray:
        self._preprocess(payload)
        self._post_process(payload)
        self._predict(payload)
