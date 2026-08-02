# Lesson 07 — Defining Functions

## 1. Introduction

A **function** is a named, reusable block of code that performs a specific task. Instead of repeating the same lines over and over, you write them once inside a function and simply *call* the function whenever you need that behavior.

Functions matter because they let you:

* Break a large problem into small, understandable pieces.
* Reuse logic without copy-pasting code.
* Give a name to a piece of behavior, making the program read like a story.

In real-world software, functions are everywhere: `send_email()`, `calculate_total()`, `validate_password()`, `is_palindrome()`. Every serious program is built from many small, well-named functions working together.

## 2. Conceptual Explanation

Think of a function like a kitchen recipe card. The card has a name ("Make Pancakes"), it may need certain ingredients (parameters), and it produces a result (the pancakes — the return value). You can hand the same recipe card to ten different cooks, give them different ingredients, and each time they follow the same steps to produce a result.

A function is written once, and then it's *called* — used — as many times as needed, each time possibly with different input values.

### Defining and calling a function

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Sara")
print(message)
```

Here, `def` starts the function definition, `name` is a **parameter** (a placeholder for input), and `return` sends a value back to whoever called the function.

## 3. Diagrams

**Function call flow:**

```
  caller code
      |
      | greet("Sara")
      v
  +---------------------+
  | def greet(name):    |   name = "Sara"
  |     return f"Hi {name}"|
  +---------------------+
      |
      | returns "Hi Sara"
      v
  caller code continues
```

**Parameter vs. Argument:**

```
def greet(name):      <- "name" is the PARAMETER (placeholder)
    return f"Hi {name}"

greet("Sara")          <- "Sara" is the ARGUMENT (actual value passed)
```

## 4. Three Examples

### Example 1 — Simple: a function with no parameters

**Explanation:** The simplest function just runs a block of code every time it's called.

```python
def say_hello():
    print("Hello there!")

say_hello()
say_hello()
```

**Expected Output:**

```
Hello there!
Hello there!
```

**Code Walkthrough:** `say_hello` takes no input and always prints the same message. Calling it twice runs the function body twice.

### Example 2 — Intermediate: a function that returns a value

**Explanation:** Instead of printing directly, a function can `return` a value so the caller decides what to do with it.

```python
def square(number):
    return number * number

result = square(5)
print(result)
print(square(3) + square(4))
```

**Expected Output:**

```
25
25
```

**Code Walkthrough:** `square` computes `number * number` and returns it. The returned value can be stored in a variable (`result`) or used directly in another expression, like `square(3) + square(4)`.

### Example 3 — Real-World: checking if a word is a palindrome

**Explanation:** A common practical task — write a function that decides whether a given word reads the same forwards and backwards, then use it to answer an input.

```python
def is_palindrome(word):
    return word == word[::-1]

text = input()
if is_palindrome(text):
    print("yes")
else:
    print("no")
```

**Expected Output (for input `racecar`):**

```
yes
```

**Code Walkthrough:** `word[::-1]` reverses the string using slicing. Comparing the original word to its reversed version tells us whether it's a palindrome. The function returns a boolean, which the `if` statement then uses to print `"yes"` or `"no"`.

## 5. Common Mistakes

**Mistake 1 — Forgetting to call the function**

```python
def greet():
    print("Hi!")

greet
```

*Why it's wrong:* `greet` (without parentheses) just refers to the function object; it never runs the code inside.

```python
greet()
```

**Mistake 2 — Confusing `print` inside a function with `return`**

```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result + 1)
```

*Why it's wrong:* `add` prints the sum but returns `None` (nothing), so `result` is `None`, and `result + 1` crashes.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result + 1)
```

**Mistake 3 — Using a parameter name that shadows a built-in**

```python
def process(list):
    return list[0]
```

*Why it's wrong:* Naming a parameter `list` hides Python's built-in `list` type inside the function, which can cause confusing bugs if you need the real `list()` later.

```python
def process(items):
    return items[0]
```

**Mistake 4 — Wrong number of arguments**

```python
def add(a, b):
    return a + b

print(add(5))
```

*Why it's wrong:* `add` requires two arguments; calling it with only one raises a `TypeError`.

```python
print(add(5, 3))
```

**Mistake 5 — Expecting a function to modify a variable it wasn't given**

```python
def double(n):
    n = n * 2

x = 5
double(x)
print(x)
```

*Why it's wrong:* `double` only changes its own local copy of `n`; the original `x` outside the function is untouched, so this prints `5`, not `10`.

```python
def double(n):
    return n * 2

x = 5
x = double(x)
print(x)
```

## 6. Debugging Practice

**Buggy Program 1:**

```python
def multiply(a, b)
    return a * b

print(multiply(4, 5))
```

**Buggy Program 2:**

```python
def is_even(number):
    if number % 2 == 0:
        print(True)
    else:
        print(False)

result = is_even(10)
print(result and "even confirmed")
```

**Buggy Program 3:**

```python
def area(width, height):
    return width * height

print(area(width=5))
```

### Corrected Versions

**Fix 1:**

```python
def multiply(a, b):
    return a * b

print(multiply(4, 5))
```

*Bug:* The function definition is missing a colon `:` after the parentheses. *Why the fix works:* Python requires a colon to mark the start of the function body.

**Fix 2:**

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(10)
print(result and "even confirmed")
```

*Bug:* `is_even` prints instead of returning, so `result` is `None`, and `None and "..."` produces `None` instead of the intended message. *Why the fix works:* Returning the boolean lets the caller actually use the result in a later expression.

**Fix 3:**

```python
def area(width, height):
    return width * height

print(area(width=5, height=3))
```

*Bug:* `area` requires both `width` and `height`; calling it with only `width` raises a `TypeError`. *Why the fix works:* Supplying both required arguments (here as keyword arguments) satisfies the function's signature.

## 7. Summary

* A function is defined with `def name(parameters):` and can be called by name with `()`.
* Parameters are placeholders; arguments are the actual values passed when calling.
* `return` sends a value back to the caller; a function without `return` gives back `None`.
* Printing inside a function is not the same as returning a value — don't confuse the two.
* Changing a parameter inside a function does not affect the original variable outside it.
* Well-named functions make code easier to read, test, and reuse.
