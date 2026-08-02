# Lesson 09 — Higher-Order Functions

## 1. Introduction

A **higher-order function** is a function that either takes another function as an argument, returns a function, or both. In Python, functions are ordinary values — they can be stored in variables, passed around, and returned — just like numbers or strings.

This idea unlocks a powerful style of programming where you describe *what* should happen to each item in a collection, rather than writing out the loop by hand every time. It matters because:

* It leads to shorter, more expressive code for common patterns (transforming, filtering, sorting).
* It's used constantly in real-world code: sorting a list of records by a custom rule, filtering out invalid entries, or applying a transformation to every element in a dataset.
* It's the foundation for understanding more advanced tools later, like `map`, `filter`, and callback-based APIs.

## 2. Conceptual Explanation

Imagine a factory conveyor belt where each item passes through a machine. Instead of building a brand-new factory for every different task, you can plug a *different tool* into the same conveyor-belt system. The conveyor belt is like `sorted()` or a loop; the tool you plug in is a function you supply — telling the belt exactly *how* to treat each item.

In Python, the most common way to "plug in" a small custom function is with a **lambda** — a short, anonymous function written in a single line.

```python
square = lambda x: x * x
print(square(5))  # 25
```

This is equivalent to:

```python
def square(x):
    return x * x
```

Passing a function as an argument looks like this:

```python
def apply_twice(func, value):
    return func(func(value))

print(apply_twice(lambda x: x + 3, 10))  # 16
```

## 3. Diagrams

**Function as a value being passed around:**

```
   my_function  ---->  passed into  ---->  another_function(my_function, data)
        |                                          |
        |                                          v
        +-----------------  called inside  --------+
```

**`sorted()` with a `key` function:**

```
data:  [("Bob", 92), ("Alice", 85), ("Charlie", 78)]

sorted(data, key=lambda pair: pair[1], reverse=True)
                      |
                      v
     compares using pair[1] (the score) for each item
                      |
                      v
      [("Bob", 92), ("Alice", 85), ("Charlie", 78)]
```

## 4. Three Examples

### Example 1 — Simple: a lambda as a standalone function

**Explanation:** Create a small anonymous function and use it directly.

```python
double = lambda x: x * 2
print(double(7))
print((lambda x, y: x + y)(3, 4))
```

**Expected Output:**

```
14
7
```

**Code Walkthrough:** `double` is a lambda bound to a name, used just like a regular function. The second line defines and calls a lambda immediately, without ever giving it a name.

### Example 2 — Intermediate: sorting a list with a custom key

**Explanation:** Sort a list of tuples by their second element using `sorted()`'s `key` parameter.

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
by_score = sorted(students, key=lambda student: student[1], reverse=True)

for name, score in by_score:
    print(name, score)
```

**Expected Output:**

```
Bob 92
Alice 85
Charlie 78
```

**Code Walkthrough:** `key=lambda student: student[1]` tells `sorted()` to compare each tuple using its score (index 1), rather than the whole tuple. `reverse=True` sorts from highest to lowest.

### Example 3 — Real-World: ranking students by score, name only

**Explanation:** Read a number of students with their scores, then print just their names, ordered from the highest score to the lowest — a common leaderboard task.

```python
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

ranked = sorted(students, key=lambda student: student[1], reverse=True)

for name, score in ranked:
    print(name)
```

**Expected Output (for input `3`, `Alice 85`, `Bob 92`, `Charlie 78`):**

```
Bob
Alice
Charlie
```

**Code Walkthrough:** Each input line is split into a name and a score, stored as a tuple. `sorted()` with a lambda `key` orders the tuples by score, descending. The final loop prints only the names, in ranked order.

## 5. Common Mistakes

**Mistake 1 — Forgetting `sorted()` returns a new list**

```python
numbers = [3, 1, 2]
numbers.sorted()
```

*Why it's wrong:* Lists don't have a `.sorted()` method; `sorted()` is a built-in function, and `numbers.sort()` (a method) sorts in place instead.

```python
numbers = [3, 1, 2]
numbers = sorted(numbers)
```

**Mistake 2 — Adding a `return` inside a lambda**

```python
square = lambda x: return x * x
```

*Why it's wrong:* A lambda's body is a single expression; it implicitly returns that expression's value, so writing `return` is a `SyntaxError`.

```python
square = lambda x: x * x
```

**Mistake 3 — Forgetting `key=` when passing a sorting function**

```python
students = [("Alice", 85), ("Bob", 92)]
sorted(students, lambda s: s[1])
```

*Why it's wrong:* `sorted()` expects the function as the `key` keyword argument; passing it positionally is interpreted as `reverse`, causing a `TypeError`.

```python
sorted(students, key=lambda s: s[1])
```

**Mistake 4 — Assuming `sorted()` changes the original list**

```python
numbers = [3, 1, 2]
sorted(numbers)
print(numbers)
```

*Why it's wrong:* `sorted()` returns a **new** sorted list and leaves the original untouched, so `numbers` still prints `[3, 1, 2]`.

```python
numbers = [3, 1, 2]
numbers = sorted(numbers)
print(numbers)
```

**Mistake 5 — Using a multi-statement block inside a lambda**

```python
process = lambda x: print(x); x * 2
```

*Why it's wrong:* A lambda can only contain a single expression — you cannot chain statements with a semicolon inside it; this doesn't behave as intended (the `print` and the multiplication aren't both part of the lambda).

```python
def process(x):
    print(x)
    return x * 2
```

## 6. Debugging Practice

**Buggy Program 1:**

```python
words = ["banana", "kiwi", "apple"]
sorted_words = words.sorted(key=len)
print(sorted_words)
```

**Buggy Program 2:**

```python
pairs = [(1, "b"), (2, "a")]
result = sorted(pairs, lambda p: p[1])
print(result)
```

**Buggy Program 3:**

```python
cube = lambda x: return x ** 3
print(cube(3))
```

### Corrected Versions

**Fix 1:**

```python
words = ["banana", "kiwi", "apple"]
sorted_words = sorted(words, key=len)
print(sorted_words)
```

*Bug:* Lists have no `.sorted()` method. *Why the fix works:* `sorted()` is the correct built-in function, called with the list as its first argument.

**Fix 2:**

```python
pairs = [(1, "b"), (2, "a")]
result = sorted(pairs, key=lambda p: p[1])
print(result)
```

*Bug:* The lambda was passed positionally instead of as `key=`. *Why the fix works:* `sorted()` requires the sorting function to be passed through the `key` keyword argument.

**Fix 3:**

```python
cube = lambda x: x ** 3
print(cube(3))
```

*Bug:* A lambda body is a single expression and cannot contain a `return` statement. *Why the fix works:* Removing `return` lets the expression's value be implicitly returned, as lambdas require.

## 7. Summary

* A higher-order function takes a function as an argument, returns one, or both.
* Functions in Python are values — they can be stored, passed, and returned like any other object.
* `lambda arguments: expression` creates a short, anonymous, single-expression function.
* `sorted(iterable, key=..., reverse=...)` uses a `key` function to decide how to compare items, without changing the original list.
* Lambdas cannot contain `return` statements or multiple statements — only one expression.
* Use `sorted()` when you need a new ordered list; use `.sort()` only when you want to sort a list in place.
