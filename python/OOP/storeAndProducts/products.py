class Product():

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __repr__(self):
        return self.name + self.category + str(self.price)

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f'Product name: ' + self.name + '\nCategory: ' + self.category + '\nPrice: $' + str(self.price))
        return self