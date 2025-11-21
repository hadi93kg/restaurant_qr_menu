from flask import Blueprint, render_template, send_file
from app.services.qr_service import generate_qr
from app.models.menu_item import menu_items

menu_bp = Blueprint("menu", name)

@menu_bp.route("/")
def index():
    return render_template("index.html")

@menu_bp.route("/menu")
def menu():
    return render_template("menu.html", items=menu_items)

@menu_bp.route("/qrcode")
def qrcode():
    img_path = generate_qr("https://your-render-url.onrender.com/menu")
    return send_file(img_path, mimetype='image/png')