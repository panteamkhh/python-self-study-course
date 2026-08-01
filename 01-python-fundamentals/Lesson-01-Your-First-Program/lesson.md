# Lesson 01 — Your First Program

## 1. Introduction

A **program** is a sequence of instructions that a computer executes, one after another, to produce a result. Python is a language for writing those instructions in a form that is close to plain English, which is why it is one of the most common first languages for new programmers and one of the most used languages in the industry — from web backends (Django, FastAPI) to data science (pandas, NumPy) to automation scripts that save people hours of manual work every day.

Every Python journey starts with the same instruction: printing text to the screen. It looks trivial, but it teaches the two things every program needs — **input/output** (getting information out where a human can see it) and **syntax** (the exact rules Python requires you to follow).

Real-world uses of `print`:

* Displaying results to a user (a receipt total, a converted temperature, a game score).
* Debugging — printing intermediate values to see what a program is doing.
* Logging — writing status messages while a long-running program executes.

## 2. Conceptual Explanation

Think of a Python program as a **recipe card**. Each line is one instruction, and the "chef" (the Python interpreter) reads it top to bottom, performing each step exactly as written, in order, without skipping ahead. If a line says "add salt," the chef doesn't wonder whether you meant sugar — it does precisely what the line says.

The interpreter is the program that reads your `.py` file and carries out its instructions. When you run:

```bash
python3 main.py
```

Python reads `main.py` from the first line to the last line and executes each one.

The simplest instruction you can give the interpreter is: *show this text on the screen*. In Python, that instruction is the `print()` **function**. A function is a named, reusable action — `print` is a function built into Python that takes whatever you put between its parentheses and displays it.

```
print("Hello, World!")
  |        |
  |        └── the argument: what to display
  └── the function name: the action to perform
```

## 3. Diagrams

**Execution flow of a one-line program:**

```
 ┌────────────────────────┐
 │  main.py                │
 │  print("Hello, World!") │
 └────────────┬────────────┘
              │  interpreter reads the line
              ▼
 ┌────────────────────────┐
 │   Python interpreter    │
 │  runs the print function│
 └────────────┬────────────┘
              │  sends text to output
              ▼
 ┌────────────────────────┐
 │   Terminal / Console    │
 │   Hello, World!          │
 └────────────────────────┘
```

**Multi-line program flow (top to bottom, no skipping):**

```
Line 1: print("Starting program...")   ──▶ runs first
Line 2: print("Calculating...")        ──▶ runs second
Line 3: print("Done!")                 ──▶ runs third
```

## 4. Three Examples

### Example 1 — A single greeting

**Explanation:** The smallest possible Python program: print one line of text.

```python
print("Hello, World!")
```

**Expected output:**
```
Hello, World!
```

**Walkthrough:** Python sees `print(...)`, recognizes it as a call to the built-in `print` function, and sends everything inside the parentheses — the text `"Hello, World!"` — to the screen, followed automatically by a new line.

---

### Example 2 — Multiple lines and comments

**Explanation:** Programs are usually more than one line, and comments let you leave notes for yourself that Python ignores.

```python
# This program introduces the user to the course
print("Welcome to Python Fundamentals!")
print("Today, you will write your very first program.")
print("Let's get started.")
```

**Expected output:**
```
Welcome to Python Fundamentals!
Today, you will write your very first program.
Let's get started.
```

**Walkthrough:** The line starting with `#` is a **comment** — Python skips it entirely; it exists only for humans reading the code. The three `print` calls execute in order, each producing its own line of output.

---

### Example 3 — A practical example: a startup banner

**Explanation:** Real programs often print a small "banner" when they start, showing the program's name and version — something you'll see in command-line tools you use every day.

```python
# Startup banner for a fictional command-line tool
print("========================================")
print(" TaskRunner CLI - version 1.0")
print("========================================")
print("Type 'taskrunner --help' to see available commands.")
```

**Expected output:**
```
========================================
 TaskRunner CLI - version 1.0
========================================
Type 'taskrunner --help' to see available commands.
```

**Walkthrough:** Each `print` call is independent and produces exactly one line. Stacking simple `print` calls is how real tools build multi-line console output — there is no special "banner" feature, just repeated use of the same function.

## 5. Common Mistakes

**Mistake 1 — Forgetting quotation marks around text**

```python
print(Hello, World!)
```
Wrong because: Python interprets `Hello` and `World` as **names** (identifiers), not text, and it doesn't understand the punctuation either. This raises a `SyntaxError`.

Correct:
```python
print("Hello, World!")
```

**Mistake 2 — Mismatched quotes**

```python
print("Hello, World!')
```
Wrong because: the string must start and end with the *same* type of quote character. Python cannot tell where the text ends.

Correct:
```python
print("Hello, World!")
```

**Mistake 3 — Forgetting the parentheses**

```python
print "Hello, World!"
```
Wrong because: in modern Python (Python 3), `print` is a function and every function call requires parentheses. This syntax is left over from Python 2 and no longer works.

Correct:
```python
print("Hello, World!")
```

**Mistake 4 — Incorrect indentation**

```python
    print("Hello, World!")
```
Wrong because: Python uses indentation (spacing) to define blocks of code (you'll see this with loops and conditionals later). An indented line with nothing above it that expects an indented block causes an `IndentationError`.

Correct:
```python
print("Hello, World!")
```

**Mistake 5 — Expecting `print` to return a usable value**

```python
result = print("Hello, World!")
print(result * 2)
```
Wrong because: `print` displays text but its return value is always `None` (Python's "nothing" value). You cannot multiply `None`.

Correct:
```python
message = "Hello, World!"
print(message)
print(message * 2)  # repeats the string itself, not the print output
```

## 6. Debugging Practice

**Buggy Program 1**
```python
print(Welcome to the course)
```

**Buggy Program 2**
```python
print("Line one")
  print("Line two")
```

**Buggy Program 3**
```python
print('It's a great day to learn Python')
```

---

**Fixed versions and explanations:**

**Fix 1**
```python
print("Welcome to the course")
```
*Bug:* Text wasn't wrapped in quotes, so Python tried to read `Welcome`, `to`, `the`, `course` as separate names. *Why the fix works:* wrapping the words in quotes tells Python this is a string (text), not code to evaluate.

**Fix 2**
```python
print("Line one")
print("Line two")
```
*Bug:* The second line had extra leading spaces, and Python does not expect an indented line here (there is no loop, function, or conditional starting above it), causing an `IndentationError`. *Why the fix works:* removing the unnecessary indentation puts both statements at the same level, which Python expects for a plain sequence of instructions.

**Fix 3**
```python
print("It's a great day to learn Python")
```
*Bug:* Using single quotes to wrap the string while the text itself contains an apostrophe closes the string early at `It'`, then confuses Python with the leftover text. *Why the fix works:* switching the outer quotes to double quotes lets the apostrophe inside be treated as ordinary text instead of a string terminator.

## 7. Summary

* A Python program is a list of instructions executed one line at a time, from top to bottom.
* `print()` is a built-in function that displays text (and other values) on the screen.
* Text values must be wrapped in matching quotes (`"..."` or `'...'`) — this is called a **string**.
* Lines starting with `#` are comments: notes for humans that Python ignores.
* Python 3 requires parentheses for every function call, including `print()`.
* Indentation matters in Python — extra spaces where none are expected cause errors.
* `print()` always returns `None`; it displays a value but does not hand one back to your code.
