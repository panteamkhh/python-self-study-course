# Lesson 13 — Quiz: Special Methods

## Multiple Choice (10)

1. What is another name for special methods like `__init__` and `__str__`?
   a) Hidden methods
   b) Dunder methods
   c) Static methods
   d) Private methods

2. Which special method controls what `print(obj)` displays?
   a) `__print__`
   b) `__display__`
   c) `__str__`
   d) `__show__`

3. What does Python do if `==` is used on an object without a defined `__eq__`?
   a) Raises an error
   b) Compares the objects by identity (are they the same object in memory)
   c) Always returns `True`
   d) Compares attribute names

4. Which special method is triggered by `obj1 + obj2`?
   a) `__plus__`
   b) `__sum__`
   c) `__add__`
   d) `__combine__`

5. Which special method allows `len(obj)` to work on a custom object?
   a) `__length__`
   b) `__len__`
   c) `__size__`
   d) `__count__`

6. Which special method allows `obj[0]` to work on a custom object?
   a) `__index__`
   b) `__item__`
   c) `__getitem__`
   d) `__at__`

7. What happens if `__add__` doesn't include a `return` statement?
   a) It causes a `SyntaxError`
   b) The expression evaluates to `None`
   c) Python automatically returns `self`
   d) It raises `TypeError` immediately at definition time

8. What is the main purpose of `__repr__`?
   a) Formatting money values
   b) A developer-facing / debugging representation of an object
   c) Comparing two objects
   d) Deleting an object

9. Which special method does `sorted()` rely on to compare custom objects?
   a) `__sort__`
   b) `__compare__`
   c) `__lt__`
   d) `__order__`

10. What is a good real-world analogy for special methods?
    a) A locked box no one can open
    b) A universal remote's standard buttons that each device wires up itself
    c) A random number generator
    d) A single global variable

## True / False (5)

11. Special methods let custom objects work with Python's built-in operators and functions.
12. If you don't define `__str__`, `print(obj)` will always throw an error.
13. `__eq__` must be defined manually if you want `==` to compare object data instead of identity.
14. `__getitem__` alone is enough to make `len()` work on an object.
15. `__add__` must return a value in order for `+` to produce a usable result.

## Short Answer (5)

16. In your own words, what problem do special methods solve for custom classes?
17. What is the difference in purpose between `__str__` and `__repr__`?
18. Why does `Point(1,2) == Point(1,2)` return `False` unless `__eq__` is defined?
19. Name two special methods you could implement to make a custom class behave like a list.
20. What common mistake often causes `__add__` or `__eq__` to behave incorrectly?

---

## Answer Key

1. b
2. c
3. b
4. c
5. b
6. c
7. b
8. b
9. c
10. b
11. True
12. False
13. True
14. False
15. True
16. Special methods let custom objects integrate with Python's built-in syntax (printing, operators, comparisons, `len()`, indexing) instead of only exposing custom-named methods.
17. `__str__` is meant for a readable, user-facing representation (used by `print()`/`str()`); `__repr__` is meant for an unambiguous, developer-facing representation used for debugging.
18. Without `__eq__`, Python compares objects by identity (memory address) rather than by their attribute values, so two different objects with the same data are still considered "not equal."
19. `__len__` and `__getitem__` (accepting `__setitem__` and `__iter__` as valid extra answers too).
20. Forgetting to `return` a value from the method, or accidentally comparing `self` to itself instead of to `other`.
