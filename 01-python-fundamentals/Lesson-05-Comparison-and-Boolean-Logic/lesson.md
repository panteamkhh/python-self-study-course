# Lesson 05 — Comparison and Boolean Logic

## 1. Introduction

Every program that makes a decision — "is this password correct," "is the cart total over the free-shipping threshold," "has the user reached the minimum age" — relies on **comparisons** that produce a `True` or `False` answer. Today's lesson builds the foundation for tomorrow's `if` statements: before a program can decide *what to do*, it must be able to ask a *yes/no question* and get a reliable answer.

This is used everywhere: login systems checking a password, e-commerce sites checking stock levels, games checking whether a player's health has hit zero.

## 2. Conceptual Explanation

Think of a comparison operator as a **yes/no question you ask Python**. `age >= 18` is Python's way of asking, "Is `age` greater than or equal to 18?" The answer is always one of exactly two values: `True` or `False` — a `bool`, the data type you met in Lesson 02.

Python's comparison operators:

* `==` equal to
* `!=` not equal to
* `>` greater than
* `<` less than
* `>=` greater than or equal to
* `<=` less than or equal to

Once you have several `True`/`False` answers, **boolean operators** combine them into a single answer:

* `and` — `True` only if **both** sides are `True`
* `or` — `True` if **at least one** side is `True`
* `not` — flips `True` to `False` and vice versa

## 3. Diagrams

**Comparison produces a bool:**

```
   age = 20

   age >= 18
     │
     ▼
   True     (a bool value, ready to be used in a decision)
```

**Truth tables for `and` / `or`:**

```
   A      B      A and B      A or B
 True   True      True         True
 True   False     False        True
 False  True      False        True
 False  False     False        False
```

**`not` flips the value:**

```
   not True   →  False
   not False  →  True
```

**Combining conditions visually:**

```
   is_adult (True)  ──┐
                       ├── and ──▶  True
   has_ticket (True) ──┘
```

## 4. Three Examples

### Example 1 — Basic comparisons

**Explanation:** Compare two numbers with every comparison operator.

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(b <= 20)
```

**Expected output:**
```
False
True
False
True
True
True
```

**Walkthrough:** Each line asks a yes/no question about `a` and `b`, and Python answers with `True` or `False` based on the actual values (`10` and `20`).

---

### Example 2 — Combining conditions with `and`, `or`, `not`

**Explanation:** Check eligibility for a discount that requires being a student **and** at least 18, or use `or` for an alternative qualifying condition.

```python
age = 20
is_student = True
has_coupon = False

qualifies_for_discount = is_student and age >= 18
print(qualifies_for_discount)

gets_free_shipping = has_coupon or age >= 18
print(gets_free_shipping)

is_minor = not (age >= 18)
print(is_minor)
```

**Expected output:**
```
True
True
False
```

**Walkthrough:** `and` requires both `is_student` and `age >= 18` to be `True`. `or` only needs one side to be `True` — here `age >= 18` alone makes the whole expression `True` even though `has_coupon` is `False`. `not` reverses the result of `age >= 18` (which is `True`), giving `False`.

---

### Example 3 — A practical example: a simple login check

**Explanation:** Compare user-entered credentials against stored values — the core operation behind every login form.

```python
stored_username = "admin"
stored_password = "secure123"

entered_username = "admin"
entered_password = "secure123"

username_correct = entered_username == stored_username
password_correct = entered_password == stored_password

login_successful = username_correct and password_correct
print("Login successful:", login_successful)

wrong_password_attempt = "wrongpass"
password_correct_2 = wrong_password_attempt == stored_password
print("Second attempt correct:", password_correct_2)
```

**Expected output:**
```
Login successful: True
Second attempt correct: False
```

**Walkthrough:** `==` compares the entered text against the stored text exactly. `login_successful` is only `True` when **both** the username and password checks pass, which is exactly the logic behind real authentication systems (though real systems never store or compare raw passwords like this — they use secure hashing).

## 5. Common Mistakes

**Mistake 1 — Using `=` instead of `==` to compare**

```python
if age = 18:
    print("Exactly 18")
```
Wrong because: `=` is assignment, not comparison; this raises a `SyntaxError`.

Correct:
```python
if age == 18:
    print("Exactly 18")
```

**Mistake 2 — Writing a chained comparison the way it might be spoken aloud**

```python
is_valid = age > 0 and < 120
```
Wrong because: `< 120` on its own is not a complete comparison; Python needs `age` repeated on both sides.

Correct:
```python
is_valid = age > 0 and age < 120
```

**Mistake 3 — Confusing `and` with `or` (over-restricting a condition)**

```python
is_weekend = day == "Saturday" and day == "Sunday"
```
Wrong because: `day` cannot equal both `"Saturday"` and `"Sunday"` at the same time, so this is always `False`.

Correct:
```python
is_weekend = day == "Saturday" or day == "Sunday"
```

**Mistake 4 — Comparing values of incompatible types and expecting a crash**

```python
result = "5" == 5
print(result)
```
Wrong assumption: some beginners expect an error here; Python actually allows this comparison and simply returns `False`, because a string and an integer are never considered equal, no matter their content.

Correct usage (convert first if you intend a numeric comparison):
```python
result = int("5") == 5
print(result)   # True
```

**Mistake 5 — Forgetting that `not` applies to the whole expression that follows**

```python
result = not age >= 18 and is_member
```
Wrong assumption: due to operator precedence, `not` binds tightly to `age >= 18` only, not the entire expression, which can produce unexpected results if you intended `not` to apply to everything.

Correct (use parentheses to make intent explicit):
```python
result = not (age >= 18 and is_member)
```

## 6. Debugging Practice

**Buggy Program 1**
```python
age = 25
if age = 25:
    print("Quarter of a century")
```

**Buggy Program 2**
```python
ticket_type = "VIP"
is_general_and_vip = ticket_type == "General" and ticket_type == "VIP"
print(is_general_and_vip)
```

**Buggy Program 3**
```python
score = "85"
passed = score >= 60
print(passed)
```

---

**Fixed versions and explanations:**

**Fix 1**
```python
age = 25
if age == 25:
    print("Quarter of a century")
```
*Bug:* `=` is assignment, not comparison, so Python raises a `SyntaxError` inside the `if`. *Why the fix works:* `==` performs the intended equality check.

**Fix 2**
```python
ticket_type = "VIP"
is_general_or_vip = ticket_type == "General" or ticket_type == "VIP"
print(is_general_or_vip)
```
*Bug:* `and` requires `ticket_type` to equal both `"General"` and `"VIP"` simultaneously, which is impossible, so the expression is always `False`. *Why the fix works:* `or` correctly checks whether `ticket_type` matches **either** value.

**Fix 3**
```python
score = int("85")
passed = score >= 60
print(passed)
```
*Bug:* `score` is a string, and comparing a string to an integer with `>=` raises a `TypeError` (unlike `==`, which is always allowed between different types, ordering comparisons like `>=` are not). *Why the fix works:* converting `score` to an `int` first allows a valid numeric comparison.

## 7. Summary

* Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) always produce a `bool`: `True` or `False`.
* `and` requires both conditions to be `True`; `or` requires at least one; `not` flips a boolean value.
* `=` assigns a value, `==` compares two values — mixing them up is one of the most common beginner errors.
* Comparing values of different types with `==`/`!=` is always allowed (and usually gives `False`), but ordering comparisons like `>=` between incompatible types raise a `TypeError`.
* Use parentheses to make the intended grouping of `and`, `or`, and `not` explicit, especially when mixing all three.
* These boolean results are the foundation for the `if` statements introduced in the next lesson.
