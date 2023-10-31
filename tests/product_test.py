import sys

# import modules from root
sys.path.insert(0,'./')

from models.product import Product

# Test objects
p1 = Product('AirPods', 1400)
p2 = Product('Iphone 13 Pro MAX', 4838)
print(p1.get_product())
print(p2.get_product())
# Test static methods
Product.say_anything()
# Test class methods
Product.add_product()
Product.add_product()
print(Product.quantity)