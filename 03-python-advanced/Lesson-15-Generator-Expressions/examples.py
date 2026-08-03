"""
Lesson 15 - Generator Expressions
All three examples from lesson.md, ready to run as-is.
"""


def main():
    print("--- Example 1 ---")
    numbers = [1, 2, 3, 4, 5]
    squares_gen = (n * n for n in numbers)
    for value in squares_gen:
        print(value)

    print("\n--- Example 2 ---")
    prices = [19.99, 5.50, 42.00, 3.25, 100.00]
    total_expensive = sum(price for price in prices if price > 10)
    print(total_expensive)

    print("\n--- Example 3 ---")
    students = [
        {"name": "Ana", "score": 92},
        {"name": "Leo", "score": 58},
        {"name": "Sam", "score": 74},
        {"name": "Kim", "score": 40},
    ]

    passing_names = (s["name"] for s in students if s["score"] >= 60)
    for name in passing_names:
        print(f"{name} passed!")

    average_score = sum(s["score"] for s in students) / len(students)
    print(f"Class average: {average_score:.1f}")


if __name__ == "__main__":
    main()
