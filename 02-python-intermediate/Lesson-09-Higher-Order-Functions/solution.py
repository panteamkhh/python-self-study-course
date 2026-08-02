"""
Lesson 09 - Higher-Order Functions
Solutions to exercise.md
"""


# Exercise 1 - Square via lambda
def exercise_1():
    square = lambda x: x * x
    print(square(6))
    # A lambda's single expression is implicitly returned.


# Exercise 2 - Larger of two numbers via lambda
def exercise_2():
    larger = lambda a, b: a if a > b else b
    print(larger(4, 9))
    # A conditional expression (ternary) fits neatly inside a lambda.


# Exercise 3 - Sort words by length
def exercise_3():
    words = ["banana", "kiwi", "fig", "apple"]
    sorted_words = sorted(words, key=len)
    print(sorted_words)
    # key=len tells sorted() to compare words by their length rather
    # than alphabetically.


# Exercise 4 - Sort tuples by age
def exercise_4():
    people = [("Sara", 30), ("Ali", 22), ("Reza", 27)]
    by_age = sorted(people, key=lambda person: person[1])
    print(by_age)
    # The lambda extracts the age (index 1) from each tuple for comparison.


# Exercise 5 - Apply an operation function
def apply_operation(func, a, b):
    return func(a, b)
    # func is treated as a value and simply called with a and b.


# Exercise 6 - Sort prices, most expensive first
def exercise_6():
    prices = [19.99, 5.50, 42.00, 12.25]
    most_expensive_first = sorted(prices, reverse=True)
    print(most_expensive_first)
    # reverse=True flips the default ascending order to descending.


# Exercise 7 - Sort strings by vowel count
def exercise_7():
    words = ["sky", "banana", "rhythm", "orange"]
    vowels = "aeiou"
    by_vowel_count = sorted(words, key=lambda w: sum(1 for ch in w if ch in vowels))
    print(by_vowel_count)
    # The lambda counts vowels in each word to use as the sort key.


# Exercise 8 - A function that returns a lambda
def make_power(exponent):
    return lambda base: base ** exponent
    # The returned lambda "remembers" exponent from the enclosing scope,
    # so it can be reused with different bases.


# Exercise 9 - Sort dictionaries by a key
def exercise_9():
    products = [
        {"name": "Mouse", "price": 25},
        {"name": "Keyboard", "price": 60},
        {"name": "Monitor", "price": 200},
    ]
    by_price = sorted(products, key=lambda product: product["price"])
    print(by_price)
    # The lambda reaches into each dictionary to pull out "price" for comparison.


# Exercise 10 - Rank students, tie-break by name
def exercise_10():
    n = int(input())
    students = []
    for _ in range(n):
        name, score = input().split()
        students.append((name, int(score)))

    ranked = sorted(students, key=lambda s: (-s[1], s[0]))

    for name, score in ranked:
        print(name)
    # Sorting by a tuple (-score, name) sorts primarily by score
    # descending (negating flips ascending into descending), and
    # ties are then broken alphabetically by name.


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    print(apply_operation(lambda a, b: a + b, 3, 4))
    exercise_6()
    exercise_7()
    triple = make_power(3)
    print(triple(2))
    exercise_9()
    # exercise_10() requires input, run separately
