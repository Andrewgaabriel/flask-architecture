import click
from pydaria.extensions.database import db
#from pydaria.extensions.auth import create_user
from pydaria.models import Product



def create_db():
    """Cria o banco de dados"""
    db.create_all()



def drop_db():
    """Limpa o banco de dados"""
    db.drop_all()
    
    
def populate_db():
    data = [
        Product(id=1, name="Ciabatta", price=15, description="Ciabatta de origem italiana"),
        Product(id=2, name="Pizza", price=20, description="Pizza de origem italiana"),
        Product(id=3, name="Pão de Queijo Recheado", price=10, description="Pão de queijo cm Nutella"),
    ]
    
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Product.query.all()

def init_app(app):
    # ADICIONA MULTIPLOS COMANDOS
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
        
    # # ADICIONA UM COMANDO
    # @app.cli.command()
    # @click.option('--username', '-u')
    # @click.option('--password', '-p')
    # def add_user(username, password):
    #     """Adiciona um novo usuário no banco de dados"""
    #     return create_user(username, password)