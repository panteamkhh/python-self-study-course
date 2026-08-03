# Lesson 11 — Classes and Objects

## 1. Introduction

**What is this topic?**

A *class* is a blueprint for creating your own custom data type. An *object* (also called an *instance*) is a concrete thing built from that blueprint. Up to now you have used Python's built-in types — `int`, `str`, `list`, `dict`. Classes let you design **your own** types that fit your problem.

**Why is it important?**

Real programs model real things: users, products, bank accounts, game characters. A `dict` can hold data, but it can't easily hold *behavior* (functions that belong to that data) or *guarantee* the data always makes sense. Classes solve both problems.

**Where is it used in real-world software?**

- Web frameworks (Django `Model`, Flask `Blueprint`) represent database rows as objects.
- Game engines represent every character, weapon, and enemy as an object.
- GUI toolkits represent every button and window as an object.
- Almost every Python library you will ever import (`requests.Response`, `pandas.DataFrame`, `pathlib.Path`) is a class.

---

## 2. Conceptual Explanation

**Real-world analogy:** Think of a *class* as a cookie cutter, and an *object* as an actual cookie made with it. The cutter defines the *shape* every cookie will have (round, star, etc.) — that's like the attributes and methods a class defines. Each cookie you actually cut out and bake is a separate, independent object — you can decorate one with chocolate and another with sprinkles, and changing one cookie doesn't change another.

In Python terms:

- The **class** defines what attributes (data) and methods (functions) every object of that type will have.
- Each **object** created from the class has its *own* copy of the data (attributes), but *shares* the same methods (behavior) defined by the class.

**Introducing the syntax**

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
```

- `class Dog:` starts the blueprint.
- `__init__` is the **constructor** — Python calls it automatically every time you create a new `Dog`. It sets up the object's starting data.
- `self` refers to "this particular object." It is always the first parameter of a method, and Python passes it automatically.
- `self.name = name` stores `name` as an **attribute** on this specific object.
- `bark` is a **method** — a function that belongs to the class and can use `self` to access that object's data.

Creating and using an object:

```python
my_dog = Dog("Rex", "Labrador")
print(my_dog.name)     # Rex
print(my_dog.bark())   # Rex says Woof!
```

---

## 3. Diagrams

**Object Creation Flow**

```text
Dog("Rex", "Labrador")
        |
        v
Python creates a new empty object
        |
        v
Python calls __init__(self, "Rex", "Labrador")
        |
        v
self.name = "Rex"
self.breed = "Labrador"
        |
        v
my_dog  ---->  [ Dog object ]
                  name:  "Rex"
                  breed: "Labrador"
```

**Class vs. Object (Memory Diagram)**

```text
class Dog (the blueprint — lives once)
   methods: __init__, bark

my_dog  ---> object #1: {name: "Rex",  breed: "Labrador"}
your_dog---> object #2: {name: "Fido", breed: "Poodle"}
```

Each object has its own data, but both use the exact same `bark` method from the class.

---

## 4. Three Examples

### Example 1 — A Simple `Point` Class

**Explanation:** A minimal class with two attributes and one method.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def describe(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
print(p1.describe())
```

**Expected output:**

```text
Point(2, 3)
```

**Code walkthrough:** `Point(2, 3)` calls `__init__`, which stores `x=2` and `y=3` on the new object. `p1.describe()` runs `describe`, using `self.x` and `self.y` from that specific object.

---

### Example 2 — A `BankAccount` with Behavior

**Explanation:** A class whose methods change the object's own data over time.

```python
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


account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.show_balance()
```

**Expected output:**

```text
Alice's balance: $120
```

**Code walkthrough:** The account "remembers" its balance between method calls because the balance lives on `self`, not in a local variable that disappears after each call.

---

### Example 3 — A Practical `ShoppingCart`

**Explanation:** A realistic example combining a list attribute, multiple methods, and a loop.

```python
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


cart = ShoppingCart("Bob")
cart.add_item("Book", 12.99)
cart.add_item("Pen", 1.50)
cart.receipt()
```

**Expected output:**

```text
Receipt for Bob:
  Book: $12.99
  Pen: $1.50
Total: $14.49
```

**Code walkthrough:** `self.items` starts as an empty list belonging to this cart only. Each `add_item` call appends a dictionary to it. `total()` uses a generator expression to sum all prices. `receipt()` loops over `self.items` to print each one.

---

## 5. Common Mistakes

**Mistake 1 — Forgetting `self` in a method definition**

```python
class Dog:
    def bark():          # WRONG
        return "Woof!"
```

Why it's wrong: every method needs `self` as its first parameter because Python automatically passes the object into it. Calling `my_dog.bark()` will raise `TypeError: bark() takes 0 positional arguments but 1 was given`.

Correct solution:

```python
class Dog:
    def bark(self):
        return "Woof!"
```

---

**Mistake 2 — Forgetting to use `self.` when storing an attribute**

```python
class Dog:
    def __init__(self, name):
        name = name   # WRONG — this is just a local variable
```

Why it's wrong: without `self.`, `name` is a temporary local variable that disappears when `__init__` finishes. The object never actually stores it, so `my_dog.name` raises `AttributeError`.

Correct solution:

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

---

**Mistake 3 — Confusing the class with an object**

```python
class Dog:
    def __init__(self, name):
        self.name = name

print(Dog.name)   # WRONG — Dog is the blueprint, it has no "name"
```

Why it's wrong: `Dog` itself is the class (the cutter), not a cookie. `name` only exists on *objects* created from `Dog`.

Correct solution:

```python
my_dog = Dog("Rex")
print(my_dog.name)
```

---

**Mistake 4 — Using a mutable default argument**

```python
class ShoppingCart:
    def __init__(self, items=[]):   # WRONG
        self.items = items
```

Why it's wrong: default argument values are created **once**, when the function is defined, and shared across every call. Every `ShoppingCart` created without arguments would silently share the *same* list, so adding an item to one cart would affect all of them.

Correct solution:

```python
class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

---

**Mistake 5 — Calling a method as if it were a plain function**

```python
account = BankAccount("Alice", 100)
BankAccount.deposit(50)   # WRONG — missing the object
```

Why it's wrong: `deposit` needs to know *which* account to change. Calling it on the class instead of an object leaves `self` unfilled (or fills it with the wrong value), causing a `TypeError`.

Correct solution:

```python
account.deposit(50)
```

---

## 6. Debugging Practice

**Buggy Program 1**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return width * height   # bug


r = Rectangle(4, 5)
print(r.area())
```

**Buggy Program 2**

```python
class Counter:
    def __init__(self):
        count = 0   # bug

    def increment(self):
        self.count += 1


c = Counter()
c.increment()
print(c.count)
```

**Buggy Program 3**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"


p = Person("Sam", 30)
print(Person.greet())   # bug
```

### Corrected Versions

**Program 1 — Fix**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r = Rectangle(4, 5)
print(r.area())
```

*Bug:* `area` used the bare names `width` and `height`, which don't exist inside the method — only the parameters of `__init__` did, and they are long gone. *Why the fix works:* `self.width` and `self.height` read the values stored on the object itself, which persist for the object's lifetime.

**Program 2 — Fix**

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


c = Counter()
c.increment()
print(c.count)
```

*Bug:* `count = 0` created a local variable inside `__init__` that vanished as soon as `__init__` returned, so the object never actually had a `count` attribute. *Why the fix works:* `self.count = 0` attaches `count` to the object, so later methods can read and modify it.

**Program 3 — Fix**

```python
p = Person("Sam", 30)
print(p.greet())
```

*Bug:* `Person.greet()` calls the method on the class, but `greet` needs a `self` (a specific person) to know whose name to use. *Why the fix works:* calling `p.greet()` automatically passes `p` in as `self`.

---

## 7. Summary

- A **class** is a blueprint; an **object** (instance) is a concrete thing built from that blueprint.
- `__init__` is the constructor — it runs automatically when you create an object and sets up its starting attributes.
- `self` refers to the specific object a method is running on, and must be the first parameter of every method.
- Attributes must be stored with `self.attribute_name = value` to persist on the object.
- Every object made from a class has its own independent data but shares the class's methods.
- Never use a mutable value (like `[]`) as a default argument.
