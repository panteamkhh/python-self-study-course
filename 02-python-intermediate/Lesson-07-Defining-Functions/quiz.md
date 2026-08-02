# Lesson 07 — Quiz: Defining Functions

## Multiple Choice Questions

1. What keyword is used to define a function in Python?
   a) `function`
   b) `def`
   c) `func`
   d) `define`

2. What does a function return if it has no `return` statement?
   a) `0`
   b) `""`
   c) `None`
   d) An error

3. In `def greet(name):`, what is `name`?
   a) An argument
   b) A parameter
   c) A return value
   d) A global variable

4. In `greet("Sara")`, what is `"Sara"`?
   a) A parameter
   b) An argument
   c) A local variable
   d) A keyword

5. What happens if you call a function with too few arguments?
   a) The missing ones default to `None`
   b) Python raises a `TypeError`
   c) The function runs with a warning
   d) Nothing happens

6. What does `print()` inside a function do that `return` does not?
   a) Sends a value back to the caller
   b) Displays output but does not give the caller a usable value
   c) Ends the function immediately
   d) Both do exactly the same thing

7. What will `result = None and "text"` evaluate to?
   a) `"text"`
   b) `None`
   c) `True`
   d) `False`

8. What does `word[::-1]` do to a string?
   a) Removes all vowels
   b) Reverses the string
   c) Converts it to uppercase
   d) Splits it into a list

9. Which of these correctly calls a function named `square` with the argument `4`?
   a) `square[4]`
   b) `square 4`
   c) `square(4)`
   d) `square = 4`

10. What is the purpose of a function parameter?
    a) To store the function's return value
    b) To act as a placeholder for input the function will use
    c) To print output automatically
    d) To rename the function

## True/False Questions

1. Calling a function's name without parentheses runs its code.
2. A function can return a value even if it also prints something.
3. Changing a parameter inside a function changes the original variable outside it.
4. A function must always have at least one parameter.
5. `return` immediately ends the function's execution.

## Short Answer Questions

1. What is the difference between a parameter and an argument?
2. Why does printing inside a function not let the caller use the result later?
3. What value does a function return by default if you don't write `return`?
4. Why is it good practice to break a large program into small functions?
5. Explain, in your own words, why changing a parameter inside a function does not affect the original variable passed in.

---

## Answer Key

**Multiple Choice:** 1-b, 2-c, 3-b, 4-b, 5-b, 6-b, 7-b, 8-b, 9-c, 10-b

**True/False:** 1-False, 2-True, 3-False, 4-False, 5-True

**Short Answer (sample answers):**

1. A parameter is the placeholder name in the function definition; an argument is the actual value supplied when the function is called.
2. Printing only displays text on screen — it doesn't hand a value back into the program, so the caller has nothing to store or use afterward.
3. It returns `None`.
4. Small functions are easier to read, test, debug, and reuse across different parts of a program.
5. Python passes a copy of the reference to the value into the function's own local variable; reassigning that local variable inside the function has no effect on the variable in the caller's scope.
