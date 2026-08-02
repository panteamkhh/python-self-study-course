"""
Lesson 08 - Arguments and Scope
Examples from lesson.md
"""


# Example 1 - Simple: default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def example_1():
    print(greet("Sara"))
    print(greet("Reza", "Welcome"))


# Example 2 - Intermediate: local variables don't leak out
def calculate_area(width, height):
    area = width * height
    return area


def example_2():
    print(calculate_area(4, 5))
    # print(area)  # would raise NameError - "area" is local to the function


# Example 3 - Real-World: averaging student grades
def average(*grades):
    return sum(grades) / len(grades)


def example_3():
    count = int(input())
    values = []
    for _ in range(count):
        values.append(float(input()))

    result = average(*values)
    print(f"{result:.2f}")


if __name__ == "__main__":
    example_1()
    example_2()
    # example_3() requires input, run separately
