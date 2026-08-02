"""
Lesson 08 - Arguments and Scope
Solutions to exercise.md
"""


# Exercise 1 - Power with a default exponent
def power(base, exponent=2):
    return base ** exponent
    # exponent defaults to 2, so calling power(5) squares 5 automatically.


# Exercise 2 - Full name with positional and keyword calls
def full_name(first, last):
    return f"{first} {last}"


def exercise_2():
    print(full_name("Ada", "Lovelace"))       # positional
    print(full_name(last="Turing", first="Alan"))  # keyword
    # Keyword arguments can be given in any order because they're matched by name.


# Exercise 3 - Local variable scope
def exercise_3():
    local_value = 42
    return local_value
    # "local_value" only exists while exercise_3 is running.
    # Trying to print it afterward raises a NameError because Python
    # discards local variables once the function call finishes.


# Exercise 4 - Apply a discount
def apply_discount(price, discount=0.1):
    return price * (1 - discount)
    # Multiplies price by the remaining fraction after the discount.


# Exercise 5 - Sum any number of arguments
def sum_all(*numbers):
    return sum(numbers)
    # *numbers collects all positional arguments into a tuple,
    # which sum() can add up directly.


# Exercise 6 - Update a global counter
counter = 0


def update_counter():
    global counter
    counter += 1
    # "global counter" tells Python to modify the existing global
    # variable instead of creating a new local one.


# Exercise 7 - Safe append avoiding mutable default argument
def safe_append(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection
    # Using None as the default and building a fresh list inside the
    # function avoids sharing one list across every call.


# Exercise 8 - Average using unpacking
def average(*values):
    return sum(values) / len(values)


def exercise_8():
    n = int(input())
    numbers = [float(input()) for _ in range(n)]
    result = average(*numbers)
    print(f"{result:.2f}")
    # The * unpacks the "numbers" list into separate arguments for average().


# Exercise 9 - Closures: a function that returns a function
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier
    # "multiplier" remembers "factor" from the enclosing scope even
    # after make_multiplier has finished running - this is a closure.


# Exercise 10 - Extra keyword arguments with **details
def describe_person(name, age, **details):
    print(f"{name}, {age} years old")
    for key, value in details.items():
        print(f"{key}: {value}")
    # **details collects any additional keyword arguments into a
    # dictionary, which can then be looped over.


if __name__ == "__main__":
    print(power(5))
    exercise_2()
    print(exercise_3())
    print(apply_discount(100))
    print(sum_all(1, 2, 3, 4))
    update_counter()
    update_counter()
    print(counter)
    print(safe_append("a"))
    print(safe_append("b"))
    double = make_multiplier(2)
    print(double(10))
    describe_person("Sara", 25, city="Tehran", job="Engineer")
