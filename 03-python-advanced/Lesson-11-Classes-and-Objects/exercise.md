# Lesson 11 — Exercises: Classes and Objects

## Easy

1. Create a `Book` class with attributes `title` and `author`, set in `__init__`. Add a method `describe()` that returns a string like `"'1984' by George Orwell"`. Create one book and print its description.

2. Create a `Circle` class that stores a `radius`. Add a method `area()` that returns the circle's area (`3.14159 * radius ** 2`). Create a circle with radius `5` and print its area.

3. Create a `Light` class with an attribute `is_on` that starts as `False`. Add methods `turn_on()` and `turn_off()` that change `is_on`. Print the value of `is_on` before and after calling `turn_on()`.

## Medium

4. Create a `Student` class with `name` and a list of `grades` (start empty). Add a method `add_grade(grade)` and a method `average()` that returns the average of all grades. Handle the case where there are no grades yet (return `0`).

5. Create a `Car` class with `make`, `model`, and `mileage` (starting at `0`). Add a method `drive(miles)` that increases `mileage` by that amount, and a method `info()` that prints `"<make> <model> — <mileage> miles"`.

6. Create a `TodoList` class with an empty list of tasks. Add methods `add_task(task)`, `complete_task(task)` (removes it from the list), and `show_tasks()` (prints all remaining tasks, or `"No tasks!"` if empty).

7. Create a `Temperature` class that stores a value in Celsius. Add methods `to_fahrenheit()` and `to_kelvin()` that return the converted values, without modifying the stored Celsius value.

## Hard

8. Create an `Inventory` class that stores products as a dictionary of `{name: quantity}`. Add methods `add_stock(name, amount)`, `remove_stock(name, amount)` (must not let quantity go below 0 — print a warning instead), and `report()` that prints every product and its quantity.

9. Create a `Login System` using a `User` class with `username` and a *hashed* password concept: store the password reversed as a simple stand-in for hashing (e.g. `"secret"` stored as `"terces"`). Add a method `check_password(attempt)` that reverses the attempt and compares it to the stored value, returning `True`/`False`.

10. Create an `ATM` class with a `balance` attribute and a `pin` attribute. Add a method `authenticate(pin)` that returns `True`/`False`, and a method `withdraw(pin, amount)` that only allows withdrawal if `authenticate(pin)` succeeds and there is enough balance; otherwise it should print an appropriate error message (`"Incorrect PIN."` or `"Insufficient funds."`).
