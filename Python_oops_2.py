class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self,dis):
        # discount price
        self.new_price = (self.price - (dis*self.price)/100)
        return self.new_price
    
p1 = Laptop('acer', 'E5-575g', 44000)
p2 = Laptop('acer', 'predator', 58000)

print(p1.brand_name)
print(p1.apply_discount(25))
print(p2.apply_discount(10))
