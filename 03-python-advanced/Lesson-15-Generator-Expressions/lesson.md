# Lesson 15 — Generator Expressions

## 1. Introduction

**What is this topic?**

A *generator expression* is a compact, one-line way to create a generator — similar in appearance to a list comprehension, but using parentheses `(...)` instead of square brackets `[...]`. It produces values lazily, one at a time, exactly like the generator functions from Lesson 14, without needing `def` or `yield`.

**Why is it important?**

You already learned generator *functions* (using `yield`). Generator *expressions* let you get the same memory-efficient, lazy behavior for simple transformations or filters — in a single readable line — without writing a whole function.

**Where is it used in real-world software?**

- Passing a large sequence of computed values directly into `sum()`, `max()`, or `sorted()` without ever storing them all in a list.
- Filtering and transforming data streams (e.g. log analysis, CSV processing) memory-efficiently.
- Building pipelines where one generator expression feeds into another function that also processes data lazily.

---

## 2. Conceptual Explanation

**Real-world analogy:** If a list comprehension is like ordering a full tray of cookies baked and boxed up all at once, a generator expression is like a cookie-of-the-month subscription — one cookie arrives only when you ask for the next one, and none are made until they're needed.

**Introducing the syntax**

List comprehension (builds the whole list immediately):

```python
squares_list = [x * x for x in range(5)]
print(squares_list)   # [0, 1, 4, 9, 16]
```

Generator expression (produces values lazily):

```python
squares_gen = (x * x for x in range(5))
print(squares_gen)    # <generator object <genexpr> at 0x...>
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

The syntax is nearly identical — only the brackets change: `[...]` → list, `(...)` → generator.

You can also filter, just like in a list comprehension:

```python
evens = (x for x in range(10) if x % 2 == 0)
```

**When to omit the parentheses**

If a generator expression is the *only* argument to a function call, you can drop the extra parentheses:

```python
total = sum(x * x for x in range(5))   # no extra parentheses needed
```

---

## 3. Diagrams

**List Comprehension vs. Generator Expression**

```text
[x * x for x in range(1000000)]        (x * x for x in range(1000000))
        |                                       |
        v                                       v
builds ALL 1,000,000 values                creates a lazy generator
right now, in memory                       object — no values computed yet
        |                                       |
        v                                       v
uses a lot of memory                       computes each value only
                                            when next() is called
```

**Lazy Evaluation Flow**

```text
gen = (x * x for x in range(3))
        |
        v
  nothing has run yet
        |
next(gen)  -->  computes 0*0 -> 0
next(gen)  -->  computes 1*1 -> 1
next(gen)  -->  computes 2*2 -> 4
next(gen)  -->  StopIteration
```

---

## 4. Three Examples

### Example 1 — Basic Generator Expression

**Explanation:** Converting a simple list comprehension into a generator expression.

```python
numbers = [1, 2, 3, 4, 5]
squares_gen = (n * n for n in numbers)

for value in squares_gen:
    print(value)
```

**Expected output:**

```text
1
4
9
16
25
```

**Code walkthrough:** `squares_gen` doesn't compute any squares until the `for` loop starts pulling values from it, one at a time.

---

### Example 2 — Filtering with a Generator Expression Fed into `sum()`

**Explanation:** A generator expression combined with a condition, passed directly into a built-in function.

```python
prices = [19.99, 5.50, 42.00, 3.25, 100.00]
total_expensive = sum(price for price in prices if price > 10)
print(total_expensive)
```

**Expected output:**

```text
161.99
```

**Code walkthrough:** The generator expression `price for price in prices if price > 10` yields only prices above `10`, and `sum()` consumes them one at a time — no intermediate list is ever created.

---

### Example 3 — Practical Example: Processing Student Grades

**Explanation:** Filtering and transforming data for a grade report without building unnecessary intermediate lists.

```python
students = [
    {"name": "Ana", "score": 92},
    {"name": "Leo", "score": 58},
    {"name": "Sam", "score": 74},
    {"name": "Kim", "score": 40},
]

passing_names = (s["name"] for s in students if s["score"] >= 60)

for name in passing_names:
    print(f"{name} passed!")

average_score = sum(s["score"] for s in students) / len(students)
print(f"Class average: {average_score:.1f}")
```

**Expected output:**

```text
Ana passed!
Sam passed!
Class average: 66.0
```

**Code walkthrough:** `passing_names` lazily filters students by score as the loop consumes it. The `average_score` line uses a second, separate generator expression fed directly into `sum()`, avoiding the need to build a temporary list of scores.

---

## 5. Common Mistakes

**Mistake 1 — Using square brackets when a generator was intended**

```python
squares = [x * x for x in range(1000000)]   # builds the FULL list in memory
```

Why it's a mistake (in memory-sensitive situations): if you only need to iterate once and sum/process values, a list comprehension wastes memory building something you never fully need at once.

Correct solution (when full storage isn't needed):

```python
squares = (x * x for x in range(1000000))
```

---

**Mistake 2 — Trying to reuse a generator expression**

```python
gen = (x for x in range(3))
print(list(gen))   # [0, 1, 2]
print(list(gen))   # WRONG — prints [] the second time
```

Why it's wrong: just like generator functions, generator expressions are single-use — once exhausted, they cannot be restarted.

Correct solution:

```python
gen = (x for x in range(3))
print(list(gen))
gen2 = (x for x in range(3))   # create a fresh one
print(list(gen2))
```

---

**Mistake 3 — Forgetting that indexing doesn't work on generator expressions**

```python
gen = (x * x for x in range(5))
print(gen[0])   # WRONG — TypeError: 'generator' object is not subscriptable
```

Why it's wrong: like all generators, generator expressions don't support indexing since they don't store their values.

Correct solution:

```python
gen = (x * x for x in range(5))
print(next(gen))
```

---

**Mistake 4 — Adding unnecessary extra parentheses, causing confusion with tuples**

```python
gen = ((x for x in range(5)))   # works, but redundant and confusing
my_tuple = (x for x in range(5)),   # WRONG intent — this creates a 1-item tuple containing a generator!
```

Why it's wrong: a trailing comma after a generator expression turns the whole thing into a tuple containing one generator object, which is rarely what's intended.

Correct solution:

```python
gen = (x for x in range(5))
```

---

**Mistake 5 — Believing a generator expression evaluates immediately, like a list comprehension**

```python
gen = (print(x) or x for x in range(3))
print("Created generator")   # nothing has printed yet!
for value in gen:
    pass
```

Why it's a common misconception: unlike a list comprehension, which runs immediately and fully, a generator expression is completely lazy — none of its code executes until values are actually pulled from it.

Correct understanding: creating a generator expression only sets it up; consuming it (with `next()`, a `for` loop, or a function like `sum()`) is what actually runs the code inside.

---

## 6. Debugging Practice

**Buggy Program 1**

```python
numbers = [1, 2, 3, 4]
gen = (n * n for n in numbers)
print(gen[1])   # bug
```

**Buggy Program 2**

```python
prices = [10, 20, 30]
cheap_total = sum(price for price in prices if price < 15)
print(cheap_total)
print(sum(price for price in prices if price < 15))   # bug — misunderstanding, or is it?
```

**Buggy Program 3**

```python
words = ["cat", "elephant", "dog"]
long_words = (w for w in words if len(w) > 3)
print(list(long_words))
print(list(long_words))   # bug
```

### Corrected Versions

**Program 1 — Fix**

```python
numbers = [1, 2, 3, 4]
gen = (n * n for n in numbers)
values = list(gen)
print(values[1])
```

*Bug:* generator expressions don't support indexing (`gen[1]`), which raises `TypeError`. *Why the fix works:* converting to a list first (`list(gen)`) allows indexing, at the cost of storing all values in memory.

**Program 2 — Fix**

This one is actually *not* a bug — it's included to test understanding. Each `sum(price for price in prices if price < 15)` call creates a **brand-new** generator expression, so calling it twice produces the same correct result both times:

```python
prices = [10, 20, 30]
print(sum(price for price in prices if price < 15))
print(sum(price for price in prices if price < 15))   # works fine — a new generator each time
```

*Explanation:* the mistake would only occur if the *same* generator object were reused, not if a fresh one is created by writing the expression again.

**Program 3 — Fix**

```python
words = ["cat", "elephant", "dog"]
long_words = (w for w in words if len(w) > 3)
result = list(long_words)
print(result)
print(result)   # reuse the LIST, not the exhausted generator
```

*Bug:* `long_words` is a generator; the first `list(long_words)` exhausts it completely, so the second `list(long_words)` returns an empty list. *Why the fix works:* store the result of the first conversion in a variable (`result`) and reuse that list as many times as needed.

---

## 7. Summary

- A **generator expression** looks like a list comprehension but uses `(...)` instead of `[...]`, and produces values lazily.
- Generator expressions can be passed directly into functions like `sum()`, `max()`, or `sorted()` without needing extra parentheses.
- Like generator functions, generator expressions are **single-use**: once exhausted, they must be recreated to iterate again.
- Generator expressions don't support indexing — convert to a `list()` first if you need that (but you lose the memory benefit).
- No code inside a generator expression runs until you actually start pulling values from it (lazy evaluation).
- Use list comprehensions when you need the full result stored and reused; use generator expressions when you only need to iterate once or are working with very large data.
