
class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price = round(self.price + (self.price * (percent_change * 0.01)), 2)
            print(f'{self.name} price increased by {percent_change}%')
        else:
            self.price = round(self.price - (self.price * (percent_change * 0.01)), 2)
            print(f'{self.name} price increased by {percent_change}%')
            #print(self.price)
        return self
    
    def print_info(self):
        print(f'{self.name} is in the {self.category} department and costs, {self.price}')
        return self
