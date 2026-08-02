"""
Lesson 07 - Defining Functions
Solutions to exercise.md
"""


# Exercise 1 - Greet
def greet(name):
    return f"Hello, {name}!"
    # f-string inserts the "name" argument directly into the returned text.


# Exercise 2 - Is even
def is_even(number):
    return number % 2 == 0
    # The modulo operator gives the remainder of division by 2;
    # a remainder of 0 means the number is even.


# Exercise 3 - Add three numbers
def add_three(a, b, c):
    return a + b + c
    # Straightforward sum of all three parameters.


# Exercise 4 - Is palindrome
def is_palindrome(word):
    return word == word[::-1]
    # word[::-1] reverses the string; comparing it to the original
    # tells us whether it reads the same both ways.


# Exercise 5 - Count vowels
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count
    # Loops through each letter and checks membership in the vowels string.


# Exercise 6 - Max of three without max()
def max_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest
    # Starts by assuming "a" is largest, then updates the guess whenever
    # a bigger value is found.


# Exercise 7 - Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
    # Applies the standard conversion formula directly.


# Exercise 8 - Is prime
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
    # Checks divisibility only up to the square root of the number,
    # since a larger factor would need a matching smaller one already found.


# Exercise 9 - Reverse the order of words
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))
    # Splits the sentence into a list of words, reverses that list's
    # order, then joins the words back with spaces.


# Exercise 10 - Factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    # Multiplies result by every integer from 1 to n; if n is 0,
    # the loop never runs and result stays 1, which is correct.


if __name__ == "__main__":
    print(greet("Sara"))
    print(is_even(10))
    print(add_three(1, 2, 3))
    print(is_palindrome("racecar"))
    print(count_vowels("hello"))
    print(max_of_three(3, 9, 5))
    print(celsius_to_fahrenheit(100))
    print(is_prime(17))
    print(reverse_words("I love Python"))
    print(factorial(5))
