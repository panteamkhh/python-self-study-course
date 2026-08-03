"""
Lesson 14 - Generators and Yield
Complete solutions for exercise.md
"""


# --- 1. count_up_to (Easy) ----------------------------------------------------

def count_up_to(n):
    for i in range(1, n + 1):
        yield i


for value in count_up_to(5):
    print(value)


# --- 2. squares (Easy) ----------------------------------------------------

def squares(n):
    for i in range(1, n + 1):
        yield i * i


for value in squares(5):
    print(value)


# --- 3. first_n_letters (Easy) ----------------------------------------------------

def first_n_letters(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet[:n]:
        yield letter


for letter in first_n_letters(5):
    print(letter)


# --- 4. even_up_to (Medium) ----------------------------------------------------

def even_up_to(n):
    current = 0
    while current <= n:
        yield current
        current += 2


gen = even_up_to(20)
for _ in range(4):
    print(next(gen))


# --- 5. countdown with final message (Medium) ----------------------------------------------------

def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Liftoff!"


for value in countdown(3):
    print(value)


# --- 6. fibonacci (Medium) ----------------------------------------------------

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


for value in fibonacci(20):
    print(value)


# --- 7. filter_long_words (Medium) ----------------------------------------------------

def filter_long_words(words, min_length):
    for word in words:
        if len(word) >= min_length:
            yield word


for word in filter_long_words(["cat", "elephant", "dog", "hippopotamus"], 4):
    print(word)


# --- 8. paginate (Hard) ----------------------------------------------------

def paginate(items, page_size):
    for start in range(0, len(items), page_size):
        yield items[start:start + page_size]


for page in paginate([1, 2, 3, 4, 5, 6, 7], 3):
    print(page)


# --- 9. unique_values (Hard) ----------------------------------------------------
# Tracks seen values manually while yielding one at a time.

def unique_values(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
            yield item


for value in unique_values([1, 2, 2, 3, 1, 4]):
    print(value)


# --- 10. Todo stream generators (Hard) ----------------------------------------------------

def simulate_todo_stream(tasks):
    for task in tasks:
        if not task["done"]:
            yield task["name"]


def mark_all_done(tasks):
    for task in tasks:
        task["done"] = True
        yield task


todo_items = [
    {"name": "Buy milk", "done": False},
    {"name": "Walk dog", "done": True},
    {"name": "Read book", "done": False},
]

print(list(simulate_todo_stream(todo_items)))
for task in mark_all_done(todo_items):
    print(task)
