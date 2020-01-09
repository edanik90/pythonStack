from products import Product

class Store():
    def __init__(self, name, list_of_products = []):
        self.name = name
        self.list_of_products = list_of_products
    
    def __repr__(self):
        return (f"List of products: " + str(self.list_of_products))

    def add_product(self, new_product):
        # product = Product(new_product, price, category)
        self.list_of_products.append(new_product)
    
    def sell_product(self, product_id):
        product_id = self.list_of_products[product_id]
        self.list_of_products.remove(product_id)


new_store = Store('Foods')
apple = Product('Apple', 1, 'fruits')
pear = Product('Pear', 2, 'fruits')
new_store.add_product(apple)
new_store.add_product(pear)
# new_store.sell_product(1)
# print(new_store)
apple.print_info()