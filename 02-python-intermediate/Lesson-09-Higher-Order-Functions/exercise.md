# Lesson 09 — Exercises: Higher-Order Functions

## Easy

1. Write a lambda that takes a number and returns its square.
2. Write a lambda that takes two numbers and returns the larger one.
3. Given a list of words, use `sorted()` to sort them by length (shortest first).

## Medium

4. Given a list of tuples `(name, age)`, sort them by age in ascending order using a lambda key.
5. Write a function `apply_operation(func, a, b)` that takes a function and two numbers, and returns the result of calling `func(a, b)`.
6. Given a list of prices, use `sorted()` with `reverse=True` to sort them from most expensive to cheapest.
7. Given a list of strings, sort them by the number of vowels each contains, using a lambda key.

## Hard

8. Write a function `make_power(exponent)` that returns a lambda which raises any given number to that exponent.
9. Given a list of dictionaries, each representing a product with `"name"` and `"price"` keys, sort the list by price using a lambda key that accesses the dictionary.
10. Read a count `n`, then read `n` lines each containing a name and a score. Sort by score descending, and if two students have the same score, break the tie alphabetically by name. Print only the names, one per line.
