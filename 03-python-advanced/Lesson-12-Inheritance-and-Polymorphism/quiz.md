# Lesson 12 — Quiz: Inheritance and Polymorphism

## Multiple Choice (10)

1. What does inheritance allow a class to do?
   a) Delete methods from another class
   b) Reuse and extend attributes/methods of another class
   c) Run faster
   d) Avoid using `self`

2. In `class Dog(Animal):`, which is the parent class?
   a) `Dog`
   b) `Animal`
   c) Both
   d) Neither

3. What does "overriding" a method mean?
   a) Deleting the method entirely
   b) Defining a new version of an inherited method in the child class
   c) Renaming a method
   d) Calling a method twice

4. What does `super()` give you access to?
   a) The child class's own methods
   b) The parent class's methods
   c) Python's built-in functions
   d) Global variables

5. What is polymorphism?
   a) Having many unrelated classes
   b) The ability of different classes to respond to the same method call in their own way
   c) A type of loop
   d) A way to delete objects

6. If `Dog` inherits from `Animal` but does not define `__init__`, what happens when you create a `Dog`?
   a) It raises an error
   b) `Animal`'s `__init__` is used automatically
   c) The object has no attributes at all
   d) Python creates an empty `__init__`

7. What is wrong with checking `if type(shape) == Square:` inside a loop over mixed shape objects?
   a) Nothing, it's the best practice
   b) It defeats the purpose of polymorphism and must be updated for every new class
   c) It causes a syntax error
   d) `type()` doesn't work on objects

8. Which line correctly declares that `Cat` inherits from `Animal`?
   a) `class Cat: Animal`
   b) `class Cat(Animal):`
   c) `class Cat -> Animal:`
   d) `class Cat extends Animal:`

9. If a child class overrides `__init__` and does NOT call `super().__init__()`, what happens to the parent's setup code?
   a) It still runs automatically
   b) It does not run, unless explicitly called
   c) Python raises an error
   d) It runs twice

10. What does `v.move` (without parentheses) do, compared to `v.move()`?
    a) They are identical
    b) `v.move` calls the method immediately
    c) `v.move` refers to the method object itself, without calling it
    d) `v.move` raises a `TypeError`

## True / False (5)

11. A subclass can override some methods from its parent while still inheriting others unchanged.
12. `super()` can only be used inside `__init__`.
13. Polymorphism lets code work with objects of different classes without knowing their exact type in advance.
14. A class can only inherit from one parent class in Python (in the basic single-inheritance style taught here).
15. Overriding a method in a child class permanently deletes the parent's version from the parent class itself.

## Short Answer (5)

16. In your own words, explain what "inheritance" means in Python.
17. What is the purpose of calling `super().__init__(...)` inside a child class's constructor?
18. Give a short example (in words, not code) of polymorphism from everyday life (outside of programming).
19. What happens if a child class defines a method with the same name as one in its parent class?
20. Why is polymorphism often better than writing `if/elif` chains that check an object's type?

---

## Answer Key

1. b
2. b
3. b
4. b
5. b
6. b
7. b
8. b
9. b
10. c
11. True
12. False
13. True
14. True
15. False
16. Inheritance is when a class (child) reuses and can extend the attributes and methods defined by another class (parent).
17. It runs the parent class's constructor so the child class doesn't have to duplicate the parent's setup logic.
18. Example answer: different musicians "perform" in their own way — a guitarist strums, a drummer hits drums — but you can say "perform" for all of them the same way (any reasonable analogy is acceptable).
19. The child class's method overrides the parent's — calling it on a child object runs the child's version.
20. Polymorphism keeps code simpler and easier to extend — adding a new class doesn't require modifying existing conditional logic, since each class handles its own behavior.
