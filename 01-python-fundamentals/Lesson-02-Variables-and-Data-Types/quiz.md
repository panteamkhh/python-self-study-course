# Lesson 02 — Quiz

## Multiple Choice Questions

1. What does the following code create?
   ```python
   age = 30
   ```
   a) A function named `age`
   b) A variable named `age` holding the value `30`
   c) A comment
   d) A data type called `age`

2. Which data type would `3.14` be?
   a) `int`
   b) `str`
   c) `float`
   d) `bool`

3. What does `type(x)` do?
   a) Changes the type of `x`
   b) Deletes `x`
   c) Returns the current data type of `x`
   d) Converts `x` to a string

4. Which of these is a valid variable name?
   a) `2total`
   b) `total_2`
   c) `total-2`
   d) `total 2`

5. What is the data type of `True`?
   a) `str`
   b) `int`
   c) `bool`
   d) `float`

6. What happens when you reassign a variable to a value of a different type?
   a) Python raises an error
   b) The variable simply now refers to the new value and type
   c) The old value and the new value are merged
   d) Nothing happens until the program restarts

7. Which statement about Python variable names is true?
   a) They are case-insensitive
   b) `Name` and `name` refer to the same variable
   c) They are case-sensitive
   d) They must be written in all capital letters

8. What is wrong with `age = "25"` if you plan to do `age + 1` next?
   a) Nothing, it works fine
   b) `"25"` is a string, so adding `1` (an int) raises a `TypeError`
   c) Strings cannot be stored in variables
   d) `age` is a reserved word

9. Which symbol is used to assign a value to a variable?
   a) `==`
   b) `=`
   c) `:=`
   d) `->`

10. What will `print(type("hello"))` output?
    a) `<class 'int'>`
    b) `<class 'bool'>`
    c) `<class 'str'>`
    d) `hello`

## True/False Questions

11. Python requires you to declare a variable's data type before assigning a value. (True/False)

12. A variable name can start with a digit as long as it contains letters too. (True/False)

13. `is_active = True` creates a variable of type `bool`. (True/False)

14. Once a variable is created as an `int`, it can never be reassigned to a `str`. (True/False)

15. Variable names in Python are case-sensitive. (True/False)

## Short Answer Questions

16. In your own words, explain what "dynamic typing" means.

17. What is the difference between the values `5` and `"5"` in Python?

18. Why does using a variable before assigning it cause an error?

19. Name the four basic data types introduced in this lesson and give one example value for each.

20. What does the `type()` function help a programmer understand about their code?

---

## Answer Key

1. b
2. c
3. c
4. b
5. c
6. b
7. c
8. b
9. b
10. c
11. False
12. False
13. True
14. False
15. True
16. Dynamic typing means Python figures out a variable's data type automatically from the value assigned to it, rather than requiring the programmer to declare the type in advance, and that type can change if the variable is reassigned.
17. `5` is an integer (a number Python can perform arithmetic on), while `"5"` is a string (text) that looks similar but cannot be used directly in numeric calculations without conversion.
18. Python executes code top to bottom; a variable does not exist in memory until the line that assigns it has run, so referencing it earlier causes a `NameError`.
19. `int` (e.g. `7`), `float` (e.g. `3.14`), `str` (e.g. `"hello"`), `bool` (e.g. `True`).
20. It reveals the current data type Python has assigned to a variable's value, which helps explain why certain operations succeed or fail.
