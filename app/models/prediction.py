from pydantic import BaseModel

from app.models.metada import MetadataResult


class PredictionResult(BaseModel):
    success: bool
    probability: float
    metadata: MetadataResult
    message: str
