"""
Lesson 12 - Inheritance and Polymorphism
All three examples from lesson.md, ready to run as-is.
"""


# --- Example 1: Basic Inheritance -------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."


class Dog(Animal):
    pass


# --- Example 2: Overriding and Polymorphism ---------------------------------

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


# --- Example 3: Login System User Roles -------------------------------------

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, password):
        if password == self.password:
            return f"{self.username} logged in successfully."
        return "Incorrect password."

    def permissions(self):
        return "read"


class AdminUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.is_admin = True

    def permissions(self):
        return "read, write, delete"


def main():
    print("--- Example 1 ---")
    d = Dog("Rex")
    print(d.eat())

    print("\n--- Example 2 ---")
    shapes = [Square(4), Circle(3)]
    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area():.2f}")

    print("\n--- Example 3 ---")
    users = [User("bob", "1234"), AdminUser("alice", "admin1")]
    for user in users:
        print(f"{user.username}: {user.permissions()}")


if __name__ == "__main__":
    main()
