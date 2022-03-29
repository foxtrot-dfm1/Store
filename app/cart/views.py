from flask import render_template
from flask_login import login_required, current_user

from . import cart

from ..models import Cart

@cart.route('/')
@login_required
def index():
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    return render_template('cart/index.html', items=cart.cart_items, total=cart.get_total())