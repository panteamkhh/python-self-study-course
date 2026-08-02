# Lesson 08 — Arguments and Scope

## 1. Introduction

Once you can define a function, the next step is understanding exactly *how* values move in and out of it, and *where* variables can be seen and used. This lesson covers two closely related ideas: **arguments** (the different ways to pass values into a function) and **scope** (the rules that decide which variables a piece of code can access).

This matters because most real bugs in beginner code come from misunderstanding scope — believing a variable inside a function is the "same" variable outside it, or vice versa. Getting this right is essential for writing predictable, bug-free programs, from simple scripts to large web applications with many interacting functions.

## 2. Conceptual Explanation

Think of each function call as its own private room. Variables created inside that room (local variables) exist only while the room is "open" — during that specific call — and disappear once the function finishes. Variables created outside any function, in the main hallway of your program, are called **global** variables and can be seen from anywhere, but functions cannot casually change them from inside their private room.

Python offers several ways to pass values into a room (function):

* **Positional arguments** — matched to parameters by their order: `add(2, 3)`.
* **Keyword arguments** — matched by name, order doesn't matter: `add(b=3, a=2)`.
* **Default arguments** — a fallback value used if the caller doesn't provide one: `def greet(name="friend")`.

```python
def describe(name, age=18):
    print(f"{name} is {age} years old")

describe("Sara")            # uses default age
describe("Reza", 25)        # positional
describe(name="Mona", age=30)  # keyword
```

## 3. Diagrams

**Scope as nested rooms:**

```
+-------------------------------+
| Global scope (main hallway)   |
|   x = 10                      |
|                                |
|   +------------------------+  |
|   | Function scope         |  |
|   |   (local room)         |  |
|   |   y = x + 1  <- can    |  |
|   |     read global x      |  |
|   +------------------------+  |
|                                |
|   (y does not exist out here) |
+-------------------------------+
```

**Argument matching:**

```
def add(a, b):
    return a + b

add(2, 3)        -> a=2, b=3   (positional: order matters)
add(b=3, a=2)    -> a=2, b=3   (keyword: name matters, order doesn't)
```

## 4. Three Examples

### Example 1 — Simple: default arguments

**Explanation:** A default value is used automatically when the caller doesn't supply one.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Sara"))
print(greet("Reza", "Welcome"))
```

**Expected Output:**

```
Hello, Sara!
Welcome, Reza!
```

**Code Walkthrough:** The first call omits `greeting`, so Python uses the default `"Hello"`. The second call overrides the default with `"Welcome"`.

### Example 2 — Intermediate: local variables don't leak out

**Explanation:** A variable created inside a function only exists during that call.

```python
def calculate_area(width, height):
    area = width * height
    return area

print(calculate_area(4, 5))
print(area)
```

**Expected Output:**

```
20
Traceback (most recent call last):
    ...
NameError: name 'area' is not defined
```

**Code Walkthrough:** `area` is a **local** variable — it exists only inside `calculate_area`. Once the function returns, `area` no longer exists in the global scope, so referencing it afterward raises a `NameError`.

### Example 3 — Real-World: averaging student grades with a default weight

**Explanation:** A grading helper that reads a number of grades and computes their average, using arguments and keeping all working variables local to the function.

```python
def average(*grades):
    return sum(grades) / len(grades)

count = int(input())
values = []
for _ in range(count):
    values.append(float(input()))

result = average(*values)
print(f"{result:.2f}")
```

**Expected Output (for input `3`, `10.0`, `20.0`, `30.0`):**

```
20.00
```

**Code Walkthrough:** `*grades` collects any number of positional arguments into a tuple inside `average`. `*values` unpacks the list back into separate arguments when calling `average`. The function's internal variables (`grades`) stay local; only the returned average escapes back to the caller.

## 5. Common Mistakes

**Mistake 1 — Assuming a local variable exists outside its function**

```python
def compute():
    total = 100

compute()
print(total)
```

*Why it's wrong:* `total` only exists inside `compute`; it's gone once the function ends, causing a `NameError`.

```python
def compute():
    total = 100
    return total

total = compute()
print(total)
```

**Mistake 2 — Using a mutable default argument**

```python
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))
```

*Why it's wrong:* Default arguments are created **once**, when the function is defined — so the same list is reused and grows across calls, giving `["apple", "banana"]` on the second call instead of a fresh basket.

```python
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
```

**Mistake 3 — Mixing positional and keyword arguments incorrectly**

```python
def describe(name, age):
    print(f"{name} is {age}")

describe(age=25, "Sara")
```

*Why it's wrong:* Positional arguments must always come before keyword arguments in a call; this is a `SyntaxError`.

```python
describe("Sara", age=25)
```

**Mistake 4 — Trying to modify a global variable without `global`**

```python
count = 0

def increment():
    count = count + 1

increment()
print(count)
```

*Why it's wrong:* Assigning to `count` inside the function makes Python treat it as a new **local** variable, causing an `UnboundLocalError` because it's read before being assigned locally.

```python
count = 0

def increment():
    global count
    count = count + 1

increment()
print(count)
```

**Mistake 5 — Forgetting that default values are evaluated once, not per-call**

```python
import time

def log(message, timestamp=time.time()):
    print(message, timestamp)
```

*Why it's wrong:* `time.time()` runs only once, when the function is defined, so every call reuses the same "frozen" timestamp instead of the current time.

```python
def log(message, timestamp=None):
    if timestamp is None:
        timestamp = time.time()
    print(message, timestamp)
```

## 6. Debugging Practice

**Buggy Program 1:**

```python
def set_score():
    score = 100

set_score()
print(score)
```

**Buggy Program 2:**

```python
total = 0

def add_to_total(value):
    total = total + value

add_to_total(5)
print(total)
```

**Buggy Program 3:**

```python
def register(name, tags=[]):
    tags.append(name)
    return tags

print(register("Ali"))
print(register("Sara"))
```

### Corrected Versions

**Fix 1:**

```python
def set_score():
    score = 100
    return score

score = set_score()
print(score)
```

*Bug:* `score` is local to `set_score` and disappears after the function ends. *Why the fix works:* Returning the value and capturing it in a variable at the caller's scope keeps it accessible.

**Fix 2:**

```python
total = 0

def add_to_total(value):
    global total
    total = total + value

add_to_total(5)
print(total)
```

*Bug:* Without `global`, assigning to `total` inside the function creates a separate local variable, causing an `UnboundLocalError` when it tries to read `total` before assigning it. *Why the fix works:* `global total` tells Python to use the existing global variable instead of creating a local one.

**Fix 3:**

```python
def register(name, tags=None):
    if tags is None:
        tags = []
    tags.append(name)
    return tags

print(register("Ali"))
print(register("Sara"))
```

*Bug:* The mutable default list `[]` is shared across every call, so it keeps accumulating names from previous calls. *Why the fix works:* Using `None` as the default and creating a fresh list inside the function ensures each call starts with its own empty list.

## 7. Summary

* Arguments can be passed **positionally**, by **keyword**, or fall back to a **default** value.
* Positional arguments must come before keyword arguments in a call.
* Variables created inside a function are **local** and disappear once the function returns.
* Assigning to a variable inside a function makes it local by default — use `global` to modify a true global variable.
* Never use a **mutable default argument** (like `[]` or `{}`) — it's created once and shared across all calls; use `None` and create the value inside the function instead.
* `*args` collects extra positional arguments into a tuple; `*` before a list unpacks it into separate arguments when calling.
