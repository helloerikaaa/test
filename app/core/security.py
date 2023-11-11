import secrets
from typing import Optional

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from app.core import config


api_key = APIKeyHeader(name="token", auto_error=False)


def validate_request(header: Optional[str] = Security(api_key)) -> bool:
    if header is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No se declaró ninguna API KEY", headers={})

    if not secrets.compare_digest(header, str(config.API_KEY)):
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="API KEY incorrecto", headers={})

    return True
