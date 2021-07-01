class Store():
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return self
    
    def sell_product(self,id):
        del self.products[id]
        return self
    
    def inflation(self, percent_increase):
        for item in self.products:
            item.update_price(percent_increase,True)
    
    def clearance(self, category, percent_discount):
        for item in self.products:
            if(item.category == category):
                item.update_price(percent_discount,False)

    def inventory(self):
        if(self.products):
            print('Products in stock')
            for item in self.products:
                item.print_info()
        else:
            print("All sold out")