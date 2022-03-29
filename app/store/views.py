from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from . import store

from .forms import CartItemForm

from .. import db
from ..models import Product, Cart, CartItem

@store.route('/')
def index():
    return render_template('store/index.html', products=Product.query.all())

@store.route('/order', methods=['POST'])
@login_required
def order():
    form = CartItemForm(request.form)

    if not form.validate():
        flash("Bad Input")
        return redirect(url_for('store.index'))
    
    product = Product.query.filter_by(id=form.product_id.data).first()
    
    if product.available_quantity < form.quantity.data:
        flash("Not available quantity for order")
        return redirect(url_for('store.index'))

    db.session.add(CartItem(
        cart_id=Cart.query.filter_by(user_id=current_user.id).first().id,
        product_id=form.product_id.data,
        quantity=form.quantity.data
    ))
    db.session.commit()

    return redirect(url_for('store.index'))