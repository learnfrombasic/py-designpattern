# Prototype Pattern

> Keywords: cloning, object duplication, performance optimization

## Introduction

In a coffee shop, sometimes we want the exact same coffee order as our friend. Instead of manually specifying all details again, wouldn’t it be great if we could just duplicate their order?

This is the Prototype Pattern, where objects can clone themselves to create identical copies.

## Problem Statement

Imagine you and I order coffee, and I want mine exactly like yours. If the barista manually re-enters all details, it’s time-consuming and error-prone.

Similarly, in programming, creating objects from scratch every time can be inefficient. We need a way to quickly copy existing objects.

## Solution

The Prototype Pattern allows an object to create clones of itself. This improves performance and maintains consistency.

### Benefits

- Reduces object creation overhead.

- Ensures consistency between original and cloned objects.

- Useful for complex objects that take time to initialize.

## Code Implementation

```python
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
```

## Conclusion

Just like how a coffee shop can duplicate an order, the Prototype Pattern enables objects to clone themselves, making object creation efficient and flexible.

