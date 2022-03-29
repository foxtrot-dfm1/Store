from flask_login import UserMixin

from . import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(512))
    available_quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Numeric(precision=2, scale=2))


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cart_items = db.relationship("CartItem", backref="cart_items")

    def get_total(self):
        """Count total cart price"""
        total = 0
        
        for item in self.cart_items:
            total += (item.product.price * item.quantity)
        
        return total

class CartItem(db.Model):
    __tablename__ = 'cart_item'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product = db.relationship("Cart", backref=db.backref("cart", uselist=False))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship("Product", backref=db.backref("product", uselist=False))
    quantity = db.Column(db.Integer)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(512))