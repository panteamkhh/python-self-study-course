# Lesson 08 — Quiz: Arguments and Scope

## Multiple Choice Questions

1. What is a "default argument"?
   a) An argument that must always be provided
   b) A fallback value used when the caller doesn't supply one
   c) The first argument in a function
   d) An argument that cannot be changed

2. What must come first in a function call — positional or keyword arguments?
   a) Keyword arguments
   b) Positional arguments
   c) It doesn't matter
   d) Neither can be used together

3. What is a local variable?
   a) A variable available everywhere in the program
   b) A variable that only exists inside the function where it was created
   c) A variable that is always named `x`
   d) A variable declared with the `local` keyword

4. What happens when you try to use a local variable outside its function?
   a) It returns `0`
   b) It returns `None`
   c) Python raises a `NameError`
   d) Python silently ignores it

5. Why is using a mutable default argument (like `[]`) risky?
   a) It causes a syntax error
   b) It is created once and shared across all calls
   c) It slows down the program significantly
   d) It cannot store more than one item

6. What keyword lets a function modify a variable from the global scope?
   a) `nonlocal`
   b) `global`
   c) `static`
   d) `outer`

7. What does `*args` do in a function definition?
   a) Requires exactly one argument
   b) Collects extra positional arguments into a tuple
   c) Collects keyword arguments into a dictionary
   d) Raises an error if extra arguments are passed

8. What does `**kwargs` (or any `**name`) collect?
   a) A tuple of positional arguments
   b) A list of default values
   c) A dictionary of extra keyword arguments
   d) Nothing — it's invalid syntax

9. What is a closure?
   a) A function that has no parameters
   b) A function that remembers variables from its enclosing scope
   c) A function that can never return a value
   d) An error caused by scope conflicts

10. What error occurs if you assign to a global variable inside a function without declaring `global`?
    a) `TypeError`
    b) `SyntaxError`
    c) `UnboundLocalError`
    d) No error at all

## True/False Questions

1. Keyword arguments can be passed in any order.
2. A variable created inside a function is automatically available outside it.
3. Default argument values are re-evaluated every time the function is called.
4. `*args` and `**kwargs` can both be used in the same function definition.
5. Using `global` inside a function is required to simply *read* a global variable's value.

## Short Answer Questions

1. What is the difference between a positional argument and a keyword argument?
2. Why does a function's local variable disappear after the function finishes running?
3. Explain why mutable default arguments can cause unexpected bugs.
4. What is the purpose of the `global` keyword?
5. In your own words, describe what a closure "remembers" and why that's useful.

---

## Answer Key

**Multiple Choice:** 1-b, 2-b, 3-b, 4-c, 5-b, 6-b, 7-b, 8-c, 9-b, 10-c

**True/False:** 1-True, 2-False, 3-False, 4-True, 5-False

**Short Answer (sample answers):**

1. A positional argument is matched to a parameter by its order in the call; a keyword argument is matched by explicitly naming the parameter, regardless of order.
2. Local variables live only in the function's private scope, which is created when the function starts and destroyed once it returns.
3. A mutable default (like `[]`) is created only once, when the function is defined, so every call that relies on the default shares and modifies the same object instead of getting a fresh one.
4. `global` tells Python that an assignment inside a function should modify the existing variable in the global scope, rather than creating a new local variable with the same name.
5. A closure remembers the variables from the scope in which it was created, even after that outer function has finished running — useful for creating customized functions, like a multiplier with a fixed factor.
