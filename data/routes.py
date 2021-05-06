from flask_marshmallow import Marshmallow
from flask_jwt_extended import jwt_required
from data.models import *
from flask_restful import Resource
from flask import request

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return [a.to_dict() for a in products]

    def post(self):
        new_product = Product(
            arcticle=request.json['arcticle'],
            name=request.json['name'],
            weight=request.json['weight'],
            cost=request.json['cost'],
            category_id=request.json['cat_id']
        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product)

class CategoryListResource(Resource):
    def get(self):
        categories = Category.query.all()
        return [a.to_dict() for a in categories]

    def post(self):
        new_category = Category(
            name=request.json['name'],
            costs=request.json['costs']
        )
        db.session.add(new_category)
        db.session.commit()
        return category_schema.dump(new_category)

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)

    def patch(self, product_id):
        product = Product.query.get_or_404(product_id)

        if 'arcticle' in request.json:
            product.arcticle = request.json['arcticle']
        if 'name' in request.json:
            product.name = request.json['name']
        if 'weight' in request.json:
            product.weight = request.json['weight']
        if 'cost' in request.json:
            product.cost = request.json['cost']
        if 'cat_id' in request.json:
            product.category_id = request.json['cat_id']

        db.session.commit()
        return product_schema.dump(product)

    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return '', 204