# Cheat Sheet — Part 02 (Lessons 06–10)

A one-page quick reference for everything covered in this block: sets, defining functions, arguments and scope, higher-order functions, and exception handling.

---

## 1. Sets and Operations

```python
my_set = {1, 2, 3}
my_set = set(some_list)     # build a set from a list (removes duplicates)

a | b     # union — everything in either set
a & b     # intersection — only what's in both
a - b     # difference — in a but not in b
a ^ b     # symmetric difference — in exactly one of the two
```

| Term | Meaning |
|---|---|
| Set | Unordered collection of unique, unchangeable items |
| Union (`\|`) | Combine two sets, no duplicates |
| Intersection (`&`) | Elements common to both sets |
| Difference (`-`) | Elements in the first set only |

**Common mistakes**
- Sets have no order and no indexing — `my_set[0]` raises `TypeError`.
- `{}` creates an empty **dict**, not an empty set — use `set()`.

---

## 2. Defining Functions

```python
def function_name(parameter):
    """Optional docstring describing what the function does."""
    result = parameter * 2
    return result

output = function_name(5)
```

| Term | Meaning |
|---|---|
| Parameter | Name listed in the function definition |
| Argument | Actual value passed in when calling the function |
| `return` | Sends a value back to the caller and ends the function |
| Function with no `return` | Implicitly returns `None` |

**Best practices**
- Give functions a single, clear responsibility.
- Prefer `return`ing a value over `print()`ing inside a function that other code needs to reuse.

---

## 3. Arguments and Scope

```python
def greet(name, greeting="Hello"):   # default argument
    return f"{greeting}, {name}!"

def average(*numbers):               # *args — variable positional arguments
    return sum(numbers) / len(numbers)

def configure(**settings):           # **kwargs — variable keyword arguments
    return settings
```

| Term | Meaning |
|---|---|
| Default argument | Used automatically when the caller omits that argument |
| Local scope | Variables created inside a function; invisible outside it |
| Global scope | Variables created at the top level of the script |
| `*args` | Collects extra positional arguments into a tuple |
| `**kwargs` | Collects extra keyword arguments into a dict |

**Common mistakes**
- Reading a function's local variable from outside it → `NameError`.
- Mutable default arguments (`def f(items=[])`) persist between calls — use `None` and create the list inside the function instead.

---

## 4. Higher-Order Functions

```python
double = lambda x: x * 2                       # anonymous function
squared = list(map(lambda x: x ** 2, values))  # apply to every item
evens = list(filter(lambda x: x % 2 == 0, values))  # keep matching items
ranked = sorted(people, key=lambda p: p[1], reverse=True)  # custom sort order
```

| Term | Meaning |
|---|---|
| Higher-order function | A function that takes another function as an argument (or returns one) |
| `lambda` | A small, unnamed function limited to a single expression |
| `map()` | Applies a function to every item of an iterable |
| `filter()` | Keeps only the items for which a function returns `True` |
| `key=` | Tells `sorted()`/`max()`/`min()` what to compare by |

**Common mistakes**
- `map()` and `filter()` return iterators, not lists — wrap in `list(...)` to see or reuse the results.
- Overusing `lambda` for logic that needs more than one line — define a regular function instead.

---

## 5. Try and Except

```python
try:
    risky_operation()
except ValueError:
    handle_value_error()
except (TypeError, ZeroDivisionError):
    handle_either()
else:
    runs_only_if_no_exception()
finally:
    always_runs()
```

| Term | Meaning |
|---|---|
| `try` | Block of code that might raise an exception |
| `except` | Runs only if a matching exception occurs |
| `else` | Runs only if the `try` block succeeded |
| `finally` | Always runs, exception or not — used for cleanup |

**Best practices**
- Catch specific exception types (`ValueError`, `ZeroDivisionError`) instead of a bare `except:`.
- Use `finally` for cleanup that must always happen (closing files, releasing resources).

**Common mistakes**
- A bare `except:` silently swallows every error, including typos and `KeyboardInterrupt`, making bugs hard to find.
- Putting too much code inside `try` — keep only the line(s) that can actually fail.

---

**Covers:** [Lesson 06](./Lesson-06-Sets-and-Operations) · [Lesson 07](./Lesson-07-Defining-Functions) · [Lesson 08](./Lesson-08-Arguments-and-Scope) · [Lesson 09](./Lesson-09-Higher-Order-Functions) · [Lesson 10](./Lesson-10-Try-and-Except)
