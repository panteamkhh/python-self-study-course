# Lesson 15 — Exercises: Generator Expressions

## Easy

1. Given `numbers = [1, 2, 3, 4, 5]`, write a generator expression that yields each number doubled. Print all values using a `for` loop.

2. Given `words = ["hi", "hello", "hey"]`, write a generator expression that yields the length of each word. Print all values.

3. Write a generator expression that yields numbers from `1` to `10` (inclusive) that are divisible by `3`. Print all values.

## Medium

4. Given `temps_celsius = [0, 20, 37, 100]`, write a generator expression that converts each to Fahrenheit (`C * 9/5 + 32`), and pass it directly into `max()` to find the highest Fahrenheit value.

5. Given `prices = [12.5, 45.0, 3.75, 89.99, 20.0]`, use a generator expression combined with `sum()` to compute the total of only the prices greater than `15`.

6. Given `names = ["Alice", "bob", "Charlie", "dave"]`, write a generator expression that yields only the names starting with an uppercase letter (hint: use `name[0].isupper()`). Print all values.

7. Given a list of dictionaries representing an inventory, e.g. `[{"item": "Pen", "qty": 5}, {"item": "Book", "qty": 0}]`, write a generator expression that yields the `"item"` names where `"qty"` is greater than `0`.

## Hard

8. Given `sentences = ["I love Python", "Generators are fast", "Lists use more memory"]`, write a generator expression that yields the number of words in each sentence (hint: `len(sentence.split())`). Use `sum()` to compute the total word count across all sentences in one line.

9. Given `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` (a list of lists), write a generator expression that yields the sum of each row. Print all row sums.

10. Given `users = [{"name": "Ana", "active": True}, {"name": "Leo", "active": False}, {"name": "Sam", "active": True}]`, write one line using a generator expression and `sum()` to count how many users are active (hint: summing `True`/`False` values works because `True` equals `1` and `False` equals `0`). Then, separately, write a generator expression that yields only the names of active users, and convert it to a list.
