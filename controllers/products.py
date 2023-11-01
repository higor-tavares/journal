from flask_restful import Resource, reqparse
from models.product import Product

products = []

class Products(Resource):
    def get(self):
        return {'products': products}

class ProductController(Resource):
    def get(self, product_name):
        for product in products:
            if product['product'] == product_name:
                return product
            return {'message':'Product not found'}, 404
        
    def post(self, product_name):
        args = reqparse.RequestParser()
        args.add_argument('price')
        data = args.parse_args()
        new_product = Product(description=product_name, price=data['price']).get_product()
        products.append(new_product)
        return new_product, 201
    
    def delete(self, product_name):
        pass