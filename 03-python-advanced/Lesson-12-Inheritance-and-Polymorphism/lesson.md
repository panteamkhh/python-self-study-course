# Lesson 12 — Inheritance and Polymorphism

## 1. Introduction

**What is this topic?**

*Inheritance* lets one class (the **child** / **subclass**) reuse and extend the attributes and methods of another class (the **parent** / **superclass**). *Polymorphism* means that objects of different classes can respond to the same method call, each in its own way ("many forms").

**Why is it important?**

Without inheritance, similar classes end up duplicating the same code over and over. Inheritance lets you write shared logic once, in a parent class, and only add or change what's different in each child. Polymorphism lets you write code that works with a *whole family* of related classes without needing to know the exact type ahead of time.

**Where is it used in real-world software?**

- GUI frameworks: `Button`, `Checkbox`, and `Slider` all inherit from a shared `Widget` class.
- Game development: `Enemy`, `Player`, and `NPC` might all inherit from a `Character` class.
- Web frameworks: custom exceptions inherit from `Exception`; custom views inherit from a base `View` class.
- Payment systems: `CreditCardPayment` and `PayPalPayment` might both inherit from a `Payment` class and implement their own `process()` method — that's polymorphism in action.

---

## 2. Conceptual Explanation

**Real-world analogy:** Think of a general blueprint for "Vehicle" — it has wheels, an engine, and can `move()`. A "Car" blueprint and a "Motorcycle" blueprint both **inherit** from "Vehicle": they automatically get wheels, an engine, and the ability to move, without redrawing those parts. Each one can then add its own special features (a car has four doors, a motorcycle can wheelie) or even change *how* `move()` works for that specific vehicle. That's inheritance and polymorphism together.

**Introducing the syntax**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

- `class Dog(Animal):` means `Dog` **inherits** from `Animal`. `Dog` automatically gets everything `Animal` has (like `__init__` and `self.name`), unless it defines its own version.
- `Dog` and `Cat` each **override** `speak()` — providing their own implementation. This is polymorphism: the same method name, different behavior per class.

```python
animals = [Dog("Rex"), Cat("Tom")]
for animal in animals:
    print(animal.speak())
```

This loop doesn't care whether each `animal` is a `Dog` or a `Cat` — it just calls `.speak()` and lets each object decide how to respond.

**`super()`**

Sometimes a child class wants to *extend* the parent's behavior rather than fully replace it:

```python
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)   # reuse Animal's __init__
        self.age = age
```

`super()` gives you access to the parent class's methods, so you don't have to rewrite them.

---

## 3. Diagrams

**Class Hierarchy**

```text
             Animal
            (name, speak)
            /          \
         Dog             Cat
   (speak overridden) (speak overridden)
         |
       Puppy
   (adds age, reuses
    Animal.__init__)
```

**Polymorphism at Call Time**

```text
for animal in [Dog("Rex"), Cat("Tom")]:
    animal.speak()
         |
         v
   Python checks: what class is this
   specific object actually made from?
         |
   Dog object  -----> runs Dog.speak()
   Cat object  -----> runs Cat.speak()
```

The variable `animal` is treated the same in the loop, but the correct version of `speak()` is chosen automatically based on the object's real class.

---

## 4. Three Examples

### Example 1 — Basic Inheritance

**Explanation:** A child class inherits an attribute and a method without redefining them.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."


class Dog(Animal):
    pass


d = Dog("Rex")
print(d.eat())
```

**Expected output:**

```text
Rex is eating.
```

**Code walkthrough:** `Dog` has no code of its own (`pass`), so it uses `Animal`'s `__init__` and `eat()` exactly as they are.

---

### Example 2 — Overriding and Polymorphism

**Explanation:** Multiple subclasses override the same method differently, and a single loop calls each correctly.

```python
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


shapes = [Square(4), Circle(3)]
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area():.2f}")
```

**Expected output:**

```text
Square area: 16.00
Circle area: 28.27
```

**Code walkthrough:** Both `Square` and `Circle` inherit from `Shape` and override `area()`. The loop treats every `shape` the same way, but each object computes its area using its own formula — that is polymorphism.

---

### Example 3 — Practical Example: Login System User Roles

**Explanation:** A base `User` class with shared login logic, extended by an `AdminUser` subclass that adds extra permissions.

```python
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


users = [User("bob", "1234"), AdminUser("alice", "admin1")]
for user in users:
    print(f"{user.username}: {user.permissions()}")
```

**Expected output:**

```text
bob: read
alice: read, write, delete
```

**Code walkthrough:** `AdminUser` reuses `User.__init__` via `super()` so it doesn't repeat the username/password setup, then adds `is_admin` and overrides `permissions()` to return more capabilities.

---

## 5. Common Mistakes

**Mistake 1 — Forgetting to call `super().__init__()`**

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed   # WRONG — name is never set
```

Why it's wrong: `Dog.__init__` completely replaces `Animal.__init__`, so `self.name` is never created, and `dog.name` raises `AttributeError`.

Correct solution:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

**Mistake 2 — Not putting the parent class in parentheses**

```python
class Dog Animal:   # WRONG — SyntaxError
    pass
```

Why it's wrong: Python requires parentheses to declare inheritance.

Correct solution:

```python
class Dog(Animal):
    pass
```

---

**Mistake 3 — Assuming overriding a method deletes the parent's version entirely**

```python
class Animal:
    def speak(self):
        return "generic sound"


class Dog(Animal):
    def speak(self):
        return "Woof! " + super().speak()   # this is FINE, but often forgotten
```

Why it's a common mistake: beginners often think they *must* rewrite everything from scratch in the child class, not realizing they can call `super().speak()` to reuse and build on the parent's version instead of duplicating logic.

Correct approach: use `super()` when you want to extend rather than fully replace behavior.

---

**Mistake 4 — Checking type manually instead of relying on polymorphism**

```python
for shape in shapes:
    if type(shape) == Square:          # WRONG — defeats the purpose
        print(shape.side ** 2)
    elif type(shape) == Circle:
        print(3.14159 * shape.radius ** 2)
```

Why it's wrong: this duplicates logic that should live inside each class's `area()` method, and it must be updated every time a new shape is added.

Correct solution:

```python
for shape in shapes:
    print(shape.area())
```

---

**Mistake 5 — Overriding `__init__` but forgetting extra parameters**

```python
class Puppy(Dog):
    def __init__(self, name):
        super().__init__(name)
        # forgot to accept/set "age" even though Puppy needs it
```

Why it's wrong: if `Puppy` is supposed to track `age`, forgetting the parameter means every `Puppy` object silently has no age data, causing `AttributeError` later when code tries to use `puppy.age`.

Correct solution:

```python
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

---

## 6. Debugging Practice

**Buggy Program 1**

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name, color):
        self.color = color   # bug


c = Cat("Tom", "black")
print(c.name)
```

**Buggy Program 2**

```python
class Shape:
    def area(self):
        return 0


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area():   # bug
        return 0.5 * self.base * self.height


t = Triangle(4, 6)
print(t.area())
```

**Buggy Program 3**

```python
class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class SportsCar(Car):
    pass


vehicles = [Vehicle(), Car(), SportsCar()]
for v in vehicles:
    print(v.move)   # bug
```

### Corrected Versions

**Program 1 — Fix**

```python
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


c = Cat("Tom", "black")
print(c.name)
```

*Bug:* `Cat.__init__` never called `Animal.__init__` (or set `self.name` itself), so `name` was never stored. *Why the fix works:* `super().__init__(name)` runs `Animal`'s constructor, which sets `self.name`.

**Program 2 — Fix**

```python
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


t = Triangle(4, 6)
print(t.area())
```

*Bug:* `area()` was missing the `self` parameter. *Why the fix works:* adding `self` lets the method access `self.base` and `self.height` on the calling object.

**Program 3 — Fix**

```python
for v in vehicles:
    print(v.move())   # calling the method, not referencing it
```

*Bug:* `v.move` (no parentheses) refers to the *method object itself*, not its result — Python prints something like `<bound method Car.move of ...>` instead of the string. *Why the fix works:* `v.move()` actually calls the method and prints its return value.

---

## 7. Summary

- **Inheritance** lets a child class reuse a parent class's attributes and methods by writing `class Child(Parent):`.
- **Overriding** means a child class defines its own version of a method that already exists in the parent.
- `super()` gives access to the parent class's methods, most commonly used inside `__init__` to reuse the parent's setup logic.
- **Polymorphism** means different classes can implement the same method name in their own way, and code that calls that method doesn't need to know which exact class it's working with.
- Prefer polymorphism (letting each class handle its own behavior) over manually checking `type()` in your code.
