# Cheat Sheet — Part 03 (Lessons 11–15)

Quick reference for: Classes & Objects · Inheritance & Polymorphism · Special Methods · Generators & Yield · Generator Expressions

---

## 1. Classes & Objects

```python
class ClassName:
    def __init__(self, param1, param2):
        self.attr1 = param1
        self.attr2 = param2

    def method(self):
        return self.attr1

obj = ClassName(value1, value2)
obj.method()
```

| Term | Meaning |
|---|---|
| Class | Blueprint for creating objects |
| Object / Instance | A specific thing built from a class |
| `self` | Refers to the current object inside a method |
| `__init__` | Constructor — runs automatically on creation |
| Attribute | Data stored on an object (`self.x = x`) |
| Method | A function defined inside a class |

**Best practices**
- Always include `self` as the first parameter of instance methods.
- Never use a mutable default argument (`def __init__(self, items=[])`) — use `None` and set it inside the method instead.
- Store data with `self.attr`, not a bare local variable.

**Common mistakes**
- Forgetting `self` → `TypeError`.
- Forgetting `self.` when assigning → data lost after `__init__` ends.
- Calling a method on the class instead of an object (`ClassName.method()` instead of `obj.method()`).

---

## 2. Inheritance & Polymorphism

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Child(Parent):
    def __init__(self, name, extra):
        super().__init__(name)   # reuse parent logic
        self.extra = extra

    def speak(self):             # override
        return f"{self.name} says hi"
```

| Term | Meaning |
|---|---|
| Inheritance | Child class reuses parent's attributes/methods |
| `super()` | Access to the parent class's methods |
| Overriding | Child redefines a method from the parent |
| Polymorphism | Different classes respond to the same method call in their own way |

**Best practices**
- Call `super().__init__(...)` when the child needs the parent's setup logic too.
- Prefer polymorphism (`obj.method()`) over manual `type()` checks in loops.

**Common mistakes**
- Forgetting `super().__init__()` → parent's attributes never get set.
- Forgetting parentheses in `class Child(Parent):`.
- Writing `if type(x) == Y:` chains instead of relying on overridden methods.

---

## 3. Special Methods (Dunder Methods)

| Method | Triggered by |
|---|---|
| `__init__` | Creating an object |
| `__str__` | `print(obj)`, `str(obj)` |
| `__repr__` | Console/debug representation |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` (used by `sorted()`) |
| `__add__` | `obj1 + obj2` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[index]` |
| `__setitem__` | `obj[index] = value` |

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"${self.amount:.2f}"

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        return Money(self.amount + other.amount)
```

**Best practices**
- Always `return` a value from a special method.
- Define `__eq__` whenever you need `==` to compare data, not identity.

**Common mistakes**
- Forgetting `return` inside `__add__`/`__eq__` → result is `None`.
- Comparing `self.x == self.x` instead of `self.x == other.x`.
- Expecting `==` to compare data without defining `__eq__` (default compares identity).

---

## 4. Generators & Yield

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
next(gen)     # 3
for value in countdown(3):
    print(value)
```

| Concept | Meaning |
|---|---|
| `yield` | Pauses the function, returns a value, remembers state |
| `next(gen)` | Resumes execution until the next `yield` |
| `StopIteration` | Raised when a generator has no more values |
| Lazy evaluation | Values are computed only when requested |

**Best practices**
- Use generators for large or infinite sequences to save memory.
- Use a `for` loop instead of manual `next()` calls when possible — it handles `StopIteration` automatically.

**Common mistakes**
- Trying to index a generator (`gen[0]`) → `TypeError`.
- Reusing an exhausted generator → yields nothing the second time.
- Assuming the function body runs immediately when called — it only runs once `next()` is called.

---

## 5. Generator Expressions

```python
squares_list = [x * x for x in range(5)]     # list comprehension: builds immediately
squares_gen  = (x * x for x in range(5))     # generator expression: lazy

total = sum(x * x for x in range(5))         # parentheses can be omitted as sole argument
```

| Syntax | Behavior |
|---|---|
| `[...]` | List comprehension — builds full list immediately |
| `(...)` | Generator expression — lazy, one value at a time |
| `{...}` | Set comprehension (builds full set immediately) |

**Best practices**
- Use generator expressions when feeding data directly into `sum()`, `max()`, `min()`, `sorted()`, `any()`, `all()`.
- Use list comprehensions when you need to reuse or index the result multiple times.

**Common mistakes**
- Reusing an already-consumed generator expression.
- Trying to index a generator expression directly.
- Accidentally creating a one-item tuple with a trailing comma: `(x for x in range(5)),`.

---

## Quick Decision Guide

```text
Need a custom data type with behavior?          -> class
Need to share/extend behavior across types?      -> inheritance
Need your class to work with +, ==, print()?     -> special methods
Need to produce many/huge/infinite values,
one at a time, memory-efficiently?               -> generator (function or expression)
Need the full result stored/reused/indexed?      -> list / list comprehension
```
