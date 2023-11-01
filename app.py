from flask import Flask
from flask_restful import Api
from controllers.products import Products, ProductController

app = Flask(__name__)
api = Api(app)

api.add_resource(Products, '/products')
api.add_resource(ProductController, '/products/<string:product_name>')

if __name__ == '__main__':
    app.run(debug=True)