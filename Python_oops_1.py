class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"

product_1 = Laptop('acer', 'E5-575g', 44000)
product_2 = Laptop('acer', 'predator', 64000)

print(product_1.brand_name)
print(product_2.price)

# way to call the instance (both are same)
print(product_2.full_name())   # -------->  mainly used to call 
print(Laptop.full_name(product_2))

