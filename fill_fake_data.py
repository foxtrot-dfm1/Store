from app.models import Product
from app import db, create_app

with create_app().app_context():
    for i in range(0, 10):
            db.session.add(Product(name="name" + str(i), price=i, description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.", available_quantity=i))
            db.session.commit()