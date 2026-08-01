# Lesson 05 — Quiz

## Multiple Choice Questions

1. What data type does a comparison like `5 > 3` produce?
   a) `int`
   b) `str`
   c) `bool`
   d) `float`

2. What is the result of `10 == 10`?
   a) `10`
   b) `True`
   c) `False`
   d) An error

3. What does `and` require to return `True`?
   a) At least one side is `True`
   b) Both sides must be `True`
   c) Neither side is `True`
   d) Only the left side matters

4. What does `or` require to return `True`?
   a) Both sides must be `True`
   b) At least one side is `True`
   c) Both sides must be `False`
   d) It always returns `True`

5. What does `not True` evaluate to?
   a) `True`
   b) `False`
   c) `None`
   d) `1`

6. What is wrong with `if age = 18:`?
   a) Nothing, it works correctly
   b) `=` is assignment, not comparison, and this raises a `SyntaxError`
   c) `18` should be in quotes
   d) `if` is spelled incorrectly

7. What does `"5" == 5` return in Python?
   a) `True`
   b) `False`
   c) An error
   d) `"5"`

8. Which expression correctly checks if `day` is either `"Saturday"` or `"Sunday"`?
   a) `day == "Saturday" and day == "Sunday"`
   b) `day == "Saturday" or day == "Sunday"`
   c) `day = "Saturday" or "Sunday"`
   d) `day != "Saturday" and "Sunday"`

9. What happens when you compare a string to an integer using `>=`?
   a) Python converts the string automatically
   b) Python raises a `TypeError`
   c) Python always returns `False`
   d) Python always returns `True`

10. In `not (age >= 18 and is_member)`, what does the parentheses grouping ensure?
    a) That `not` only applies to `age >= 18`
    b) That `not` applies to the entire combined condition
    c) That the code will not run
    d) That `and` is evaluated after `not`

## True/False Questions

11. Comparison operators like `==` and `>` always produce a `bool` value. (True/False)

12. `and` returns `True` if at least one side is `True`. (True/False)

13. `"5" == 5` raises an error in Python. (True/False)

14. `=` and `==` do the same thing in Python. (True/False)

15. `not` reverses a boolean value. (True/False)

## Short Answer Questions

16. What is the difference between `=` and `==`?

17. Explain, using a truth table or your own words, when `and` produces `True`.

18. Why does `"5" == 5` return `False` instead of raising an error?

19. Why might comparing a string and an integer with `>=` raise an error when `==` between the same two values does not?

20. Describe a real-world decision (outside programming) that could be modeled using `and`, and one that could be modeled using `or`.

---

## Answer Key

1. c
2. b
3. b
4. b
5. b
6. b
7. b
8. b
9. b
10. b
11. True
12. False
13. False
14. False
15. True
16. `=` assigns a value to a variable, while `==` compares two values and returns a boolean indicating whether they are equal.
17. `and` produces `True` only when both the left side and the right side are `True`; if either side is `False`, the whole expression is `False`.
18. Python allows `==` between any two values regardless of type; a string and an integer are simply never considered equal to each other, so the comparison is valid and returns `False` rather than raising an error.
19. Equality (`==`) only needs to check whether two values represent the same thing, which is well-defined even across types (the answer is just "no"), while ordering comparisons (`>=`) require Python to know how to rank the values relative to each other, which is undefined between incompatible types like `str` and `int`.
20. Example for `and`: "I will go to the beach if it is sunny and I have the day off" (both conditions must hold). Example for `or`: "I will have dessert if I finish my dinner or it is my birthday" (either condition alone is enough).
