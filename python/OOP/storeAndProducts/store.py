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
    
    def sell_product(self, id):
        product_id = self.list_of_products[id]
        self.list_of_products.remove(product_id)
    
    def inflation(self, percent_increase):
        for item in self.list_of_products:
            item.update_price(percent_increase, True)
    
    def set_clearance(self, category, percent_discount):
        for item in self.list_of_products:
            if category == item.category:
                item.update_price(percent_discount, False)
    
    def show_products(self):
        for item in self.list_of_products:
            print(f'Product name: ' + item.name + ' || Category: ' + item.category + ' || Price: $' + str(item.price))
        print('*'*80)
        return self