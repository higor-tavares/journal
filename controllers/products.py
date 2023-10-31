from flask_restful import Resource
from models.product import Product

class Products(Resource):
    def get(self):
        return {
            'products': [
            Product('xiaomi',1000).get_product(),
            Product('Sansumg Galaxy Plus', 3000).get_product()
        ]}