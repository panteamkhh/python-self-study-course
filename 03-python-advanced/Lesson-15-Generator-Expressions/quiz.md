# Lesson 15 — Quiz: Generator Expressions

## Multiple Choice (10)

1. What brackets are used to write a generator expression?
   a) `{ }`
   b) `[ ]`
   c) `( )`
   d) `< >`

2. What is the main difference between a list comprehension and a generator expression?
   a) They produce different results
   b) A list comprehension builds the full result in memory immediately; a generator expression produces values lazily
   c) Generator expressions can only use numbers
   d) There is no difference

3. Which of these creates a generator expression?
   a) `[x for x in range(5)]`
   b) `{x for x in range(5)}`
   c) `(x for x in range(5))`
   d) `x for x in range(5)`

4. What happens when you write `sum(x for x in range(5))`?
   a) A `SyntaxError` occurs
   b) The extra parentheses of the generator expression can be omitted since it's the sole function argument
   c) It behaves differently from `sum([x for x in range(5)])`
   d) `sum()` cannot accept generators

5. What is printed by `print(x * x for x in range(3))` (without converting or iterating)?
   a) `0 1 4`
   b) `[0, 1, 4]`
   c) Something like `<generator object <genexpr> at 0x...>`
   d) A `SyntaxError`

6. Can a generator expression be reused after being fully consumed?
   a) Yes, always
   b) No — it must be recreated to iterate again
   c) Only if stored in a variable
   d) Only inside a `for` loop

7. What error occurs if you try `gen[0]` on a generator expression?
   a) `IndexError`
   b) `KeyError`
   c) `TypeError`
   d) No error — it works fine

8. When does the code inside a generator expression actually execute?
   a) Immediately when it's written
   b) Only when values are pulled from it (e.g. via `next()` or a loop)
   c) Never
   d) When the program starts

9. What does `(x for x in range(5)),` (with a trailing comma) actually create?
   a) A generator expression
   b) A list
   c) A one-item tuple containing a generator object
   d) A `SyntaxError`

10. When is a list comprehension a better choice than a generator expression?
    a) When you need to store and reuse the full result multiple times
    b) When working with an extremely large dataset
    c) Always
    d) Never

## True / False (5)

11. Generator expressions and list comprehensions use the same syntax except for the brackets used.
12. A generator expression computes all of its values as soon as it is created.
13. Passing a generator expression directly into `sum()` avoids creating an intermediate list.
14. Generator expressions can include an `if` condition, just like list comprehensions.
15. Generator expressions support indexing with square brackets, like lists.

## Short Answer (5)

16. In your own words, explain the difference between `[x for x in range(5)]` and `(x for x in range(5))`.
17. Why might a generator expression be preferred over a list comprehension when processing a very large dataset?
18. What happens if you try to iterate over an already-exhausted generator expression a second time?
19. When can you omit the parentheses around a generator expression?
20. Give an example (in words) of a situation where you would want a list instead of a generator, even though a generator uses less memory.

---

## Answer Key

1. c
2. b
3. c
4. b
5. c
6. b
7. c
8. b
9. c
10. a
11. True
12. False
13. True
14. True
15. False
16. `[x for x in range(5)]` immediately builds a complete list of all five values in memory; `(x for x in range(5))` creates a generator that produces each value one at a time, only when requested.
17. It avoids storing the entire dataset in memory at once, which keeps memory usage low and can make the program more efficient when only iterating once.
18. It produces no more values — iterating again yields nothing (an empty result), since generators are single-use.
19. When the generator expression is the only argument being passed to a function call, e.g. `sum(x for x in range(5))`.
20. Example answer: when you need to access elements by index, loop over the data multiple times, or sort it — any situation requiring random access or reuse of the full data justifies using a list (any reasonable example is acceptable).
