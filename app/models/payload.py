from typing import List
from pydantic import BaseModel


class Payload(BaseModel):
    img1: str
    img2: str


def payload_to_list(payload: Payload) -> List:
    payload_list = [
        payload.img1,
        payload.img2
    ]

    return payload_list
