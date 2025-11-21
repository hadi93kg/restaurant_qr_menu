# app/models/menu_item.py

class MenuItem:
    def __init__(self, name, description, price, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url

# نمونه داده‌ها
menu_items = [
    MenuItem(
        name="پیتزا مارگاریتا",
        description="پیتزا با پنیر موزارلا و گوجه تازه",
        price=120000,
        image_url="/static/uploads/pizza.jpg"
    ),
    MenuItem(
        name="برگر مخصوص",
        description="برگر با گوشت تازه و پنیر چدار",
        price=90000,
        image_url="/static/uploads/burger.jpg"
    ),
    MenuItem(
        name="سالاد فصل",
        description="سالاد تازه با سبزیجات متنوع",
        price=50000,
        image_url="/static/uploads/salad.jpg"
    )
]