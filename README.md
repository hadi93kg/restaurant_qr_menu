# Restaurant QR Menu

## English Version

### Project Overview
This is a simple QR code-based restaurant menu project built using FastAPI, Jinja2, and qrcode.  
When the QR code is scanned, it directs the user to the restaurant menu page displaying food items with images and descriptions.  

### Features
- Generate QR code automatically pointing to the live menu.
- Display food items with images.
- Mobile-friendly menu page.

### Tech Stack
- Python 3.10+
- FastAPI
- Jinja2
- qrcode[pil]
- HTML/CSS

### Installation
1. Clone the repository:
`bash
git clone <your-repo-link>
cd <project-folder>

2. Create a virtual environment and activate it:



python -m venv rest
rest\Scripts\activate   # Windows
source rest/bin/activate # Linux/Mac

3. Install dependencies:



pip install -r requirements.txt

4. Run the project locally:



uvicorn app.main:app --reload

Live Demo

Live project deployed on Render: https://restaurant-qr-menu-irzq.onrender.com



---
