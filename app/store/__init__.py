from flask import Blueprint


store = Blueprint('store', __name__, 
                  template_folder='templates', 
                  url_prefix='/store'
                 )

from . import views