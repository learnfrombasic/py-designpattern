# Builder Pattern

> Keywords: step-by-step creation, flexibility, complex objects

## Introduction

When ordering coffee, some people like to customize it—choosing bean type, milk option, sugar levels, and toppings. Instead of overwhelming the barista with all choices at once, it’s easier to build the coffee step by step.

This is the Builder Pattern, which helps construct complex objects piece by piece.

## Problem Statement

Imagine you and I walk into a coffee shop and want highly customized drinks. If the barista had to manage all details at once, mistakes would be frequent, and orders would be inconsistent.

Similarly, in programming, constructing complex objects with multiple attributes can be messy and hard to manage.

## Solution

The Builder Pattern simplifies object creation by allowing step-by-step construction of an object.

### Benefits

Provides a clear and flexible way to create complex objects.

Avoids large, unreadable constructors.

Ensures consistency when building objects with multiple parameters.

### Code Implementation

```python
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
    print(coffee)
```

## Conclusion
Just like how a coffee shop allows customers to customize their drinks step by step, the Builder Pattern helps create complex objects in a structured and flexible manner.

