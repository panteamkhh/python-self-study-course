"""
Lesson 12 - Inheritance and Polymorphism
Complete solutions for exercise.md
"""


# --- 1. Employee / Manager (Easy) ----------------------------------------------------
# A subclass that inherits everything without changes.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    pass


m = Manager("Dana", 90000)
print(m.name, m.salary)


# --- 2. Bird / Penguin (Easy) ----------------------------------------------------
# Overriding a method in a subclass.

class Bird:
    def fly(self):
        return "Flying high!"


class Penguin(Bird):
    def fly(self):
        return "Penguins can't fly, but they can swim!"


print(Bird().fly())
print(Penguin().fly())


# --- 3. Shape / Triangle (Easy) ----------------------------------------------------

class Shape:
    def describe(self):
        return "I am a shape"


class Triangle(Shape):
    def describe(self):
        return "I am a triangle"


print(Shape().describe())
print(Triangle().describe())


# --- 4. Employee / Manager with super() (Medium) ----------------------------------------

class Employee2:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager2(Employee2):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


mgr = Manager2("Dana", 90000, 5)
print(mgr.name, mgr.salary, mgr.team_size)


# --- 5. Vehicle fuel types (Medium) ----------------------------------------------------
# Polymorphism: a loop calls the same method on different subclasses.

class Vehicle:
    def fuel_type(self):
        return "Unknown"


class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"


class GasCar(Vehicle):
    def fuel_type(self):
        return "Gasoline"


for v in [ElectricCar(), GasCar()]:
    print(v.fuel_type())


# --- 6. Payment methods (Medium) ----------------------------------------------------

class PaymentMethod:
    def process(self, amount):
        return f"Processing ${amount} via generic method"


class CreditCard(PaymentMethod):
    def process(self, amount):
        return f"Processing ${amount} via credit card"


class PayPal(PaymentMethod):
    def process(self, amount):
        return f"Processing ${amount} via PayPal"


for method in [CreditCard(), PayPal()]:
    print(method.process(50))


# --- 7. Student / HonorsStudent (Medium) ----------------------------------------------------
# Extending, rather than replacing, the parent's method using super().

class Student:
    def __init__(self, name):
        self.name = name

    def status(self):
        return "Regular student"


class HonorsStudent(Student):
    def status(self):
        return super().status() + " (Honors)"


print(HonorsStudent("Lee").status())


# --- 8. Product / DiscountedProduct (Hard) ----------------------------------------------------
# Polymorphism used to avoid manual type-checking.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price


class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def final_price(self):
        return self.price * (1 - self.discount_percent / 100)


products = [Product("Mug", 10), DiscountedProduct("Shirt", 40, 25)]
for p in products:
    print(f"{p.name}: ${p.final_price():.2f}")


# --- 9. Animal chorus (Hard) ----------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof"


class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow"


class Snake(Animal):
    def speak(self):
        return f"{self.name}: Hiss"


def animal_chorus(animals):
    return ", ".join(animal.speak() for animal in animals)


zoo = [Dog("Rex"), Cat("Tom"), Snake("Kaa")]
print(animal_chorus(zoo))


# --- 10. ATM login roles (Hard) ----------------------------------------------------

class Account:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin

    def access_level(self):
        return "basic"


class AdminAccount(Account):
    def access_level(self):
        return "admin"

    def reset_account(self, other_account):
        other_account.pin = "0000"
        print(f"{other_account.username}'s PIN was reset by an admin.")


regular = Account("bob", "1234")
admin = AdminAccount("alice", "admin1")
admin.reset_account(regular)
print(regular.pin)
