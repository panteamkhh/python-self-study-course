# Lesson 08 — Exercises: Arguments and Scope

## Easy

1. Write a function `power(base, exponent=2)` that returns `base` raised to `exponent`, defaulting to squaring if no exponent is given.
2. Write a function `full_name(first, last)` and call it once using positional arguments and once using keyword arguments.
3. Write a function that creates a local variable, then explain (in a comment) why trying to print that variable outside the function fails.

## Medium

4. Write a function `apply_discount(price, discount=0.1)` that returns the price after applying a discount (default 10%).
5. Write a function `sum_all(*numbers)` that accepts any number of arguments and returns their sum.
6. Write a function `update_counter()` that increments a global variable `counter` by 1 each time it's called, using the `global` keyword correctly.
7. Write a function `safe_append(item, collection=None)` that correctly avoids the mutable default argument bug when appending `item` to a list.

## Hard

8. Read a count `n`, then read `n` numbers. Pass them all to a function `average(*values)` using unpacking, and print the result formatted to 2 decimal places.
9. Write a function `make_multiplier(factor)` that returns another function, which when called with a number, multiplies it by `factor`. (This introduces closures — variables remembered from the enclosing scope.)
10. Write a function `describe_person(name, age, **details)` that accepts any number of extra keyword arguments (like `city="Tehran"`) and prints them all alongside `name` and `age`.
