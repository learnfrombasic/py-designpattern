class CashierMeta:
    _name: str

    def __new__(cls, name):
        if not hasattr(cls, "instance"):
            cls.instance = super(CashierMeta, cls).__new__(cls)
            cls.instance._name = name

        return cls.instance


class Cashier(CashierMeta):
    def __repr__(self):
        return f"Cashier name is {self._name}"


if __name__ == "__main__":
    cashier_name = "Minh Le Duc 00"
    cashier_00 = Cashier(cashier_name)
    print(cashier_00)  # Cashier name is Minh Le Duc 00

    # Create another instance
    cashier_01 = Cashier(cashier_name)
    if cashier_00 == cashier_01:
        print("Both cashier share the same instance!!!")
