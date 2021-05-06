import os
from flask import Flask, request, render_template
from data.models import db
from data.routes import *
from flask_restful import Api, Resource

if os.path.exists('test.db'):
    os.remove('test.db')

if __name__ == '__main__':
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "abc"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)

    api.add_resource(ProductResource, '/product/<int:product_id>')
    api.add_resource(ProductListResource, '/products')
    api.add_resource(CategoryListResource, '/categories')


    app.run(debug=True)