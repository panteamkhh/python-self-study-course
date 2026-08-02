# Lesson 06 — Quiz: Sets and Operations

## Multiple Choice Questions

1. What does `{1, 2, 2, 3}` evaluate to?
   a) `{1, 2, 2, 3}`
   b) `{1, 2, 3}`
   c) An error
   d) `[1, 2, 3]`

2. Which of these creates an empty set?
   a) `{}`
   b) `set{}`
   c) `set()`
   d) `[]`

3. What does `a & b` return for two sets?
   a) Union of both sets
   b) Only elements in both sets
   c) Elements in `a` but not `b`
   d) A new empty set

4. What does `a - b` return?
   a) Elements in `a` but not in `b`
   b) Elements in `b` but not in `a`
   c) Elements common to both
   d) All elements from both sets

5. Which operator gives the symmetric difference?
   a) `&`
   b) `|`
   c) `-`
   d) `^`

6. What happens if you try `my_set[0]`?
   a) It returns the first inserted item
   b) It returns a random item
   c) It raises a `TypeError`
   d) It returns `None`

7. Which of the following can be added to a set?
   a) A list
   b) A dictionary
   c) A tuple
   d) Another set

8. What does `a <= b` check for two sets?
   a) Whether `a` and `b` are equal
   b) Whether `a` is a subset of `b`
   c) Whether `a` has fewer elements than `b`
   d) Whether `a` and `b` share no elements

9. What is the result of `set("hello")`?
   a) `{'h', 'e', 'l', 'l', 'o'}`
   b) `{'h', 'e', 'l', 'o'}`
   c) `['h', 'e', 'l', 'o']`
   d) An error

10. Which method removes an item from a set without raising an error if it's missing?
    a) `.remove()`
    b) `.discard()`
    c) `.pop()`
    d) `.delete()`

## True/False Questions

1. Sets maintain the order in which items were inserted.
2. A set can contain duplicate values if you add them with `.add()` twice.
3. `set()` and `{}` both create an empty set.
4. `a | b` returns all unique elements from both `a` and `b`.
5. Sets can store lists as elements.

## Short Answer Questions

1. What is the main difference between a list and a set?
2. Why can't you index into a set using `my_set[0]`?
3. What does the intersection of two sets represent conceptually?
4. Why must elements added to a set be hashable?
5. Give one real-world scenario where a set is more useful than a list.

---

## Answer Key

**Multiple Choice:** 1-b, 2-c, 3-b, 4-a, 5-d, 6-c, 7-c, 8-b, 9-b, 10-b

**True/False:** 1-False, 2-False, 3-False, 4-True, 5-False

**Short Answer (sample answers):**

1. A list is ordered and allows duplicates; a set is unordered and stores only unique values.
2. Sets have no defined order, so there is no concept of a "first" or "0th" element to index.
3. It represents the elements shared by both sets — what they have in common.
4. Sets rely on each element's hash value to check uniqueness and membership quickly; unhashable (mutable) types like lists cannot provide a stable hash.
5. Removing duplicate entries from a large dataset, or quickly checking whether a user ID exists in a blocklist.
