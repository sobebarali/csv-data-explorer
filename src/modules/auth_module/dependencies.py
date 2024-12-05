from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from src.config import SEGWISE_API_KEY

API_KEY_NAME = "x-api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == SEGWISE_API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
