# routes.py

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import ShortenedURL
from .schemas import ShortenURLRequest

router = APIRouter()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from app.utils import valid_url
from app.utils import generate_short_code

@router.post("/shorten")
def shorten_url(request: ShortenURLRequest, db: Session = Depends(get_db)):
    short_code = generate_short_code()
    url = valid_url(request.original_url)
    db_url = ShortenedURL(original_url=url, short_code=short_code)
    db.add(db_url)
    db.commit()
    return {"short_url": f"http://127.0.0.1:8000/{short_code}"}

@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url_entry = db.query(ShortenedURL).filter(ShortenedURL.short_code == short_code).first()
    if url_entry:
        return RedirectResponse(url_entry.original_url)
    raise HTTPException(status_code=404, detail="URL not found")

# @router.get("/{short_code}")
# def redirect_url(short_code: str, db: Session = Depends(get_db)):
#     url_entry = db.query(ShortenedURL).filter(ShortenedURL.short_code == short_code).first()
#     if url_entry:
#         return {"original_url": url_entry.original_url}
#     raise HTTPException(status_code=404, detail="URL not found")

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
