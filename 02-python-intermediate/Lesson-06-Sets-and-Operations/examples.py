"""
Lesson 06 - Sets and Operations
Examples from lesson.md
"""


# Example 1 - Simple: unique letters in a word
def example_1():
    word = "banana"
    unique_letters = set(word)
    print(unique_letters)
    print(len(unique_letters))


# Example 2 - Intermediate: comparing two classes of students
def example_2():
    class_a = {"Ali", "Sara", "Reza", "Mona"}
    class_b = {"Sara", "Reza", "Kian"}

    both_classes = class_a & class_b
    only_a = class_a - class_b
    either_class = class_a | class_b

    print("In both:", both_classes)
    print("Only in A:", only_a)
    print("In either:", either_class)


# Example 3 - Real-World: shared numbers between two input lines
def example_3():
    line1 = input()
    line2 = input()

    set1 = set(line1.split())
    set2 = set(line2.split())

    common = set1 & set2

    if common:
        print(" ".join(sorted(common, key=int)))
    else:
        print()


if __name__ == "__main__":
    example_1()
    example_2()
    # example_3() requires two lines of input, run separately
