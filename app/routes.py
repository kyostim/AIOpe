from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.actions import suorita_toiminto

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def etusivu(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tulos": ""
        }
    )


@router.post("/suorita", response_class=HTMLResponse)
async def suorita(request: Request):

    tulos = suorita_toiminto()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tulos": tulos
        }
    )