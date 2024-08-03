from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_TOKEN = "your_static_token_here"
api_key_header = APIKeyHeader(name="Authorization")

def authenticate(api_key: str = Security(api_key_header)):
    if api_key != API_TOKEN:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
