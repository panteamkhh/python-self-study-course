# Lesson 04 — Type Conversion

## 1. Introduction

Data doesn't always arrive in the type your program needs. A web form gives you every field as text, even a field labeled "age." A file on disk stores everything as text too. Before you can do arithmetic with a number that arrived as text, you must **convert** it to a numeric type — and sometimes you need to go the other way, turning a number into text so it can be combined with other text for display.

This is called **type conversion** (or **type casting**), and it is one of the most common operations in real software: reading user input, parsing files, formatting reports, and preparing data for calculations all depend on it.

## 2. Conceptual Explanation

Think of type conversion like **currency exchange**. The value `"100"` (a string) and the value `100` (an integer) represent the same idea to a human, but Python treats them as fundamentally different kinds of things — the way US dollars and Japanese yen are both "money" but cannot be added together directly. You must explicitly convert one into the other's "currency" before combining them.

Python provides built-in conversion functions, each named after the type it produces:

* `int(x)` — converts `x` to an integer
* `float(x)` — converts `x` to a decimal number
* `str(x)` — converts `x` to text
* `bool(x)` — converts `x` to `True` or `False`

Not every conversion is possible: `int("hello")` fails, because `"hello"` cannot be interpreted as a number. Python raises a `ValueError` when a conversion doesn't make sense.

## 3. Diagrams

**Conversion flow:**

```
   "42"   (str)
     │
     │  int("42")
     ▼
    42    (int)
     │
     │  float(42)
     ▼
   42.0   (float)
     │
     │  str(42.0)
     ▼
  "42.0"  (str)
```

**What can convert to what (common cases):**

```
            int()        float()       str()
  "42"   →   42            42.0        (already str)
  3.9    →   3          (already f)     "3.9"
  True   →   1            1.0          "True"
  "abc"  →  ValueError!  ValueError!    (already str)
```

## 4. Three Examples

### Example 1 — Converting user-style text input to numbers

**Explanation:** Simulate data that arrived as text (as it always does from `input()`) and convert it for arithmetic.

```python
age_text = "28"
age_number = int(age_text)

next_year = age_number + 1
print(next_year)
print(type(age_number))
```

**Expected output:**
```
29
<class 'int'>
```

**Walkthrough:** `age_text` starts as a `str`. `int()` converts it into a real integer, which can then be used in arithmetic like `+ 1`.

---

### Example 2 — Building a message that mixes numbers and text

**Explanation:** `print()` can take multiple comma-separated values of different types directly, but combining them into a single string with `+` requires converting numbers to text first.

```python
score = 87
message = "Your score is " + str(score) + " points."
print(message)

pi_value = 3.14159
label = "Pi is approximately " + str(round(pi_value, 2))
print(label)
```

**Expected output:**
```
Your score is 87 points.
Pi is approximately 3.14
```

**Walkthrough:** The `+` operator between strings performs **concatenation** (joining text), but it only works if every piece being joined is already a string — hence wrapping `score` and the rounded `pi_value` in `str()`.

---

### Example 3 — A practical example: parsing form-style data

**Explanation:** Simulate values exactly as they would arrive from a web form (always text) and convert each into the type it should really be.

```python
form_age = "34"
form_height = "1.82"
form_subscribed = "True"

age = int(form_age)
height = float(form_height)
subscribed = form_subscribed == "True"   # manual boolean check, see note below

print("Age:", age, type(age))
print("Height:", height, type(height))
print("Subscribed:", subscribed, type(subscribed))
```

**Expected output:**
```
Age: 34 <class 'int'>
Height: 1.82 <class 'float'>
Subscribed: True <class 'bool'>
```

**Walkthrough:** `int()` and `float()` convert numeric-looking text directly. Converting text to a *meaningful* boolean is trickier than the other conversions — `bool("False")` would actually return `True`, because any non-empty string is "truthy." The reliable approach is to compare the text against the expected value, as shown, which produces a genuine `bool` result.

## 5. Common Mistakes

**Mistake 1 — Trying to add a string and a number directly**

```python
age = "25"
next_year = age + 1
```
Wrong because: Python cannot combine a `str` and an `int` with `+`; it raises a `TypeError`.

Correct:
```python
age = int("25")
next_year = age + 1
```

**Mistake 2 — Forgetting to convert a number before concatenating text**

```python
score = 95
message = "Score: " + score
```
Wrong because: `+` between a `str` and an `int` is not allowed, raising a `TypeError`.

Correct:
```python
score = 95
message = "Score: " + str(score)
```

**Mistake 3 — Assuming `bool("False")` gives `False`**

```python
flag = bool("False")
print(flag)
```
Wrong assumption: this prints `True`, because any non-empty string (including the text `"False"`) is considered "truthy" by `bool()`.

Correct (compare the text explicitly):
```python
flag = "False" == "True"   # evaluates the intended meaning, gives False
print(flag)
```

**Mistake 4 — Converting text that isn't a valid number**

```python
quantity = int("twelve")
```
Wrong because: `int()` can only convert digit-based text like `"12"`; it does not understand number words, raising a `ValueError`.

Correct:
```python
quantity = int("12")
```

**Mistake 5 — Losing precision by converting float to int carelessly**

```python
price = 9.99
whole_price = int(price)
print(whole_price)
```
Wrong assumption: many beginners expect rounding, but `int()` **truncates** — it simply cuts off the decimal part, giving `9`, not `10`.

Correct (if rounding is intended):
```python
price = 9.99
whole_price = round(price)
print(whole_price)
```

## 6. Debugging Practice

**Buggy Program 1**
```python
quantity = "4"
price = 2.5
total = quantity * price
print(total)
```

**Buggy Program 2**
```python
count = 12
message = "Total items: " + count
print(message)
```

**Buggy Program 3**
```python
user_input = "abc"
number = int(user_input)
print(number)
```

---

**Fixed versions and explanations:**

**Fix 1**
```python
quantity = int("4")
price = 2.5
total = quantity * price
print(total)
```
*Bug:* `quantity` was a string, and multiplying a string by a float is not defined the way this program intended (it would actually raise a `TypeError` here since `price` is a float, not an int). *Why the fix works:* converting `quantity` to an `int` first allows normal numeric multiplication.

**Fix 2**
```python
count = 12
message = "Total items: " + str(count)
print(message)
```
*Bug:* string concatenation with `+` requires both sides to be strings; `count` is an `int`. *Why the fix works:* `str(count)` converts the number to text so it can be joined with the rest of the sentence.

**Fix 3**
```python
user_input = "12"
number = int(user_input)
print(number)
```
*Bug:* `"abc"` cannot be interpreted as a number, so `int()` raises a `ValueError`. *Why the fix works:* using text that genuinely represents a number allows the conversion to succeed. (In real programs, this situation is normally handled by validating input before conversion — a technique that becomes more powerful once conditionals are introduced.)

## 7. Summary

* Type conversion (casting) changes a value from one data type to another using `int()`, `float()`, `str()`, or `bool()`.
* String concatenation with `+` requires every piece to already be a `str` — convert numbers with `str()` first.
* `int()` on a float **truncates** the decimal part rather than rounding; use `round()` if rounding is intended.
* `bool()` on any non-empty string returns `True`, even `bool("False")` — comparing text directly is the reliable way to interpret a yes/no string.
* Converting text that doesn't represent a valid number (e.g., `int("abc")`) raises a `ValueError`.
* Data from external sources (forms, files, user input) usually arrives as text and must be deliberately converted before use.
