# Lesson 10 — Quiz: Try and Except

## Multiple Choice Questions

1. What is the purpose of a `try`/`except` block?
   a) To make code run faster
   b) To handle errors gracefully instead of crashing
   c) To repeat code multiple times
   d) To define a new function

2. What error does `int("abc")` raise?
   a) `TypeError`
   b) `ZeroDivisionError`
   c) `ValueError`
   d) `IndexError`

3. What error does dividing by zero raise?
   a) `ValueError`
   b) `ZeroDivisionError`
   c) `KeyError`
   d) `IndexError`

4. What error occurs when accessing a list index that doesn't exist?
   a) `KeyError`
   b) `IndexError`
   c) `ValueError`
   d) `TypeError`

5. What error occurs when accessing a missing dictionary key?
   a) `KeyError`
   b) `IndexError`
   c) `ValueError`
   d) `NameError`

6. What happens to the remaining lines in a `try` block after an error occurs?
   a) They still run normally
   b) They are skipped immediately
   c) They run after the `except` block
   d) They cause a second error

7. Why is a bare `except:` generally discouraged?
   a) It's slower than naming exceptions
   b) It catches every error, hiding real bugs
   c) It's not valid Python syntax
   d) It only works with `ValueError`

8. When does the `else` clause of a `try` statement run?
   a) Only if an exception was raised
   b) Only if no exception was raised
   c) Always, regardless of an exception
   d) Never — `else` is not valid with `try`

9. When does the `finally` clause run?
   a) Only if an exception was raised
   b) Only if no exception was raised
   c) Always, regardless of whether an exception occurred
   d) Only when explicitly called

10. What is wrong with `except IndexError` (no colon) as a line of code?
    a) Nothing, it's valid
    b) It's missing a required colon
    c) `IndexError` should be lowercase
    d) `except` cannot be followed by an exception name

## True/False Questions

1. A bare `except:` catches every type of error.
2. Code after the line that raised an error inside `try` continues to execute normally.
3. `finally` only runs if an exception occurred.
4. Multiple `except` clauses can handle different exception types differently.
5. `else` in a `try` statement runs only when no exception was raised.

## Short Answer Questions

1. What is the purpose of `try`/`except` in a program?
2. Why should you avoid a bare `except:` in most cases?
3. What is the difference between `else` and `finally` in a `try` statement?
4. Give an example of a situation where `ValueError` would be raised.
5. Explain, in your own words, why catching the exact exception type matters instead of catching everything generically.

---

## Answer Key

**Multiple Choice:** 1-b, 2-c, 3-b, 4-b, 5-a, 6-b, 7-b, 8-b, 9-c, 10-b

**True/False:** 1-True, 2-False, 3-False, 4-True, 5-True

**Short Answer (sample answers):**

1. It lets a program detect and respond to runtime errors gracefully, instead of crashing entirely.
2. A bare `except:` catches every kind of error, including unrelated bugs and typos, which makes real problems much harder to diagnose.
3. `else` runs only when the `try` block completes without raising any exception; `finally` runs no matter what, whether or not an exception occurred.
4. Trying to convert a non-numeric string to an integer or float, such as `int("hello")`.
5. Catching the exact exception type ensures the handler responds specifically to the expected problem, while letting unrelated, unexpected errors surface clearly instead of being silently swallowed.
