# Lesson 10 — Exercises: Try and Except

## Easy

1. Write code that attempts to convert the string `"hello"` to an integer, catching the `ValueError` and printing `"Not a number"`.
2. Write code that attempts to divide `10` by `0`, catching the `ZeroDivisionError` and printing `"Cannot divide by zero"`.
3. Write code that attempts to access index `10` of a 3-item list, catching the `IndexError` and printing `"Index out of range"`.

## Medium

4. Write a function `safe_int(text)` that tries to convert `text` to an integer and returns `None` if it fails, instead of crashing.
5. Write a function `safe_divide(a, b)` that returns the division result, or the string `"undefined"` if dividing by zero.
6. Write code that reads a dictionary key that might not exist, catching the resulting `KeyError` and printing `"Key not found"`.
7. Write a `try`/`except`/`else` block that prints `"Success"` only if converting a given string to a float succeeds.

## Hard

8. Write a function `parse_numbers(values)` that takes a list of strings, attempts to convert each to an integer, and returns a list of only the ones that succeeded (skipping invalid ones silently using `try`/`except` inside a loop).
9. Write a program that reads two numbers from input and divides them, but handles **both** possible errors: invalid input (`ValueError`) and division by zero (`ZeroDivisionError`), each with its own distinct message.
10. Write a function `safe_lookup(data, key)` where `data` is a dictionary, that returns the value for `key` if it exists, or `"missing"` if it raises a `KeyError`, using `try`/`except`/`finally` where the `finally` block prints `"Lookup attempted"` every time, regardless of the outcome.
