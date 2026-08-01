# Lesson 04 — Quiz

## Multiple Choice Questions

1. What does `int("42")` return?
   a) `"42"`
   b) `42.0`
   c) `42`
   d) An error

2. What does `str(100)` return?
   a) `100`
   b) `"100"`
   c) `100.0`
   d) `True`

3. What happens when you run `int("hello")`?
   a) It returns `0`
   b) It returns `"hello"`
   c) It raises a `ValueError`
   d) It returns `None`

4. What does `int(9.99)` return?
   a) `10`
   b) `9`
   c) `9.99`
   d) An error

5. What does `bool("False")` actually return?
   a) `False`
   b) `True`
   c) `"False"`
   d) An error

6. Why does `"Score: " + 95` raise an error?
   a) Because `95` is too large
   b) Because `+` cannot combine a string with an integer directly
   c) Because strings cannot be concatenated
   d) Because `Score:` is a reserved word

7. Which function converts a value into a decimal number?
   a) `str()`
   b) `int()`
   c) `float()`
   d) `bool()`

8. What is the correct way to build the message `"Total: 10"` from an integer `total = 10`?
   a) `"Total: " + total`
   b) `"Total: " + str(total)`
   c) `str("Total: " + total)`
   d) `"Total: ", total`

9. If `price_text = "3.5"`, which conversion correctly turns it into a usable number for arithmetic?
   a) `int(price_text)`
   b) `str(price_text)`
   c) `float(price_text)`
   d) `bool(price_text)`

10. What is the safest way to convert a text value like `"True"` or `"False"` into a genuine boolean matching its intended meaning?
    a) `bool(text_value)`
    b) `int(text_value)`
    c) Comparing it directly, e.g. `text_value == "True"`
    d) `str(text_value)`

## True/False Questions

11. `int()` rounds a float to the nearest whole number. (True/False)

12. `str()` converts any value into text. (True/False)

13. `bool("False")` returns `False`. (True/False)

14. `int("abc")` raises a `ValueError`. (True/False)

15. Data coming from a web form typically arrives already converted to the correct type. (True/False)

## Short Answer Questions

16. What is the difference between `int(9.99)` and `round(9.99)`?

17. Why must you use `str()` before concatenating a number with text using `+`?

18. Why does `bool("False")` return `True`, and what does this reveal about how Python decides if a string is "truthy"?

19. Give a real-world example (outside this lesson) of data that arrives as text but needs to be converted to a number before use.

20. What error does Python raise when you try to convert non-numeric text like `"twelve"` into an integer, and why does that error occur?

---

## Answer Key

1. c
2. b
3. c
4. b
5. b
6. b
7. c
8. b
9. c
10. c
11. False
12. True
13. False
14. True
15. False
16. `int(9.99)` truncates the decimal part, giving `9`, while `round(9.99)` rounds to the nearest whole number, giving `10`.
17. Because `+` between a string and any other type is undefined in Python; converting the number to a string first makes both sides compatible for concatenation.
18. `bool()` treats any non-empty string as "truthy," regardless of its content, so even the text `"False"` counts as `True` because it is a non-empty string, not because Python evaluates its meaning.
19. Examples include: an age typed into a web form, a price read from a text file, or a quantity entered through a command-line prompt — all of these arrive as text (`str`) and must be converted before arithmetic can be performed on them.
20. Python raises a `ValueError`, because `int()` can only interpret text that is made up of digits (optionally with a sign); it has no built-in understanding of number words like "twelve."
