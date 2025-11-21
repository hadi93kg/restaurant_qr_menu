# app/main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import qrcode
import os

from app.models.menu_item import menu_items  # وارد کردن داده‌ها

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request: Request):
    qr_path = "app/static/uploads/menu_qr.png"
    url = "https://restaurant-qr-menu-irzq.onrender.com/"  # لینک رندر
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/menu")
def show_menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request, "menu_items": menu_items})
