# Lesson 13 — Exercises: Special Methods

## Easy

1. Create a class `Book` with `title` and `author`. Implement `__str__` so `print(book)` shows `"'Title' by Author"`.

2. Create a class `Fraction` with `numerator` and `denominator`. Implement `__str__` so it prints like `"3/4"`.

3. Create a class `Temperature` with a `degrees` attribute. Implement `__eq__` so two `Temperature` objects are equal if their `degrees` match.

## Medium

4. Create a class `Vector` with `x` and `y`. Implement `__add__` so two vectors can be added (`v1 + v2` returns a new `Vector` with summed components), and `__str__` to print it as `"(x, y)"`.

5. Create a class `Playlist` with a list of song names. Implement `__len__` so `len(playlist)` returns the number of songs, and `__getitem__` so `playlist[0]` returns the first song.

6. Create a class `Grade` with a numeric `score`. Implement `__lt__` (less than) so `Grade` objects can be compared with `<` based on their score. Sort a list of `Grade` objects using `sorted()`.

7. Create a class `ShoppingCart` that stores items as a list of `(name, price)` tuples. Implement `__len__` to return the number of items, and `__str__` to display the total price like `"Cart total: $25.50"`.

## Hard

8. Create a class `Matrix2x2` that stores four numbers `a, b, c, d` (representing a 2x2 matrix). Implement `__add__` (adds matrices element-wise) and `__str__` (prints as two rows, e.g. `"[a b]\n[c d]"`).

9. Create a class `Student` with `name` and `average_grade`. Implement `__eq__` and `__lt__` based on `average_grade` so a list of students can be sorted from lowest to highest average using `sorted()`.

10. Create a class `JSONLikeObject` that wraps a dictionary internally. Implement `__getitem__` so `obj["key"]` retrieves a value, `__setitem__` so `obj["key"] = value` sets a value, and `__len__` so `len(obj)` returns the number of keys. (Hint: `__setitem__(self, key, value)` is triggered by `obj[key] = value`.)
