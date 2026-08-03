# Lesson 13 — Special Methods (Dunder Methods)

## 1. Introduction

**What is this topic?**

*Special methods* (also called **dunder methods**, short for "double underscore") are methods with names like `__init__`, `__str__`, and `__add__`. You already met `__init__`. These methods let your custom objects work with Python's built-in syntax and functions — `print()`, `+`, `==`, `len()`, and more — instead of only working through explicitly named methods.

**Why is it important?**

Without special methods, `print(my_object)` shows an unreadable memory address, `obj1 + obj2` raises an error, and `len(my_object)` doesn't work at all. Special methods let your own classes feel just as natural to use as Python's built-in types.

**Where is it used in real-world software?**

- `datetime` objects can be compared (`<`, `>`) and subtracted (`-`) because of special methods.
- NumPy/pandas objects support `+`, `*`, indexing (`obj[0]`), and `len()` through special methods.
- Custom exception classes use `__str__` to control the error message shown to users.
- Data classes (like a `Money` or `Vector` class) use `__eq__` and `__add__` to behave like numbers.

---

## 2. Conceptual Explanation

**Real-world analogy:** Think of special methods as a *universal remote control's* standard buttons. Every TV brand wires its own circuitry differently inside, but they all agree that pressing "Power" turns the TV on. Python's built-in operators (`+`, `==`, `len()`, `print()`) are like those standard buttons — special methods are how *your* class wires up what happens when someone "presses" them.

**Introducing the syntax**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

- `__str__` controls what `print(obj)` or `str(obj)` displays.
- `__eq__` controls what `obj1 == obj2` checks.
- `__add__` controls what `obj1 + obj2` returns.

```python
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)             # uses __str__
print(p1 == Point(1, 2))  # uses __eq__
print(p1 + p2)         # uses __add__
```

Common special methods:

| Method       | Triggered by     |
|--------------|-------------------|
| `__init__`   | Creating an object |
| `__str__`    | `print(obj)`, `str(obj)` |
| `__repr__`   | Typing `obj` in the console, debugging |
| `__eq__`     | `obj1 == obj2` |
| `__lt__`     | `obj1 < obj2` |
| `__add__`    | `obj1 + obj2` |
| `__len__`    | `len(obj)` |
| `__getitem__`| `obj[index]` |

---

## 3. Diagrams

**How Python Routes Built-in Syntax**

```text
print(p1)
   |
   v
Python looks for p1.__str__()
   |
   v
runs your custom __str__ code
   |
   v
displays the returned string
```

```text
p1 + p2
   |
   v
Python looks for p1.__add__(p2)
   |
   v
runs your custom __add__ code
   |
   v
returns a new object
```

**Method Resolution at a Glance**

```text
Operator/Function        Special Method Called
--------------------     ----------------------
print(obj) / str(obj) -> obj.__str__()
obj1 == obj2           -> obj1.__eq__(obj2)
obj1 + obj2            -> obj1.__add__(obj2)
len(obj)               -> obj.__len__()
obj[i]                 -> obj.__getitem__(i)
```

---

## 4. Three Examples

### Example 1 — `__str__` for Readable Printing

**Explanation:** Without `__str__`, printing an object shows something unhelpful like `<__main__.Point object at 0x...>`.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p = Point(3, 4)
print(p)
```

**Expected output:**

```text
Point(3, 4)
```

**Code walkthrough:** `print(p)` internally calls `str(p)`, which calls `p.__str__()`, returning our custom formatted string.

---

### Example 2 — `__eq__` and `__add__` for a `Money` Class

**Explanation:** Two different `Money` objects can be compared and added like numbers.

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"${self.amount:.2f}"


a = Money(10)
b = Money(5)
print(a + b)
print(a == Money(10))
```

**Expected output:**

```text
$15.00
True
```

**Code walkthrough:** `a + b` calls `a.__add__(b)`, returning a new `Money` object. `a == Money(10)` calls `a.__eq__(Money(10))`, comparing the underlying amounts instead of comparing memory addresses.

---

### Example 3 — Practical Example: An Inventory with `__len__` and `__getitem__`

**Explanation:** Custom container-like behavior for an inventory system, so it can be used with `len()` and indexing like a list.

```python
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


inv = Inventory()
inv.add("Sword")
inv.add("Shield")
print(len(inv))
print(inv[0])
print(inv)
```

**Expected output:**

```text
2
Sword
Inventory with 2 item(s)
```

**Code walkthrough:** `len(inv)` calls `inv.__len__()`. `inv[0]` calls `inv.__getitem__(0)`. `print(inv)` calls `inv.__str__()`. The `Inventory` object now behaves like a built-in container, even though it's a custom class.

---

## 5. Common Mistakes

**Mistake 1 — Using `print()` and expecting `__repr__` to be used automatically for `str()`**

```python
class Point:
    def __repr__(self):
        return "Point repr"


p = Point()
print(p)   # works, but relies on Python's fallback
```

Why it's a common source of confusion: if `__str__` is missing, Python falls back to `__repr__`, which can hide bugs where you meant to define `__str__` specifically for user-facing output versus `__repr__` for debugging output.

Correct solution: define both when they should differ.

```python
class Point:
    def __str__(self):
        return "User-friendly Point"

    def __repr__(self):
        return "Point(debug info)"
```

---

**Mistake 2 — Forgetting to return a value from a special method**

```python
class Money:
    def __add__(self, other):
        total = self.amount + other.amount   # WRONG — no return
```

Why it's wrong: without `return`, `__add__` returns `None`, so `a + b` becomes `None` instead of a new `Money` object, and any further use of the result crashes.

Correct solution:

```python
class Money:
    def __add__(self, other):
        return Money(self.amount + other.amount)
```

---

**Mistake 3 — Comparing objects with `==` without defining `__eq__`**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print(Point(1, 2) == Point(1, 2))   # False! (surprising to beginners)
```

Why it's wrong (or surprising): without `__eq__`, Python compares by identity (are they the *same object in memory*), not by their data, so two `Point`s with identical coordinates are still considered unequal.

Correct solution:

```python
class Point:
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

**Mistake 4 — Using `self` instead of `other` correctly in comparison methods**

```python
class Money:
    def __eq__(self, other):
        return self.amount == self.amount   # WRONG — always True!
```

Why it's wrong: comparing `self.amount` to itself always returns `True`, regardless of what `other` actually is — a classic copy-paste mistake.

Correct solution:

```python
class Money:
    def __eq__(self, other):
        return self.amount == other.amount
```

---

**Mistake 5 — Implementing `__getitem__` but forgetting `__len__`**

```python
class Inventory:
    def __getitem__(self, index):
        return self.items[index]


inv = Inventory()
len(inv)   # WRONG — raises TypeError: object of type 'Inventory' has no len()
```

Why it's wrong: `len()` specifically requires `__len__`; having `__getitem__` alone does not provide it.

Correct solution:

```python
class Inventory:
    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]
```

---

## 6. Debugging Practice

**Buggy Program 1**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x, y"   # bug


p = Point(3, 4)
print(p)
```

**Buggy Program 2**

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        self.amount + other.amount   # bug


a = Money(10)
b = Money(5)
result = a + b
print(result)
```

**Buggy Program 3**

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.title   # bug


b = Book("Dune", 412)
print(len(b))
```

### Corrected Versions

**Program 1 — Fix**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"


p = Point(3, 4)
print(p)
```

*Bug:* `__str__` returned the literal text `"x, y"` instead of the actual values. *Why the fix works:* using an f-string with `self.x` and `self.y` inserts the real stored values.

**Program 2 — Fix**

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)


a = Money(10)
b = Money(5)
result = a + b
print(result.amount)
```

*Bug:* `__add__` computed the sum but never returned it, so `a + b` evaluated to `None`. *Why the fix works:* adding `return Money(...)` makes `__add__` produce a usable new object.

**Program 3 — Fix**

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages


b = Book("Dune", 412)
print(len(b))
```

*Bug:* `__len__` must return an integer, but it returned `self.title` (a string), causing `TypeError: 'str' object cannot be interpreted as an integer`. *Why the fix works:* returning `self.pages` (an int) satisfies what `len()` expects.

---

## 7. Summary

- Special methods (dunder methods) connect your classes to Python's built-in syntax like `print()`, `+`, `==`, and `len()`.
- `__str__` controls how an object looks when printed; `__repr__` is the debugging/console representation.
- `__eq__` defines what `==` means for your objects — without it, `==` compares identity, not data.
- `__add__` (and similar methods like `__sub__`, `__mul__`) let objects use math-style operators.
- `__len__` and `__getitem__` let custom objects behave like built-in containers (support `len()` and indexing).
- Special methods must `return` a value — forgetting `return` is a very common bug.
