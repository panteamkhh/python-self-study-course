"""
Lesson 09 - Higher-Order Functions
Examples from lesson.md
"""


# Example 1 - Simple: a lambda as a standalone function
def example_1():
    double = lambda x: x * 2
    print(double(7))
    print((lambda x, y: x + y)(3, 4))


# Example 2 - Intermediate: sorting a list with a custom key
def example_2():
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    by_score = sorted(students, key=lambda student: student[1], reverse=True)

    for name, score in by_score:
        print(name, score)


# Example 3 - Real-World: ranking students by score, name only
def example_3():
    n = int(input())
    students = []
    for _ in range(n):
        name, score = input().split()
        students.append((name, int(score)))

    ranked = sorted(students, key=lambda student: student[1], reverse=True)

    for name, score in ranked:
        print(name)


if __name__ == "__main__":
    example_1()
    example_2()
    # example_3() requires input, run separately
