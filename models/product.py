class Product(): 
    quantity = 0;
    def __init__(self, description, price):
        self.description = description
        self.price = price
    
    def get_product(self):
        return {'product':self.description, 'price':self.price}
    
    @classmethod
    def remove_product(cls):
        cls.quantity = cls.quantity - 1
    @classmethod
    def add_product(cls):
        cls.quantity = cls.quantity + 1

    @staticmethod
    def say_anything():
        print("I am a product!")