from flask_sqlalchemy import SQLAlchemy                     # Para o uso de banco de dados


db = SQLAlchemy()                                        # Carrega o banco de dados

def init_app(app):
    db.init_app(app)


    