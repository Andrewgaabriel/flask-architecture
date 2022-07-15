from flask_admin import Admin                               # Interface administrativa
from flask_admin.base import AdminIndexView                 # Interface administrativa
from flask_admin.contrib import sqla                        # Interface administrativa
from flask_simplelogin import login_required   # Para o uso do login


from pydaria.extensions.database import db               # Para o uso do banco de dados
from pydaria.models import Product





# PROTEÇÃO ADMIN:
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view) # solicita o login
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view) # solicita o login
admin = Admin()




def init_app(app):
    admin.name=app.config.TITLE
    admin.template_mode="bootstrap3"
    admin.init_app(app)
    # ADICIONA A VIEW DO ADMIN COM O BANCO DE DADOS
    admin.add_view(sqla.ModelView(Product, db.session))