"""
Lesson 15 - Generator Expressions
Complete solutions for exercise.md
"""


# --- 1. Doubling numbers (Easy) ----------------------------------------------------

numbers = [1, 2, 3, 4, 5]
doubled = (n * 2 for n in numbers)
for value in doubled:
    print(value)


# --- 2. Word lengths (Easy) ----------------------------------------------------

words = ["hi", "hello", "hey"]
lengths = (len(word) for word in words)
for length in lengths:
    print(length)


# --- 3. Divisible by 3 (Easy) ----------------------------------------------------

divisible_by_3 = (n for n in range(1, 11) if n % 3 == 0)
for value in divisible_by_3:
    print(value)


# --- 4. Celsius to Fahrenheit with max() (Medium) ---------------------------------------

temps_celsius = [0, 20, 37, 100]
highest_f = max(c * 9 / 5 + 32 for c in temps_celsius)
print(highest_f)


# --- 5. Sum of prices above 15 (Medium) ----------------------------------------------------

prices = [12.5, 45.0, 3.75, 89.99, 20.0]
total = sum(price for price in prices if price > 15)
print(total)


# --- 6. Names starting with uppercase (Medium) ------------------------------------------

names = ["Alice", "bob", "Charlie", "dave"]
capitalized_names = (name for name in names if name[0].isupper())
for name in capitalized_names:
    print(name)


# --- 7. Inventory items in stock (Medium) ----------------------------------------------------

inventory = [
    {"item": "Pen", "qty": 5},
    {"item": "Book", "qty": 0},
    {"item": "Notebook", "qty": 12},
]
in_stock = (entry["item"] for entry in inventory if entry["qty"] > 0)
for item in in_stock:
    print(item)


# --- 8. Total word count (Hard) ----------------------------------------------------

sentences = [
    "I love Python",
    "Generators are fast",
    "Lists use more memory",
]
total_words = sum(len(sentence.split()) for sentence in sentences)
print(total_words)


# --- 9. Matrix row sums (Hard) ----------------------------------------------------

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sums = (sum(row) for row in matrix)
for row_sum in row_sums:
    print(row_sum)


# --- 10. Active user count and names (Hard) ----------------------------------------------------

users = [
    {"name": "Ana", "active": True},
    {"name": "Leo", "active": False},
    {"name": "Sam", "active": True},
]

active_count = sum(user["active"] for user in users)
print(active_count)

active_names = list(name for name in (u["name"] for u in users if u["active"]))
print(active_names)
