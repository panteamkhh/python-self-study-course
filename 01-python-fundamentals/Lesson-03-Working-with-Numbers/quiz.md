# Lesson 03 — Quiz

## Multiple Choice Questions

1. What does `10 / 3` return in Python?
   a) `3`
   b) `3.3333333333333335`
   c) `1`
   d) An error

2. What does `10 // 3` return?
   a) `3.33`
   b) `3`
   c) `1`
   d) `0`

3. What does `10 % 3` return?
   a) `3`
   b) `1`
   c) `0.33`
   d) `10`

4. What is the result of `2 ** 3`?
   a) `6`
   b) `5`
   c) `8`
   d) `9`

5. What is the result of `2 + 3 * 4`?
   a) `20`
   b) `14`
   c) `24`
   d) `9`

6. What does `/` always return in Python, regardless of the numbers used?
   a) An `int`
   b) A `float`
   c) A `bool`
   d) A `str`

7. What happens when you divide a number by zero using `/`?
   a) Python returns `0`
   b) Python returns `None`
   c) Python raises a `ZeroDivisionError`
   d) Python rounds up automatically

8. Which operator gives you only the remainder of a division?
   a) `/`
   b) `//`
   c) `%`
   d) `**`

9. What built-in function would you use to round `3.14159` to 2 decimal places?
   a) `format()`
   b) `round(3.14159, 2)`
   c) `int(3.14159)`
   d) `truncate(3.14159, 2)`

10. In `price * (discount_percent / 100)`, what is the purpose of the parentheses?
    a) They are purely decorative
    b) They force the division to happen before the multiplication
    c) They convert the result to a string
    d) They cause an error

## True/False Questions

11. `/` in Python always returns a whole number when both operands are whole numbers. (True/False)

12. `//` discards the decimal part of a division result. (True/False)

13. `%` calculates a percentage automatically. (True/False)

14. Python follows standard mathematical order of operations (PEMDAS). (True/False)

15. Dividing any number by zero using `/` raises an error in Python. (True/False)

## Short Answer Questions

16. Explain the difference between `/` and `//` in your own words.

17. What does the `%` operator actually compute, and give one real-world scenario where it is useful.

18. Why does `2 + 3 * 4` evaluate to `14` instead of `20`?

19. Why might a beginner mistakenly use `%` when they meant to calculate a percentage discount?

20. What is the purpose of the `round()` function, and why is it commonly used with currency calculations?

---

## Answer Key

1. b
2. b
3. b
4. c
5. b
6. b
7. c
8. c
9. b
10. b
11. False
12. True
13. False
14. True
15. True
16. `/` (true division) always returns a float, even when the numbers divide evenly, while `//` (floor division) divides and then discards anything after the decimal point, returning the whole number of times one value fits into another.
17. `%` returns the remainder left over after division; it's useful for problems like determining how many items are left over after filling complete groups, or checking whether a number is even/odd.
18. Python follows standard operator precedence, performing multiplication before addition unless parentheses specify a different order, so `3 * 4` is computed first, giving `12`, then `2` is added.
19. The `%` symbol is commonly associated with "percent" in everyday language, but in Python it is the remainder operator, not a percentage calculation — a beginner may transfer the everyday meaning of the symbol without realizing Python interprets it differently.
20. `round()` rounds a number to a specified number of decimal places; it's commonly used with currency because money is conventionally displayed with exactly two decimal places, and raw calculations can otherwise produce long, unreadable decimals.
