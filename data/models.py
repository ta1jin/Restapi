from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    costs = db.Column(db.Integer)

    def __str__(self):
        result = f'name:{self.name} costs:{self.costs}.'
        return result

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'costs': self.costs,
        }


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arcticle = db.Column(db.String(50))
    name = db.Column(db.String(255))
    weight = db.Column(db.Float)
    cost = db.Column(db.Integer)
    category = db.relationship('Category', backref='products', lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'arcticle': self.arcticle,
            'name': self.name,
            'weight': self.weight,
            'cost': self.cost,
            'category': str(self.category),
        }


class CategorySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "costs")
        model = Category

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "arcticle", "name", "weight", "cost", "category_id")
        model = Product

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)