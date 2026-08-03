# Lesson 14 — Generators and Yield

## 1. Introduction

**What is this topic?**

A *generator* is a special kind of function that produces a sequence of values **one at a time**, pausing between each one, instead of computing and returning them all at once. The `yield` keyword is what turns an ordinary function into a generator.

**Why is it important?**

If you need a list of the first 10 million numbers, building the entire list in memory can be slow and wasteful. A generator produces values *on demand*, using very little memory, no matter how large (or infinite) the sequence is.

**Where is it used in real-world software?**

- Reading huge files line-by-line without loading the whole file into memory.
- Streaming data from an API or database, one record at a time.
- Generating infinite sequences (like an ID counter) that would be impossible to store as a list.
- Python's own built-ins — `range()`, `enumerate()`, `zip()`, and file objects — all behave like generators.

---

## 2. Conceptual Explanation

**Real-world analogy:** Think of a regular function as a chef who cooks an entire 10-course meal and brings it all to your table at once — you have to wait for everything before eating anything, and the table needs a lot of space. A generator is a chef who brings you **one course at a time**, only cooking the next dish when you finish the current one and ask for more. Nothing is prepared until it's actually needed.

**Introducing the syntax**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

- `yield` pauses the function and sends a value back to whoever is iterating over it.
- The function's state (all local variables) is **frozen** at that point.
- The next time a value is requested, the function resumes exactly where it left off.

```python
for number in countdown(3):
    print(number)
```

**Expected output:**

```text
3
2
1
```

Compare this to a normal function using `return`:

```python
def countdown_list(n):
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result
```

`countdown_list` builds the *entire* list in memory before returning it. `countdown` never stores more than one number at a time.

You can also manually pull values with `next()`:

```python
gen = countdown(2)
print(next(gen))   # 2
print(next(gen))   # 1
print(next(gen))   # raises StopIteration — no more values
```

---

## 3. Diagrams

**Regular Function vs. Generator**

```text
Regular function (return)          Generator (yield)
--------------------------         --------------------------
call countdown_list(3)             call countdown(3)
      |                                  |
      v                                  v
builds [3, 2, 1] fully                creates a "paused" generator
      |                                  |
      v                                  v
returns the whole list         next() -> runs until first yield -> 3 (pauses)
                                next() -> resumes, runs to next yield -> 2 (pauses)
                                next() -> resumes, runs to next yield -> 1 (pauses)
                                next() -> function ends -> StopIteration
```

**Execution Flow of `yield`**

```text
def countdown(n):
    while n > 0:
        yield n     <-- function pauses HERE, remembers n
        n -= 1      <-- resumes HERE on the next next() call
```

---

## 4. Three Examples

### Example 1 — A Simple Number Generator

**Explanation:** The most basic generator: yields numbers one at a time.

```python
def simple_numbers():
    yield 1
    yield 2
    yield 3


for num in simple_numbers():
    print(num)
```

**Expected output:**

```text
1
2
3
```

**Code walkthrough:** Each `yield` produces one value and pauses. The `for` loop automatically calls `next()` repeatedly until the generator is exhausted.

---

### Example 2 — Generating an Infinite Sequence (with a Limit)

**Explanation:** Generators can represent infinite sequences safely, since values are only produced when asked for.

```python
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2


gen = even_numbers()
for _ in range(5):
    print(next(gen))
```

**Expected output:**

```text
0
2
4
6
8
```

**Code walkthrough:** `even_numbers()` would run forever if fully consumed, but because we only call `next()` five times, only five values are ever produced.

---

### Example 3 — Practical Example: Reading a Large File Line by Line

**Explanation:** A generator that processes text data (like log lines) without loading everything into memory at once.

```python
def read_important_lines(lines):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()


log_lines = [
    "INFO: server started",
    "ERROR: disk full",
    "INFO: request handled",
    "ERROR: connection lost",
]

for important_line in read_important_lines(log_lines):
    print(important_line)
```

**Expected output:**

```text
ERROR: disk full
ERROR: connection lost
```

**Code walkthrough:** `read_important_lines` filters and yields only matching lines, one at a time. In a real program, `lines` could come from `open("huge_log_file.txt")`, and this generator would process gigabytes of data using almost no extra memory.

---

## 5. Common Mistakes

**Mistake 1 — Using `return` with a value inside a generator, expecting it to behave like `yield`**

```python
def numbers():
    return 1
    return 2   # never reached, and this isn't how generators work anyway
```

Why it's wrong: this is just a regular function that returns `1`; it is not a generator at all (no `yield` is used), and the second `return` is unreachable dead code.

Correct solution:

```python
def numbers():
    yield 1
    yield 2
```

---

**Mistake 2 — Trying to index or slice a generator like a list**

```python
gen = countdown(5)
print(gen[0])   # WRONG — TypeError: 'generator' object is not subscriptable
```

Why it's wrong: generators don't store their values; they produce them on demand and don't support indexing.

Correct solution:

```python
gen = countdown(5)
print(next(gen))   # get the next value one at a time
# or, if you need a list:
print(list(countdown(5))[0])
```

---

**Mistake 3 — Reusing an already-exhausted generator**

```python
gen = countdown(3)
for n in gen:
    print(n)

for n in gen:      # WRONG — prints nothing, generator is exhausted
    print(n)
```

Why it's wrong: once a generator has produced all its values, it cannot be "rewound" — it's a one-time-use iterator.

Correct solution:

```python
for n in countdown(3):   # create a fresh generator each time
    print(n)
```

---

**Mistake 4 — Calling `next()` too many times**

```python
gen = countdown(2)
print(next(gen))
print(next(gen))
print(next(gen))   # WRONG — raises StopIteration
```

Why it's wrong: once a generator runs out of values, calling `next()` again raises `StopIteration` instead of returning something.

Correct solution: use a `for` loop (which handles `StopIteration` automatically) or check with a default:

```python
for value in countdown(2):
    print(value)
```

---

**Mistake 5 — Thinking a generator function runs immediately when called**

```python
def loud_numbers():
    print("Starting!")
    yield 1
    yield 2


gen = loud_numbers()
print("Generator created")   # "Starting!" has NOT printed yet
print(next(gen))              # NOW "Starting!" prints, then 1
```

Why it's a common misconception: calling a generator function does **not** run its body — it only creates a generator object. The code only starts executing on the first `next()` call.

Correct understanding: treat generator creation and generator *consumption* as two separate steps.

---

## 6. Debugging Practice

**Buggy Program 1**

```python
def numbers():
    for i in range(3):
        return i   # bug


for n in numbers():
    print(n)
```

**Buggy Program 2**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1


gen = countdown(3)
print(list(gen))
print(list(gen))   # bug — expecting the same values again
```

**Buggy Program 3**

```python
def squares(limit):
    n = 1
    while n <= limit:
        yield n * n
    n += 1   # bug — indentation


for sq in squares(5):
    print(sq)
```

### Corrected Versions

**Program 1 — Fix**

```python
def numbers():
    for i in range(3):
        yield i


for n in numbers():
    print(n)
```

*Bug:* `return i` inside the loop exits the function on the very first iteration, and since `return` isn't `yield`, this isn't even a generator — it just returns `0` and the `for n in numbers()` line raises `TypeError` because it tries to iterate over an integer. *Why the fix works:* `yield i` pauses and produces each value in turn, correctly making the function a generator that the `for` loop can iterate over.

**Program 2 — Fix**

```python
gen = countdown(3)
print(list(gen))
gen2 = countdown(3)     # create a new generator for a second pass
print(list(gen2))
```

*Bug:* the first `list(gen)` fully consumes the generator; calling `list(gen)` a second time on the same, already-exhausted generator returns an empty list. *Why the fix works:* creating a brand-new generator object (`countdown(3)` again) gives a fresh sequence to iterate.

**Program 3 — Fix**

```python
def squares(limit):
    n = 1
    while n <= limit:
        yield n * n
        n += 1


for sq in squares(5):
    print(sq)
```

*Bug:* `n += 1` was outside the `while` loop (wrong indentation), so `n` never increased — causing an infinite loop that yields `1` forever. *Why the fix works:* indenting `n += 1` inside the loop body ensures `n` increases every iteration, so the loop eventually stops at `limit`.

---

## 7. Summary

- A **generator** is a function that uses `yield` to produce values one at a time, pausing its state between each value.
- Generators are memory-efficient — ideal for large or infinite sequences.
- `next(gen)` retrieves the next value; a `for` loop calls `next()` automatically and stops safely on `StopIteration`.
- Calling a generator function does **not** run its body immediately — it only creates a generator object; execution starts on the first `next()`.
- Generators are single-use: once exhausted, you must create a new one to iterate again.
- Never try to index (`gen[0]`) a generator directly — convert to a list first if you need that, but doing so gives up the memory savings.
