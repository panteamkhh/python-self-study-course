# Lesson 14 — Exercises: Generators and Yield

## Easy

1. Write a generator function `count_up_to(n)` that yields numbers from `1` up to and including `n`. Print all values using a `for` loop.

2. Write a generator function `squares(n)` that yields the square of each number from `1` to `n`. Print all values.

3. Write a generator function `first_n_letters(n)` that yields the first `n` letters of the alphabet (`"a"`, `"b"`, `"c"`, ...). Print all values.

## Medium

4. Write a generator function `even_up_to(n)` that yields only even numbers from `0` up to `n`. Use it to print the first 4 even numbers up to `20` with `next()`.

5. Write a generator function `countdown(n)` that yields numbers from `n` down to `1`, then yields the string `"Liftoff!"` as the very last value.

6. Write a generator function `fibonacci(limit)` that yields Fibonacci numbers (`0, 1, 1, 2, 3, 5, ...`) up to (but not exceeding) `limit`.

7. Write a generator function `filter_long_words(words, min_length)` that takes a list of strings and yields only the words with length greater than or equal to `min_length`.

## Hard

8. Write a generator function `paginate(items, page_size)` that yields successive "pages" (lists) of `page_size` items at a time from a longer list. (For example, with `page_size=3`, a list of 7 items yields 3 pages: sizes 3, 3, 1.)

9. Write a generator function `unique_values(items)` that yields each value from a list only the first time it appears, skipping duplicates, without converting the whole list to a `set` first (track seen values manually as you go).

10. Write a generator function `simulate_todo_stream(tasks)` that takes a list of task dictionaries like `{"name": "Buy milk", "done": False}` and yields only the names of tasks that are **not** done, one at a time. Then write a second generator `mark_all_done(tasks)` that yields each task dictionary after setting `"done": True` on it (mutating and yielding the same dictionaries).
