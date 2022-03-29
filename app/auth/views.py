from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db
from ..models import User, Cart

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Bad login data')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=True)

    return redirect(url_for('index'))

@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    if User.query.filter_by(email=email).first():
        flash('Email already exists')
        return redirect(url_for('auth.signup'))
    
    user = User(
        email=email,
        name=name,
        password=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()
    db.session.add(Cart(user_id=user.id))
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('index'))