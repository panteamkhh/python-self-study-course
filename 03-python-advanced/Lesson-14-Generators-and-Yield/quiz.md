# Lesson 14 — Quiz: Generators and Yield

## Multiple Choice (10)

1. What keyword turns a regular function into a generator?
   a) `return`
   b) `yield`
   c) `generate`
   d) `pause`

2. What is the main advantage of a generator over building a full list?
   a) Generators run code faster
   b) Generators use much less memory by producing values on demand
   c) Generators can only hold numbers
   d) Generators automatically sort their values

3. What happens when a generator function is called (e.g. `gen = my_generator()`)?
   a) The function body runs immediately
   b) A generator object is created, but the body hasn't run yet
   c) It raises an error unless used in a loop
   d) It returns a list

4. What does `next(gen)` do?
   a) Restarts the generator from the beginning
   b) Runs the generator until the next `yield` and returns that value
   c) Deletes the generator
   d) Converts the generator into a list

5. What is raised when a generator has no more values to produce?
   a) `ValueError`
   b) `IndexError`
   c) `StopIteration`
   d) `EOFError`

6. Can a generator represent an infinite sequence safely?
   a) No, it will always crash
   b) Yes, as long as you don't try to consume it entirely at once
   c) Only if it uses `return`
   d) Only with lists

7. What happens if you try to do `gen[0]` on a generator?
   a) It works exactly like list indexing
   b) It raises a `TypeError` — generators don't support indexing
   c) It always returns the first value
   d) It restarts the generator

8. Can a generator be iterated over more than once?
   a) Yes, always
   b) No — once exhausted, you must create a new generator to iterate again
   c) Only with `for` loops, not `while` loops
   d) Only if it has fewer than 10 values

9. In `while n > 0: yield n; n -= 1`, what happens each time the generator resumes?
   a) It restarts `n` from the original value
   b) It continues execution right after the `yield` statement, remembering `n`
   c) It creates a brand-new function call
   d) It ignores the `while` loop

10. Which built-in Python features behave like generators?
    a) `list()` and `dict()`
    b) `range()` and file objects (when read line by line)
    c) `print()` and `input()`
    d) `int()` and `str()`

## True / False (5)

11. A generator function must use `yield` at least once.
12. Calling a generator function executes its entire body immediately.
13. A `for` loop over a generator automatically stops when `StopIteration` is raised, without crashing your program.
14. Generators can only be used with numbers.
15. Two calls to the same generator function (e.g. `countdown(3)` and `countdown(3)`) create two independent, freshly-started generators.

## Short Answer (5)

16. In your own words, explain how `yield` is different from `return`.
17. Why are generators especially useful when processing very large files?
18. What happens internally when a generator function pauses at a `yield` statement?
19. What error occurs if you call `next()` on an already-exhausted generator, and how can a `for` loop avoid crashing because of it?
20. Give one real-world scenario (not from the lesson) where a generator would be a better choice than building a full list.

---

## Answer Key

1. b
2. b
3. b
4. b
5. c
6. b
7. b
8. b
9. b
10. b
11. True
12. False
13. True
14. False
15. True
16. `return` ends a function and sends back one final value; `yield` pauses the function, sends back one value, and preserves the function's state so it can resume from that exact point on the next call.
17. Because a generator can read and process one line at a time without loading the entire file into memory, which matters a lot for very large files.
18. The function's execution state (local variables, current position in the code) is frozen/saved so it can pick up exactly where it left off the next time a value is requested.
19. `StopIteration` is raised; a `for` loop catches `StopIteration` automatically and simply ends the loop instead of crashing.
20. Example answer: streaming live sensor readings, processing an endless feed of incoming messages, or generating IDs one at a time as needed (any reasonable example is acceptable).
