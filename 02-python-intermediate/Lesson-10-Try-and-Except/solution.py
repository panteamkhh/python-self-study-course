"""
Lesson 10 - Try and Except
Solutions to exercise.md
"""


# Exercise 1 - Catch a ValueError
def exercise_1():
    try:
        number = int("hello")
        print(number)
    except ValueError:
        print("Not a number")
    # int() cannot parse "hello", so it raises ValueError, which is caught.


# Exercise 2 - Catch a ZeroDivisionError
def exercise_2():
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    # Dividing by 0 raises ZeroDivisionError, which is caught here.


# Exercise 3 - Catch an IndexError
def exercise_3():
    items = [1, 2, 3]
    try:
        print(items[10])
    except IndexError:
        print("Index out of range")
    # Accessing an index beyond the list's length raises IndexError.


# Exercise 4 - Safe integer conversion
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
    # Returns None instead of crashing when conversion isn't possible.


# Exercise 5 - Safe division
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"
    # Returns a descriptive placeholder instead of crashing on b == 0.


# Exercise 6 - Catch a KeyError
def exercise_6():
    data = {"name": "Sara"}
    try:
        print(data["age"])
    except KeyError:
        print("Key not found")
    # Accessing a missing dictionary key raises KeyError.


# Exercise 7 - try/except/else
def exercise_7():
    text = "3.14"
    try:
        value = float(text)
    except ValueError:
        print("Conversion failed")
    else:
        print("Success")
    # else only runs when the try block completes without raising an error.


# Exercise 8 - Parse numbers, skipping invalid ones
def parse_numbers(values):
    parsed = []
    for value in values:
        try:
            parsed.append(int(value))
        except ValueError:
            continue
    return parsed
    # Each value is attempted individually; failures are simply skipped
    # with "continue" instead of stopping the whole loop.


# Exercise 9 - Handle both ValueError and ZeroDivisionError
def exercise_9():
    try:
        a = int(input())
        b = int(input())
        print(a / b)
    except ValueError:
        print("Please enter valid integers")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    # Each possible failure gets its own specific, descriptive message.


# Exercise 10 - Safe lookup with finally
def safe_lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return "missing"
    finally:
        print("Lookup attempted")
    # finally always runs, whether the lookup succeeded or raised KeyError.


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    print(safe_int("42"), safe_int("abc"))
    print(safe_divide(10, 2), safe_divide(10, 0))
    exercise_6()
    exercise_7()
    print(parse_numbers(["1", "two", "3", "four", "5"]))
    # exercise_9() requires input, run separately
    print(safe_lookup({"a": 1}, "a"))
    print(safe_lookup({"a": 1}, "b"))
