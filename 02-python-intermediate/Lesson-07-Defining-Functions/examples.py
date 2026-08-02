"""
Lesson 07 - Defining Functions
Examples from lesson.md
"""


# Example 1 - Simple: a function with no parameters
def say_hello():
    print("Hello there!")


def example_1():
    say_hello()
    say_hello()


# Example 2 - Intermediate: a function that returns a value
def square(number):
    return number * number


def example_2():
    result = square(5)
    print(result)
    print(square(3) + square(4))


# Example 3 - Real-World: checking if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]


def example_3():
    text = input()
    if is_palindrome(text):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    example_1()
    example_2()
    # example_3() requires input, run separately
