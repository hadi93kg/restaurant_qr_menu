import qrcode
import os

def generate_qr(data):
    folder = "app/static/qrcodes"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "menu_qr.png")

    img = qrcode.make(data)
    img.save(file_path)

    return file_path