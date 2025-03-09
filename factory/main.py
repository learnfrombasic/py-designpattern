class Coffee:
    def brew(self):
        pass

class ArabicaCoffee(Coffee):
    def brew(self):
        return "Brewing a cup of Arabica coffee!"

class RobustaCoffee(Coffee):
    def brew(self):
        return "Brewing a cup of Robusta coffee!"

class LibericaCoffee(Coffee):
    def brew(self):
        return "Brewing a cup of Liberica coffee!"

class CoffeeFactory:
    @staticmethod
    def get_coffee(bean_type):
        coffee_types = {
            "arabica": ArabicaCoffee(),
            "robusta": RobustaCoffee(),
            "liberica": LibericaCoffee()
        }
        return coffee_types.get(bean_type.lower(), None)

if __name__ == "__main__":
    coffee_type = "arabica"
    coffee = CoffeeFactory.get_coffee(coffee_type)
    if coffee:
        print(coffee.brew())        # Brewing a cup of Arabica coffee!
    else:
        print("Sorry, we don't have that coffee type.")