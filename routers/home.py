from fastapi import APIRouter

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import fastapi
import streamlit


router = APIRouter(
    prefix="/home",
    tags=['Home']
)

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Simple home page template using jinja2.
    Args:
        request (Request): Request that's returned.
    Returns:
        template: Returns template and a simple dict.
    """
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

