# models.py

from sqlalchemy import Column, Integer, String
from .database import Base

class ShortenedURL(Base):
    __tablename__ = "shortened_urls"
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True)
