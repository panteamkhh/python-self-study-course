# Lesson 02 — Variables and Data Types

## 1. Introduction

A **variable** is a name that refers to a value stored in the computer's memory. Instead of retyping `"Alice"` every time you need a user's name, you store it once under a name like `user_name` and reuse that name throughout your program.

This is one of the most important ideas in programming. Every application you have ever used — a banking app tracking your balance, a game tracking your score, a website remembering your login — relies on variables to hold information while the program runs.

A **data type** describes what kind of value a variable holds — text, a whole number, a decimal number, or a true/false value — because Python needs to know this to decide what operations make sense (you can add two numbers, but adding two pieces of text means something different).

## 2. Conceptual Explanation

Think of computer memory as a wall of **labeled boxes**. A variable is the label on a box, and the value is whatever you put inside. When you write:

```python
age = 25
```

Python creates a box, puts the value `25` inside it, and attaches the label `age` to that box. Later, whenever you write `age`, Python looks up the box with that label and gives you what's inside.

Unlike some languages, Python does not require you to declare a data type in advance — it figures out the type from the value itself. This is called **dynamic typing**. The four data types you'll use constantly from day one are:

* `int` — whole numbers: `7`, `-3`, `1000`
* `float` — decimal numbers: `3.14`, `-0.5`, `100.0`
* `str` — text, wrapped in quotes: `"hello"`, `'Python'`
* `bool` — a truth value: `True` or `False`

## 3. Diagrams

**Variable as a labeled box (memory diagram):**

```
 Variable name        Memory
 ┌──────────┐        ┌───────────────┐
 │   age    │ ─────▶ │      25        │  (type: int)
 └──────────┘        └───────────────┘

 ┌──────────┐        ┌───────────────┐
 │   name   │ ─────▶ │   "Alice"      │  (type: str)
 └──────────┘        └───────────────┘
```

**Reassignment — the label moves, it doesn't merge boxes:**

```
age = 25        age ─────▶ [ 25 ]

age = 26        age ─────▶ [ 26 ]     (the old 25 is discarded)
```

**Type overview:**

```
        Data Types
    ┌───────┬───────┬───────┬────────┐
    │  int  │ float │  str  │  bool  │
    ├───────┼───────┼───────┼────────┤
    │   7   │  3.14 │"hello"│  True  │
    │  -3   │ -0.5  │'Py'   │  False │
    └───────┴───────┴───────┴────────┘
```

## 4. Three Examples

### Example 1 — Storing and printing simple values

**Explanation:** Create one variable of each basic type and print them.

```python
age = 25
height = 1.75
name = "Alice"
is_student = True

print(age)
print(height)
print(name)
print(is_student)
```

**Expected output:**
```
25
1.75
Alice
True
```

**Walkthrough:** Each `=` assigns a value to a name. Python infers the type from the value on the right: `25` becomes an `int`, `1.75` a `float`, `"Alice"` a `str`, and `True` a `bool`.

---

### Example 2 — Checking types and reassigning variables

**Explanation:** Use the built-in `type()` function to inspect a variable's data type, and show that a variable can be reassigned to a new value.

```python
score = 90
print(type(score))

score = "A"          # reassigned - now holds text instead of a number
print(type(score))
print(score)
```

**Expected output:**
```
<class 'int'>
<class 'str'>
A
```

**Walkthrough:** `type()` reveals the current data type of a variable. Because Python is dynamically typed, the same variable name `score` can be reassigned from an `int` to a `str` — the label just moves to point at a new box.

---

### Example 3 — A practical example: a student profile

**Explanation:** Store several related pieces of information about a student, the way a real program (e.g., a school records system) would.

```python
student_name = "Maria Lopez"
student_id = 10432
gpa = 3.8
is_enrolled = True

print("Student Profile")
print("Name:", student_name)
print("ID:", student_id)
print("GPA:", gpa)
print("Currently enrolled:", is_enrolled)
```

**Expected output:**
```
Student Profile
Name: Maria Lopez
ID: 10432
GPA: 3.8
Currently enrolled: True
```

**Walkthrough:** `print()` can accept multiple comma-separated arguments; it prints each one separated by a space. This pattern — several typed variables describing one real-world entity — is the foundation of almost every data-driven program you will write.

## 5. Common Mistakes

**Mistake 1 — Using quotes around a number you intend to calculate with**

```python
age = "25"
next_year_age = age + 1
```
Wrong because: `"25"` is a string, not a number, and Python cannot add an `int` to a `str`. This raises a `TypeError`.

Correct:
```python
age = 25
next_year_age = age + 1
```

**Mistake 2 — Starting a variable name with a number**

```python
1st_place = "Alice"
```
Wrong because: Python variable names cannot start with a digit. This raises a `SyntaxError`.

Correct:
```python
first_place = "Alice"
```

**Mistake 3 — Using a variable before it is assigned**

```python
print(total)
total = 0
```
Wrong because: Python executes top to bottom; `total` does not exist yet on the first line, causing a `NameError`.

Correct:
```python
total = 0
print(total)
```

**Mistake 4 — Confusing `=` (assignment) with equality**

```python
if x = 5:
    print("x is five")
```
Wrong because: a single `=` assigns a value; comparing for equality requires `==`. This raises a `SyntaxError`.

Correct:
```python
if x == 5:
    print("x is five")
```

**Mistake 5 — Case-sensitivity mistakes**

```python
Name = "Alice"
print(name)
```
Wrong because: Python is case-sensitive, so `Name` and `name` are two completely different variables; the second one was never created, causing a `NameError`.

Correct:
```python
Name = "Alice"
print(Name)
```

## 6. Debugging Practice

**Buggy Program 1**
```python
quantity = "5"
price = 2.5
total = quantity * price
print(total)
```

**Buggy Program 2**
```python
2nd_score = 88
print(2nd_score)
```

**Buggy Program 3**
```python
temperature = 72
print(Temperature)
```

---

**Fixed versions and explanations:**

**Fix 1**
```python
quantity = 5
price = 2.5
total = quantity * price
print(total)
```
*Bug:* `quantity` was stored as the string `"5"` instead of the number `5`, so `quantity * price` does not perform arithmetic the way a store's checkout calculation needs. *Why the fix works:* storing `5` as an `int` lets Python multiply it with the `float` price as expected.

**Fix 2**
```python
second_score = 88
print(second_score)
```
*Bug:* the variable name `2nd_score` starts with a digit, which Python's naming rules forbid. *Why the fix works:* renaming it to start with a letter (`second_score`) satisfies the rule.

**Fix 3**
```python
temperature = 72
print(temperature)
```
*Bug:* the variable was created as `temperature` (lowercase) but referenced as `Temperature` (capital T); Python treats these as two different names. *Why the fix works:* using the exact same casing that was used at creation lets Python find the variable.

## 7. Summary

* A variable is a name attached to a value stored in memory; assignment uses `=`.
* Python is dynamically typed — it infers a variable's type from its value, and that type can change on reassignment.
* The four core data types introduced today: `int`, `float`, `str`, `bool`.
* `type()` reveals a variable's current data type.
* Variable names are case-sensitive, cannot start with a digit, and must exist before they are used.
* `=` assigns a value; `==` (covered later) compares two values for equality — they are not interchangeable.
