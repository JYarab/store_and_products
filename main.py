from products import Product
from stores import Store


store1 = Store("The Store")

baseball = Product("baseball", 2.99, "Sporting Goods")
football = Product("football", 7.99, "Sporting Goods")
grill = Product("grill", 99.99, "Outdoor")

#store1.inventory()
#store1.add_product(baseball).add_product(football).add_product(grill)
#store1.inventory()
#store1.sell_product(2)
#store1.clearance("Sporting Goods", 50)
#store1.inventory()
grill.print_info()
grill.update_price(50,False)
grill.print_info()