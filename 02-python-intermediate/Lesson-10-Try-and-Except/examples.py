"""
Lesson 10 - Try and Except
Examples from lesson.md
"""


# Example 1 - Simple: catching a ValueError
def example_1():
    try:
        number = int("abc")
        print(number)
    except ValueError:
        print("Conversion failed!")


# Example 2 - Intermediate: catching multiple exception types
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"


def example_2():
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide(10, "two"))


# Example 3 - Real-World: dividing two user-provided numbers safely
def example_3():
    numerator = int(input())
    denominator = int(input())

    try:
        result = numerator / denominator
        print(f"{result:.2f}")
    except ZeroDivisionError:
        print("cannot divide by zero")


if __name__ == "__main__":
    example_1()
    example_2()
    # example_3() requires input, run separately
