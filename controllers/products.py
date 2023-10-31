from flask import Flask
from flask_restful import Resource, Api
import sys

sys.path.insert(0,'./')
from models.product import Product

app = Flask(__name__)
api = Api(app)

class Products(Resource):
    def get(self):
        return {
            'products': [
                Product('xiaomi',1000).get_product()
        ]}

api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.run(debug=True)