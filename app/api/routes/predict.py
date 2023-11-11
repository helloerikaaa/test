from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.core import security
from app.models.payload import Payload
from app.models.prediction import PredictionResult
from app.service.model import DataModel

router = APIRouter()

@router.post("/predict", response_model=PredictionResult, name="predict")
def post_predict(request: Request, authenticated: bool = Depends(security.validation_request), block_data: Payload = None) -> PredictionResult:
    model: DataModel = request.app.state.model
    prediction: PredictionResult = model.predict(block_data)

    return prediction
