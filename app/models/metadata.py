from pydantic import BaseModel


class MetadataResult(BaseModel):
    algo_name: str
    model_name: str
    metrics: dict
