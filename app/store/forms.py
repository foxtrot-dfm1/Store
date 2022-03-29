from wtforms import Form, IntegerField, validators


class CartItemForm(Form):
    product_id = IntegerField('product_id')
    quantity = IntegerField('quantity')