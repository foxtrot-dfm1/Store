from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from .config import Configuration


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Configuration)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import User

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth
    app.register_blueprint(auth)

    from .store import store
    app.register_blueprint(store)

    from .cart import cart
    app.register_blueprint(cart)

    @app.route('/')
    def index():
        return redirect(url_for('store.index'))
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', e=e), 404

    return app

