# schemas.py

from pydantic import BaseModel

class ShortenURLRequest(BaseModel):
    original_url: str