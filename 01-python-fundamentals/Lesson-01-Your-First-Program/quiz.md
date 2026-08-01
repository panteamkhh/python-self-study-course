# Lesson 01 — Quiz

## Multiple Choice Questions

1. What is the correct way to print the text `Hi there` in Python 3?
   a) `print Hi there`
   b) `print("Hi there")`
   c) `echo("Hi there")`
   d) `print[Hi there]`

2. What does the `print()` function do?
   a) Reads a value from the user
   b) Displays a value on the screen
   c) Deletes a variable
   d) Saves a file

3. Which line is a comment in Python?
   a) `// This is a note`
   b) `<!-- This is a note -->`
   c) `# This is a note`
   d) `** This is a note **`

4. What happens if you run `print(Hello)` without quotes around `Hello`?
   a) It prints `Hello`
   b) It prints an empty line
   c) It raises an error because Python looks for a name called `Hello`
   d) It prints `None`

5. In what order does Python execute the lines of a simple script?
   a) Randomly
   b) Bottom to top
   c) Top to bottom
   d) All at once

6. What is the return value of `print("test")`?
   a) `"test"`
   b) `True`
   c) `None`
   d) `0`

7. Which of these correctly prints a sentence containing an apostrophe?
   a) `print('It's sunny')`
   b) `print("It's sunny")`
   c) `print(It's sunny)`
   d) `print(#It's sunny#)`

8. How many lines of output does this produce?
   ```python
   print("A")
   print("B")
   print("C")
   ```
   a) 1
   b) 2
   c) 3
   d) 0

9. What is required after the word `print` in Python 3 to call it correctly?
   a) A colon
   b) Parentheses
   c) A semicolon
   d) Nothing

10. Why does Python ignore lines starting with `#`?
    a) Because they are considered errors
    b) Because `#` marks the end of a file
    c) Because they are comments meant only for humans
    d) Because `#` disables the whole program

## True/False Questions

11. Python programs execute their lines in a random order. (True/False)

12. `print()` is used to display information to the screen. (True/False)

13. Comments in Python start with the symbol `#`. (True/False)

14. In Python 3, you can call `print` without parentheses. (True/False)

15. A string must be wrapped in matching quote characters (both single or both double). (True/False)

## Short Answer Questions

16. What is a "function" in the context of `print()`?

17. Why does `print("It's a test")` work but `print('It's a test')` does not?

18. What is the purpose of a comment in a Python program?

19. What value does `print()` return, and why does that matter if you try to store it in a variable?

20. Describe, in your own words, what the Python interpreter does when it runs a `.py` file.

---

## Answer Key

1. b
2. b
3. c
4. c
5. c
6. c
7. b
8. c
9. b
10. c
11. False
12. True
13. True
14. False
15. True
16. A function is a named, reusable action that Python can perform when called; `print` is a built-in function that displays whatever is passed to it.
17. Double quotes let the apostrophe inside the sentence be treated as ordinary text, while single quotes end the string early at the apostrophe, breaking the syntax.
18. A comment documents the code for human readers; Python ignores it completely during execution.
19. `print()` always returns `None`; storing it in a variable gives you a variable that holds "nothing useful," so you cannot use it like the original text.
20. The interpreter reads the file from the first line to the last line and executes each instruction in order, producing whatever output or effects those instructions specify.
