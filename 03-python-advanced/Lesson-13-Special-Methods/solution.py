"""
Lesson 13 - Special Methods (Dunder Methods)
Complete solutions for exercise.md
"""


# --- 1. Book (Easy) ----------------------------------------------------
# __str__ controls what print() shows.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


print(Book("Dune", "Frank Herbert"))


# --- 2. Fraction (Easy) ----------------------------------------------------

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


print(Fraction(3, 4))


# --- 3. Temperature (Easy) ----------------------------------------------------
# __eq__ compares by data, not by identity.

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __eq__(self, other):
        return self.degrees == other.degrees


print(Temperature(20) == Temperature(20))
print(Temperature(20) == Temperature(30))


# --- 4. Vector (Medium) ----------------------------------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)


# --- 5. Playlist (Medium) ----------------------------------------------------
# Making a custom class behave like a list.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]


playlist = Playlist(["Song A", "Song B", "Song C"])
print(len(playlist))
print(playlist[0])


# --- 6. Grade with __lt__ (Medium) ----------------------------------------------------
# sorted() uses __lt__ under the hood to compare objects.

class Grade:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return f"Grade({self.score})"


grades = [Grade(88), Grade(72), Grade(95)]
print(sorted(grades))


# --- 7. ShoppingCart (Medium) ----------------------------------------------------

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    def __len__(self):
        return len(self.items)

    def __str__(self):
        total = sum(price for _, price in self.items)
        return f"Cart total: ${total:.2f}"


cart = ShoppingCart()
cart.add("Book", 15.50)
cart.add("Pen", 10.00)
print(len(cart))
print(cart)


# --- 8. Matrix2x2 (Hard) ----------------------------------------------------

class Matrix2x2:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def __add__(self, other):
        return Matrix2x2(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d,
        )

    def __str__(self):
        return f"[{self.a} {self.b}]\n[{self.c} {self.d}]"


m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(5, 6, 7, 8)
print(m1 + m2)


# --- 9. Student sorting (Hard) ----------------------------------------------------

class Student:
    def __init__(self, name, average_grade):
        self.name = name
        self.average_grade = average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __repr__(self):
        return f"{self.name}({self.average_grade})"


students = [Student("Ana", 88), Student("Leo", 95), Student("Sam", 72)]
print(sorted(students))


# --- 10. JSONLikeObject (Hard) ----------------------------------------------------
# __getitem__ and __setitem__ let the object act like a dict.

class JSONLikeObject:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __len__(self):
        return len(self._data)


obj = JSONLikeObject()
obj["name"] = "Alice"
obj["age"] = 30
print(obj["name"])
print(len(obj))
