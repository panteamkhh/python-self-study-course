"""
Lesson 11 - Classes and Objects
Complete solutions for exercise.md
"""


# --- 1. Book (Easy) ----------------------------------------------------
# Basic class with two attributes and a describe() method.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"


book = Book("1984", "George Orwell")
print(book.describe())


# --- 2. Circle (Easy) ----------------------------------------------------
# A method computes and returns a derived value from an attribute.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


circle = Circle(5)
print(circle.area())


# --- 3. Light (Easy) ----------------------------------------------------
# Methods that toggle a boolean attribute.

class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


light = Light()
print(light.is_on)
light.turn_on()
print(light.is_on)


# --- 4. Student (Medium) ----------------------------------------------------
# A list attribute grows over time; average() guards against division by zero.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


student = Student("Maya")
student.add_grade(90)
student.add_grade(80)
print(student.average())


# --- 5. Car (Medium) ----------------------------------------------------
# drive() updates state that persists between calls.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles

    def info(self):
        print(f"{self.make} {self.model} — {self.mileage} miles")


car = Car("Toyota", "Corolla")
car.drive(150)
car.info()


# --- 6. TodoList (Medium) ----------------------------------------------------
# Managing a list attribute: add, remove, and display.

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks!")
        else:
            for task in self.tasks:
                print(task)


todo = TodoList()
todo.add_task("Buy milk")
todo.add_task("Walk dog")
todo.complete_task("Buy milk")
todo.show_tasks()


# --- 7. Temperature (Medium) ----------------------------------------------------
# Conversion methods that do not mutate the stored value.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15


temp = Temperature(25)
print(temp.to_fahrenheit())
print(temp.to_kelvin())


# --- 8. Inventory (Hard) ----------------------------------------------------
# Dictionary attribute with guarded modification.

class Inventory:
    def __init__(self):
        self.products = {}

    def add_stock(self, name, amount):
        self.products[name] = self.products.get(name, 0) + amount

    def remove_stock(self, name, amount):
        current = self.products.get(name, 0)
        if amount > current:
            print(f"Cannot remove {amount} of '{name}' — only {current} in stock.")
        else:
            self.products[name] = current - amount

    def report(self):
        for name, qty in self.products.items():
            print(f"{name}: {qty}")


inventory = Inventory()
inventory.add_stock("Apples", 10)
inventory.remove_stock("Apples", 3)
inventory.report()


# --- 9. Login System (Hard) ----------------------------------------------------
# A simple stand-in for password hashing using string reversal.

class User:
    def __init__(self, username, password):
        self.username = username
        self._stored = password[::-1]  # pretend "hash"

    def check_password(self, attempt):
        return attempt[::-1] == self._stored


user = User("alice", "secret")
print(user.check_password("secret"))
print(user.check_password("wrong"))


# --- 10. ATM (Hard) ----------------------------------------------------
# Combines authentication logic with a guarded state change.

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def authenticate(self, pin):
        return pin == self.pin

    def withdraw(self, pin, amount):
        if not self.authenticate(pin):
            print("Incorrect PIN.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")


atm = ATM(pin="1234", balance=200)
atm.withdraw("0000", 50)
atm.withdraw("1234", 50)
