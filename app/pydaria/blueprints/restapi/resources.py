from flask import jsonify, abort # jsonify é para transformar um dicionário em json
from flask_restful import Resource
from pydaria.models import Product




# RETORNA TODOS OS RECURSOS (i.e PRODUTOS)
class ProductResource(Resource):
    def get(self):
        productsall = Product.query.all() or abort(204)
        return jsonify(
            {"products": [productx.to_dict() for productx in productsall]}
        )
        


# RETORNA UM RECURSO ESPECÍFICO (i.e PRODUTO)
class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(
            404, "Product not found")
        return jsonify(product.to_dict())