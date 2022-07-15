from lzma import FORMAT_ALONE


from importlib import import_module
from dynaconf import FlaskDynaconf                          # Permite o uso de configurações dinâmicas


def load_extensions(app):
    for ext in app.config['EXTENSIONS']:
        module = import_module(ext)
        module.init_app(app)

def init_app(app):
    FlaskDynaconf(app)      # Carrega as config para o app