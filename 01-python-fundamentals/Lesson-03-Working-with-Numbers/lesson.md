# Lesson 03 — Working with Numbers

## 1. Introduction

Almost every useful program does some kind of arithmetic: calculating a total price, computing a percentage, converting units, splitting a bill, or measuring how long something took. Python's numeric operators let you perform these calculations directly in your code, the same way you would on paper — just with a few extra tools, like integer division and the remainder operator, that are especially useful in programming.

Understanding how numbers behave in Python — including a few surprises around division — is essential before you can build anything that calculates real results, from a tip calculator to a physics simulation.

## 2. Conceptual Explanation

Think of Python's numeric operators as a **calculator with extra buttons**. A regular calculator has `+`, `-`, `×`, `÷`. Python has those, plus two extras that regular calculators don't offer directly: **floor division** (division that throws away the remainder) and the **modulo** operator (which gives you *only* the remainder).

These extra operators matter because computers often need to answer questions a plain calculator can't: "How many full boxes of 12 eggs can I make from 50 eggs, and how many are left over?" Floor division answers the first part, modulo answers the second.

```
50 eggs ÷ 12 per box
 →  50 // 12  =  4   (4 full boxes)
 →  50 %  12  =  2   (2 eggs left over)
```

## 3. Diagrams

**Operator overview:**

```
  a = 17,  b = 5

  a + b   →   22        (addition)
  a - b   →   12        (subtraction)
  a * b   →   85        (multiplication)
  a / b   →   3.4       (true division - always returns a float)
  a // b  →   3         (floor division - whole number result)
  a % b   →   2         (modulo - the remainder)
  a ** b  →   1419857   (exponentiation - a to the power of b)
```

**How floor division and modulo relate:**

```
   17 ÷ 5
   ┌───┬───┬───┬───┬───┐
   │ 5 │ 5 │ 5 │ 2 │        17 split into groups of 5
   └───┴───┴───┴───┴───┘
     3 full groups of 5     +     2 left over
     17 // 5 = 3                  17 % 5 = 2
```

**Order of operations (PEMDAS applies):**

```
2 + 3 * 4
      │
      ▼   multiplication happens first
2 + 12  =  14
```

## 4. Three Examples

### Example 1 — Basic arithmetic

**Explanation:** Perform the four basic operations on two numbers.

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

**Expected output:**
```
13
7
30
3.3333333333333335
```

**Walkthrough:** `+`, `-`, and `*` behave as expected. `/` is **true division** — it always returns a `float`, even when the numbers divide evenly, because Python cannot know in advance whether the result will be a whole number.

---

### Example 2 — Floor division, modulo, and exponents

**Explanation:** Show the "extra" operators and how they answer different questions than `/`.

```python
total_minutes = 130

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)

squared = 4 ** 2
cubed = 4 ** 3
print("4 squared:", squared)
print("4 cubed:", cubed)
```

**Expected output:**
```
Hours: 2
Remaining minutes: 10
4 squared: 16
4 cubed: 64
```

**Walkthrough:** `//` gives the whole number of times `60` fits into `130` (2 full hours), and `%` gives what's left over (10 minutes) — together they convert a raw minute count into hours-and-minutes, a very common real-world calculation. `**` raises a number to a power.

---

### Example 3 — A practical example: a restaurant bill splitter

**Explanation:** Calculate a total bill with tax and tip, then split it evenly among a group of friends.

```python
meal_cost = 60.00
tax_rate = 0.08
tip_rate = 0.15
number_of_people = 4

tax = meal_cost * tax_rate
tip = meal_cost * tip_rate
total = meal_cost + tax + tip

per_person = total / number_of_people

print("Meal cost:", meal_cost)
print("Tax:", round(tax, 2))
print("Tip:", round(tip, 2))
print("Total:", round(total, 2))
print("Amount per person:", round(per_person, 2))
```

**Expected output:**
```
Meal cost: 60.0
Tax: 4.8
Tip: 9.0
Total: 73.8
Amount per person: 18.45
```

**Walkthrough:** This combines multiplication (calculating a percentage of a value), addition (building a total), and division (splitting it), plus the built-in `round()` function to keep currency values readable to two decimal places — exactly the kind of calculation a billing app performs.

## 5. Common Mistakes

**Mistake 1 — Expecting `/` to always return a whole number**

```python
result = 10 / 2
print(type(result))
```
Wrong assumption: many beginners expect `5`, an `int`. Python's `/` **always** produces a `float` (`5.0`), regardless of whether the division is even.

Correct (if a whole number is genuinely needed):
```python
result = 10 // 2
print(type(result))   # <class 'int'>
```

**Mistake 2 — Confusing `/` and `//`**

```python
average_speed = 100 // 3   # intended: precise average
```
Wrong because: `//` discards the decimal part, giving `33` instead of the more precise `33.33...`.

Correct:
```python
average_speed = 100 / 3
```

**Mistake 3 — Dividing by zero**

```python
result = 10 / 0
```
Wrong because: division by zero is mathematically undefined, and Python raises a `ZeroDivisionError` rather than silently producing an incorrect value.

Correct: guard the divisor before dividing (using conditionals, covered in a later lesson), or ensure the divisor is never zero in your data.

**Mistake 4 — Ignoring operator precedence**

```python
total = 2 + 3 * 4   # expecting 20
```
Wrong assumption: this actually evaluates to `14`, because multiplication happens before addition (PEMDAS), not left to right blindly.

Correct (if `20` was truly intended):
```python
total = (2 + 3) * 4
```

**Mistake 5 — Mixing up `%` (modulo) with "percent"**

```python
discount = price % 10   # intended: 10% discount
```
Wrong because: `%` is the **remainder** operator, not a percentage calculation; this computes something entirely different from a discount.

Correct:
```python
discount = price * 0.10
```

## 6. Debugging Practice

**Buggy Program 1**
```python
items = 7
boxes = items / 2
print("Full boxes:", boxes)
```

**Buggy Program 2**
```python
price = 50
discount_percent = 20
final_price = price - price % discount_percent
print(final_price)
```

**Buggy Program 3**
```python
a = 5
b = 0
print(a / b)
```

---

**Fixed versions and explanations:**

**Fix 1**
```python
items = 7
boxes = items // 2
print("Full boxes:", boxes)
```
*Bug:* `/` returns `3.5`, which doesn't make sense as a count of "full boxes." *Why the fix works:* `//` performs floor division, giving the whole number of complete boxes (`3`).

**Fix 2**
```python
price = 50
discount_percent = 20
final_price = price - price * (discount_percent / 100)
print(final_price)
```
*Bug:* `%` is the remainder operator, not a percentage calculator, so `price % discount_percent` computes something unrelated to a 20% discount. *Why the fix works:* converting the percentage to a decimal fraction (`discount_percent / 100`) and multiplying by `price` correctly computes the discount amount.

**Fix 3**
```python
a = 5
b = 1
print(a / b)
```
*Bug:* dividing by `0` raises a `ZeroDivisionError`, crashing the program. *Why the fix works:* in this simplified example the divisor is changed to a non-zero value; in a real program you would check the value before dividing (a technique covered once conditionals are introduced).

## 7. Summary

* Python supports `+`, `-`, `*`, `/`, `//`, `%`, and `**` for arithmetic.
* `/` is true division and always returns a `float`; `//` is floor division and discards the remainder.
* `%` (modulo) returns only the remainder of a division — useful for splitting totals into groups.
* `**` raises a number to a power.
* Python follows standard operator precedence (PEMDAS) — multiplication and division happen before addition and subtraction unless parentheses say otherwise.
* Division by zero raises a `ZeroDivisionError`.
* `round()` is a handy built-in for formatting calculated numbers, especially currency.
