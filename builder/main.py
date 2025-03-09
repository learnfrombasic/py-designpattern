class CoffeeBuilder:
    def __init__(self):
        self.coffee = {}
    
    def set_type(self, type):
        self.coffee["type"] = type
        return self
    
    def set_size(self, size):
        self.coffee["size"] = size
        return self
    
    def set_sugar(self, sugar):
        self.coffee["sugar"] = sugar
        return self
    
    def build(self):
        return self.coffee

if __name__ == "__main__":
    coffee = CoffeeBuilder().set_type("Espresso").set_size("Large").set_sugar("No sugar").build()
    print(coffee)   # {'type': 'Espresso', 'size': 'Large', 'sugar': 'No sugar'}