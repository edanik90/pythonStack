from products import Product
from store import Store

new_store = Store('Electronics')
iphone = Product('Iphone 11', 900, 'smartphones')
chromebook = Product('Chromebook', 450, 'laptops')
asus_rog = Product('Asus ROG', 1400, 'laptops')
new_store.add_product(iphone)
new_store.add_product(chromebook)
new_store.add_product(asus_rog)
iphone.print_info()
new_store.show_products()
new_store.inflation(0.02)
new_store.show_products()
new_store.set_clearance('laptops', 0.03)
new_store.show_products()
new_store.sell_product(1)
new_store.show_products()