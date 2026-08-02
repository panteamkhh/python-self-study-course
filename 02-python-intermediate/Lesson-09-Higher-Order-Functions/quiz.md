# Lesson 09 — Quiz: Higher-Order Functions

## Multiple Choice Questions

1. What is a higher-order function?
   a) A function that runs faster than others
   b) A function that takes or returns another function
   c) A function with more than five parameters
   d) A function defined inside a class

2. What keyword creates an anonymous function in Python?
   a) `func`
   b) `def`
   c) `lambda`
   d) `anon`

3. What can a lambda's body contain?
   a) Any number of statements
   b) A single expression
   c) A `return` statement
   d) A loop

4. What does `sorted(data, key=lambda x: x[1])` do?
   a) Sorts `data` using the second element of each item for comparison
   b) Sorts `data` alphabetically only
   c) Modifies `data` in place
   d) Raises an error

5. Does `sorted()` modify the original list?
   a) Yes, always
   b) No, it returns a new list
   c) Only if `reverse=True`
   d) Only for lists of numbers

6. What does `reverse=True` do inside `sorted()`?
   a) Reverses the characters of each string
   b) Sorts in descending order
   c) Sorts only even numbers
   d) Has no effect

7. Which of the following is a valid lambda?
   a) `lambda x: return x + 1`
   b) `lambda x: x + 1`
   c) `lambda x { return x + 1 }`
   d) `def lambda(x): x + 1`

8. What is returned by `make_power(3)` if it's written as `lambda base: base ** exponent`?
   a) A number
   b) A new function
   c) `None`
   d) An error

9. What must be true for a function to be passed as an argument to another function?
   a) It must be a lambda
   b) It must return `None`
   c) Functions are ordinary values in Python, so any function can be passed
   d) It must have no parameters

10. To sort a list of tuples first by score descending, then by name ascending, which key works best?
    a) `key=lambda x: x[1]`
    b) `key=lambda x: (-x[1], x[0])`
    c) `key=lambda x: (x[1], -x[0])`
    d) `reverse=True` alone

## True/False Questions

1. A lambda can contain multiple statements separated by semicolons.
2. Functions in Python can be stored in variables just like numbers or strings.
3. `sorted()` always sorts in ascending order unless `reverse=True` is passed.
4. A higher-order function must always return another function.
5. `key=` in `sorted()` expects a function, not a value.

## Short Answer Questions

1. What makes a function "higher-order"?
2. Why can't a lambda contain a `return` statement?
3. What is the purpose of the `key` argument in `sorted()`?
4. Explain, in your own words, why `sorted()` doesn't change the original list.
5. Give a real-world example (outside of programming) that resembles how a higher-order function works.

---

## Answer Key

**Multiple Choice:** 1-b, 2-c, 3-b, 4-a, 5-b, 6-b, 7-b, 8-b, 9-c, 10-b

**True/False:** 1-False, 2-True, 3-True, 4-False, 5-True

**Short Answer (sample answers):**

1. It either accepts a function as one of its arguments, returns a function as its result, or both.
2. A lambda's body is restricted to a single expression, whose value is implicitly returned — adding `return` would be redundant and is invalid syntax.
3. `key` tells `sorted()` what value to use for comparing each item, instead of comparing the items directly.
4. `sorted()` builds and returns a brand-new list containing the items in sorted order, leaving the original list completely untouched.
5. A recipe that says "cook using whatever protein you have" — the recipe (higher-order function) doesn't care exactly what you plug in (chicken, tofu, beans), as long as it fits the role.
