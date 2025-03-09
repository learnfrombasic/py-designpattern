import copy

class CoffeeOrder:
    def __init__(self, type, size, sugar):
        self.type = type
        self.size = size
        self.sugar = sugar
    
    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"Coffee Order: {self.size} {self.type} with {self.sugar} sugar."

if __name__ == "__main__":
    original_order = CoffeeOrder("Latte", "Medium", "1 teaspoon")
    cloned_order = original_order.clone()
    
    print(original_order)
    print(cloned_order)

    """
    Coffee Order: Medium Latte with 1 teaspoon sugar.
    Coffee Order: Medium Latte with 1 teaspoon sugar.
    """