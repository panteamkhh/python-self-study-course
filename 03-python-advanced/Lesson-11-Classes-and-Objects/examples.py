"""
Lesson 11 - Classes and Objects
All three examples from lesson.md, ready to run as-is.
"""


# --- Example 1: A Simple Point Class ---------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def describe(self):
        return f"Point({self.x}, {self.y})"


# --- Example 2: A BankAccount with Behavior ---------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")


# --- Example 3: A Practical ShoppingCart ------------------------------------

class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def total(self):
        return sum(item["price"] for item in self.items)

    def receipt(self):
        print(f"Receipt for {self.customer_name}:")
        for item in self.items:
            print(f"  {item['name']}: ${item['price']:.2f}")
        print(f"Total: ${self.total():.2f}")


def main():
    print("--- Example 1 ---")
    p1 = Point(2, 3)
    print(p1.describe())

    print("\n--- Example 2 ---")
    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    account.show_balance()

    print("\n--- Example 3 ---")
    cart = ShoppingCart("Bob")
    cart.add_item("Book", 12.99)
    cart.add_item("Pen", 1.50)
    cart.receipt()


if __name__ == "__main__":
    main()
