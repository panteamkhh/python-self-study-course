# Lesson 11 — Quiz: Classes and Objects

## Multiple Choice (10)

1. What is a class in Python?
   a) A built-in function
   b) A blueprint for creating objects
   c) A type of loop
   d) A variable

2. What is an object?
   a) The class itself
   b) A specific instance created from a class
   c) A method inside a class
   d) A Python keyword

3. What does `self` refer to inside a method?
   a) The class definition
   b) The module the class is in
   c) The specific object the method is called on
   d) Nothing — it's optional

4. Which method is automatically called when you create a new object?
   a) `__str__`
   b) `__new__`
   c) `__init__`
   d) `__create__`

5. What happens if you forget `self` as the first parameter of a method?
   a) Nothing, it works fine
   b) Python raises a `TypeError` when the method is called
   c) The method becomes a class attribute
   d) Python renames it automatically

6. How do you store a value as an attribute on an object inside `__init__`?
   a) `value = x`
   b) `self.value = x`
   c) `this.value = x`
   d) `attr(value) = x`

7. What is the danger of using a mutable default argument like `items=[]`?
   a) It causes a syntax error
   b) The list is shared across all objects created without an argument
   c) It makes the class slower
   d) There is no danger

8. Given `my_dog = Dog("Rex")`, which correctly accesses the dog's name?
   a) `Dog.name`
   b) `my_dog.name`
   c) `name.my_dog`
   d) `self.name`

9. What do all objects created from the same class share?
   a) Their attribute values
   b) Their memory address
   c) The methods defined by the class
   d) Nothing

10. What is the correct way to call a method on an object?
    a) `ClassName.method()`
    b) `method(object)`
    c) `object.method()`
    d) `self.method()`

## True / False (5)

11. A class can create many independent objects, each with its own data.
12. `self` must always be explicitly passed as an argument when calling a method (e.g. `my_dog.bark(my_dog)`).
13. `__init__` is optional — a class can be defined without it.
14. Two objects created from the same class always have identical attribute values.
15. Attributes set with `self.` persist for as long as the object exists.

## Short Answer (5)

16. In one sentence, explain the difference between a class and an object.
17. What is the purpose of the `__init__` method?
18. Why must every regular method include `self` as its first parameter?
19. What error occurs if you try to access an attribute that was never set with `self.`?
20. Give one real-world example (outside this lesson) of something that could be modeled as a class, and name two attributes it might have.

---

## Answer Key

1. b
2. b
3. c
4. c
5. b
6. b
7. b
8. b
9. c
10. c
11. True
12. False
13. True
14. False
15. True
16. A class is the blueprint/template that defines attributes and behavior; an object is a specific instance created from that blueprint with its own data.
17. `__init__` is the constructor — it runs automatically when a new object is created and is used to set up the object's initial attributes.
18. `self` lets the method know which specific object it should read/modify data on; without it, the method has no way to access that object's attributes.
19. `AttributeError`
20. Example answer: a `Car` class with attributes `make` and `model` (any reasonable real-world example with two attributes is acceptable).
