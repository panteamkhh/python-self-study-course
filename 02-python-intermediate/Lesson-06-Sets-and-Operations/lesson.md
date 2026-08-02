# Lesson 06 — Sets and Operations

## 1. Introduction

A **set** is a collection of unique, unordered values. Unlike a list, a set never stores duplicates, and it does not remember the order in which items were added.

Sets matter because a huge number of real problems are really questions about *membership* and *overlap*: Which users are in both groups? Which tags are unused? Which items appeared only once? Lists can answer these questions too, but sets answer them faster and with far less code.

In real-world software, sets show up in:

* Removing duplicate records from a dataset.
* Comparing two groups of users (shared permissions, common friends, mutual followers).
* Fast membership checks (`if user_id in blocked_users`) in login and security systems.
* Tag systems, where each item has a set of labels.

## 2. Conceptual Explanation

Think of a set like a bag of unique library cards. If you already have a card with a name on it and someone hands you a duplicate, you simply don't add it — the bag never holds two cards with the same name. There's also no "first" or "second" card in the bag; you can only ask "is this card in here?"

This is different from a list, which is like a numbered shelf: order matters, and the same book can appear in multiple slots.

Because a set only cares about *uniqueness* and *membership*, Python can check "is X in this set?" almost instantly, no matter how large the set is — unlike a list, where Python may have to check every single item one by one.

### Creating a set

```python
numbers = {1, 2, 3, 4}
empty_set = set()  # NOT {} — that creates an empty dictionary!
from_list = set([1, 2, 2, 3])  # duplicates are dropped automatically
```

## 3. Diagrams

**List vs. Set — duplicates and order:**

```
List:  [3, 1, 3, 2]   -> keeps order, keeps duplicates
Set:   {3, 1, 3, 2}   -> {1, 2, 3}  (order not guaranteed, duplicates removed)
```

**Set operations as overlapping circles:**

```
   A only     A ∩ B      B only
  +------+  +------+  +------+
  |  A   |==|A and B|==|  B   |
  +------+  +------+  +------+

  A | B  = everything in either circle   (union)
  A & B  = only the overlap              (intersection)
  A - B  = A's circle minus the overlap  (difference)
  A ^ B  = everything except the overlap (symmetric difference)
```

## 4. Three Examples

### Example 1 — Simple: unique letters in a word

**Explanation:** Convert a string into a set of characters to find how many *distinct* letters it uses.

```python
word = "banana"
unique_letters = set(word)
print(unique_letters)
print(len(unique_letters))
```

**Expected Output:**

```
{'b', 'a', 'n'}
3
```

*(Note: the printed order of set elements may vary, but the contents and count will always match.)*

**Code Walkthrough:** `set(word)` treats the string as a sequence of characters and keeps only the unique ones. `len()` then counts how many unique letters remain.

### Example 2 — Intermediate: comparing two classes of students

**Explanation:** Given two sets of student names, find who is in both classes, who is only in class A, and who is enrolled in either class.

```python
class_a = {"Ali", "Sara", "Reza", "Mona"}
class_b = {"Sara", "Reza", "Kian"}

both_classes = class_a & class_b
only_a = class_a - class_b
either_class = class_a | class_b

print("In both:", both_classes)
print("Only in A:", only_a)
print("In either:", either_class)
```

**Expected Output:**

```
In both: {'Sara', 'Reza'}
Only in A: {'Ali', 'Mona'}
In either: {'Ali', 'Sara', 'Reza', 'Mona', 'Kian'}
```

**Code Walkthrough:** `&` is intersection (shared elements), `-` is difference (in the left set but not the right), and `|` is union (everything from both sets, duplicates merged).

### Example 3 — Real-World: shared numbers between two input lines

**Explanation:** Read two lines of space-separated numbers and print the numbers that appear in both lines, matching the structure of a common "find common elements" task.

```python
line1 = input()
line2 = input()

set1 = set(line1.split())
set2 = set(line2.split())

common = set1 & set2

if common:
    print(" ".join(sorted(common, key=int)))
else:
    print()
```

**Expected Output (for input `1 2 3 4 5` then `3 4 5 6 7`):**

```
3 4 5
```

**Code Walkthrough:** Each line is split into individual number-strings and turned into a set. The intersection `&` finds the shared values. `sorted(..., key=int)` orders them numerically (since they are still strings) before joining them back into one line. If there is no overlap, an empty line is printed.

## 5. Common Mistakes

**Mistake 1 — Using `{}` for an empty set**

```python
empty = {}
```

*Why it's wrong:* `{}` creates an empty **dictionary**, not a set.

```python
empty = set()
```

**Mistake 2 — Trying to index a set**

```python
s = {1, 2, 3}
print(s[0])
```

*Why it's wrong:* Sets have no order, so there is no "first item" — this raises a `TypeError`.

```python
s = {1, 2, 3}
print(list(s)[0])  # convert to a list first if you need indexing
```

**Mistake 3 — Assuming sets preserve insertion order**

```python
s = {3, 1, 2}
print(s)  # you might expect {3, 1, 2}
```

*Why it's wrong:* Sets do not guarantee any particular order in output; relying on it will break your program on a different Python version or run.

```python
s = {3, 1, 2}
print(sorted(s))  # explicitly sort if order matters
```

**Mistake 4 — Confusing `-` with symmetric difference**

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # learner expects "everything different between them"
```

*Why it's wrong:* `a - b` only removes `b`'s elements from `a`; it does **not** give you the full symmetric difference.

```python
print(a ^ b)  # {1, 4} — items in exactly one of the two sets
```

**Mistake 5 — Adding an unhashable item to a set**

```python
s = set()
s.add([1, 2])
```

*Why it's wrong:* Lists are mutable and unhashable, so they cannot be stored inside a set — this raises a `TypeError`.

```python
s = set()
s.add((1, 2))  # tuples are hashable, so this works
```

## 6. Debugging Practice

**Buggy Program 1:**

```python
tags = {}
tags.add("python")
tags.add("beginner")
print(tags)
```

**Buggy Program 2:**

```python
scores = {90, 85, 70, 60}
print(scores[0])
```

**Buggy Program 3:**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a + b)
```

### Corrected Versions

**Fix 1:**

```python
tags = set()
tags.add("python")
tags.add("beginner")
print(tags)
```

*Bug:* `{}` creates a dictionary, so `.add()` (a set method) does not exist on it. *Why the fix works:* `set()` creates a real empty set, which supports `.add()`.

**Fix 2:**

```python
scores = {90, 85, 70, 60}
print(sorted(scores)[0])
```

*Bug:* Sets cannot be indexed with `[0]` because they have no defined order. *Why the fix works:* Sorting the set first produces an ordered list, which can be safely indexed.

**Fix 3:**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
```

*Bug:* Sets don't support the `+` operator for combining. *Why the fix works:* `|` is the correct set operation for union (combining all unique elements).

## 7. Summary

* A set stores **unique**, **unordered** values — duplicates are automatically removed.
* Create a set with `{1, 2, 3}` or `set()`; never use `{}` for an empty set.
* Core operations: `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference).
* Sets cannot be indexed — convert to a `list` or use `sorted()` if you need order.
* Only hashable (immutable) items — like numbers, strings, and tuples — can go inside a set.
* Sets are the right tool whenever a problem is really about membership or overlap between groups.
