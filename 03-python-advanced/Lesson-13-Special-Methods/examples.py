"""
Lesson 13 - Special Methods (Dunder Methods)
All three examples from lesson.md, ready to run as-is.
"""


# --- Example 1: __str__ for Readable Printing -------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# --- Example 2: __eq__ and __add__ for a Money Class ------------------------

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"${self.amount:.2f}"


# --- Example 3: Inventory with __len__ and __getitem__ ----------------------

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        return f"Inventory with {len(self)} item(s)"


def main():
    print("--- Example 1 ---")
    p = Point(3, 4)
    print(p)

    print("\n--- Example 2 ---")
    a = Money(10)
    b = Money(5)
    print(a + b)
    print(a == Money(10))

    print("\n--- Example 3 ---")
    inv = Inventory()
    inv.add("Sword")
    inv.add("Shield")
    print(len(inv))
    print(inv[0])
    print(inv)


if __name__ == "__main__":
    main()
