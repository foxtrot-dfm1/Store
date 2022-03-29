from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from . import cart

from .. import db
from ..models import Cart

@cart.route('/')
@login_required
def index():
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    return render_template('cart/index.html', items=cart.cart_items, total=cart.get_total())

@cart.route('/remove-item', methods=['POST'])
@login_required
def remove_item():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    item = cart.cart_items.filter_by(id=request.form.get('cart_item_id')).first()

    db.session.delete(item)
    db.session.commit()

    return redirect(url_for('cart.index'))
    
     
