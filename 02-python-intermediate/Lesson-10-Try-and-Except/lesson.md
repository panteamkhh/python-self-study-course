# Lesson 10 — Try and Except

## 1. Introduction

Programs don't always run smoothly — a user might type letters instead of numbers, a file might be missing, or a calculation might divide by zero. When Python hits one of these problems, it raises an **exception**, and if nothing handles it, the entire program crashes.

The `try`/`except` block lets a program **anticipate** possible errors and respond gracefully instead of crashing. This matters enormously in real software: a banking app should never crash just because a user typed "ten" instead of "10" — it should catch the problem and show a helpful message.

Exception handling is used everywhere: reading user input, working with files, calling external services (like APIs), and parsing data that might be malformed.

## 2. Conceptual Explanation

Think of `try`/`except` like a safety net under a tightrope walker. The walker (your code) attempts something risky — walking the rope (running the risky code). If they fall (an error occurs), the net (the `except` block) catches them instead of letting them hit the ground (crash the program).

```python
try:
    risky_code()
except SomeErrorType:
    handle_the_problem()
```

Python checks the `try` block line by line. The instant an error occurs, it immediately jumps to a matching `except` block instead of continuing. If no error occurs, the `except` block is simply skipped.

You can catch specific error types, which is much better practice than catching everything blindly:

```python
try:
    number = int(input())
except ValueError:
    print("That wasn't a valid number!")
```

## 3. Diagrams

**Try/Except control flow:**

```
   +-------------------+
   |  try:             |
   |    risky_line_1   |
   |    risky_line_2  <--- error happens here
   |    risky_line_3   |   (never runs)
   +-------------------+
             |
             | error detected -> jump immediately
             v
   +-------------------+
   |  except Error:    |
   |    handle it      |
   +-------------------+
             |
             v
      program continues
```

**No error case:**

```
try: runs completely, top to bottom -> except block is skipped entirely
```

## 4. Three Examples

### Example 1 — Simple: catching a `ValueError`

**Explanation:** Handle the case where converting text to a number fails.

```python
try:
    number = int("abc")
    print(number)
except ValueError:
    print("Conversion failed!")
```

**Expected Output:**

```
Conversion failed!
```

**Code Walkthrough:** `int("abc")` cannot convert the text to a number, so Python raises a `ValueError`. Because this happens inside the `try` block, control jumps immediately to the matching `except ValueError:` block instead of crashing.

### Example 2 — Intermediate: catching multiple exception types

**Explanation:** Handle both an invalid conversion and a division by zero in the same block, using separate `except` clauses.

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "two"))
```

**Expected Output:**

```
5.0
Cannot divide by zero
Both values must be numbers
```

**Code Walkthrough:** Each call to `safe_divide` may fail differently. Python matches the actual error to the correct `except` clause: dividing by `0` raises `ZeroDivisionError`, and dividing by a string raises `TypeError`. Each is handled with a specific, appropriate message.

### Example 3 — Real-World: dividing two user-provided numbers safely

**Explanation:** Read a numerator and a denominator from input, then safely compute and print the division result, handling the zero-division case explicitly.

```python
numerator = int(input())
denominator = int(input())

try:
    result = numerator / denominator
    print(f"{result:.2f}")
except ZeroDivisionError:
    print("cannot divide by zero")
```

**Expected Output (for input `10`, `3`):**

```
3.33
```

**Expected Output (for input `10`, `0`):**

```
cannot divide by zero
```

**Code Walkthrough:** The division happens inside `try`. When the denominator is `0`, Python raises `ZeroDivisionError`, which is caught and turned into a friendly message instead of crashing the program.

## 5. Common Mistakes

**Mistake 1 — Using a bare `except:` that hides real bugs**

```python
try:
    result = 10 / number
except:
    print("Something went wrong")
```

*Why it's wrong:* A bare `except:` catches **every** possible error, including typos and bugs unrelated to the division — making real problems much harder to find.

```python
try:
    result = 10 / number
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("'number' is not defined")
```

**Mistake 2 — Putting too much code inside `try`**

```python
try:
    print("Starting calculation")
    number = int(input())
    result = 100 / number
    print("Done:", result)
except ValueError:
    print("Invalid input")
```

*Why it's wrong:* Wrapping unrelated lines (like the initial `print`) inside `try` makes it unclear exactly which line could fail, and can accidentally swallow errors from code that has nothing to do with the expected risk.

```python
print("Starting calculation")
try:
    number = int(input())
    result = 100 / number
except ValueError:
    print("Invalid input")
    number = None
if number is not None:
    print("Done:", result)
```

**Mistake 3 — Forgetting that `except` needs to match the actual error type**

```python
try:
    number = int("abc")
except ZeroDivisionError:
    print("Conversion failed!")
```

*Why it's wrong:* `int("abc")` raises a `ValueError`, not a `ZeroDivisionError`, so this `except` block never triggers and the program still crashes.

```python
try:
    number = int("abc")
except ValueError:
    print("Conversion failed!")
```

**Mistake 4 — Assuming code after the error in the `try` block still runs**

```python
try:
    print("Step 1")
    x = 1 / 0
    print("Step 2")
except ZeroDivisionError:
    print("Caught the error")
```

*Why it's wrong:* Beginners sometimes expect `"Step 2"` to print anyway — but once an error occurs, Python immediately skips the rest of the `try` block.

```python
# This is actually correct behavior; the key fix is understanding
# that "Step 2" is intentionally skipped, and only "Step 1" and
# "Caught the error" will print.
```

**Mistake 5 — Not using `else` or `finally` when appropriate**

```python
try:
    number = int(input())
except ValueError:
    print("Invalid input")

print("This always runs, even after an error, but should it?")
```

*Why it's wrong:* Code that should only run when there was **no** error (or should run *no matter what*) is often placed carelessly after the `try`/`except`, instead of using `else` (runs only if no error occurred) or `finally` (always runs).

```python
try:
    number = int(input())
except ValueError:
    print("Invalid input")
else:
    print(f"You entered {number}")
finally:
    print("Input attempt finished")
```

## 6. Debugging Practice

**Buggy Program 1:**

```python
try:
    age = int(input())
    print(100 / age)
except:
    print("error")
```

**Buggy Program 2:**

```python
try:
    value = int("42x")
except TypeError:
    print("Conversion failed")
```

**Buggy Program 3:**

```python
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError
    print("Index out of range")
```

### Corrected Versions

**Fix 1:**

```python
try:
    age = int(input())
    print(100 / age)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Age cannot be zero")
```

*Bug:* The bare `except:` hides which specific error occurred, making debugging harder and potentially catching unrelated bugs. *Why the fix works:* Naming the specific exception types gives clearer, more accurate error messages for each distinct failure.

**Fix 2:**

```python
try:
    value = int("42x")
except ValueError:
    print("Conversion failed")
```

*Bug:* Converting a non-numeric string with `int()` raises a `ValueError`, not a `TypeError`, so the `except` clause never matches. *Why the fix works:* Catching the correct exception type lets the handler actually run.

**Fix 3:**

```python
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Index out of range")
```

*Bug:* The `except IndexError` line is missing its colon `:`. *Why the fix works:* Every `except` clause, like every block header in Python, requires a trailing colon.

## 7. Summary

* `try`/`except` lets a program handle errors gracefully instead of crashing.
* As soon as an error occurs inside `try`, Python jumps immediately to a matching `except` — the rest of the `try` block is skipped.
* Always catch **specific** exception types (like `ValueError`, `ZeroDivisionError`) rather than a bare `except:`, so real bugs aren't hidden.
* Multiple `except` clauses can handle different error types differently.
* `else` runs only if no error occurred; `finally` runs no matter what — use them to keep error-handling logic clean and explicit.
* Every `except` clause needs a matching, correctly-named exception type and a trailing colon.
