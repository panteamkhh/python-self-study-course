"""
Lesson 06 - Sets and Operations
Solutions to exercise.md
"""


# Exercise 1 - Count unique values in a list
def exercise_1():
    numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    unique_numbers = set(numbers)
    print(len(unique_numbers))
    # Turning the list into a set removes duplicates automatically,
    # so its length is the count of distinct values.


# Exercise 2 - Do two words share a common letter?
def exercise_2():
    word1 = "hello"
    word2 = "world"
    shares_letter = bool(set(word1) & set(word2))
    print(shares_letter)
    # Converting both words to sets and intersecting them shows any
    # shared letters; bool() turns a non-empty set into True.


# Exercise 3 - Add and remove from a set
def exercise_3():
    fruits = {"apple", "banana", "orange"}
    fruits.add("grape")
    fruits.remove("banana")
    print(fruits)
    # .add() inserts a new unique item; .remove() deletes an existing one.


# Exercise 4 - Numbers in line 1 but not line 2, sorted
def exercise_4():
    line1 = "10 20 30 40"
    line2 = "20 40"
    set1 = set(line1.split())
    set2 = set(line2.split())
    difference = set1 - set2
    print(" ".join(sorted(difference, key=int)))
    # Difference keeps only values exclusive to set1; sorting by int
    # avoids alphabetical ordering of number strings ("10" before "2").


# Exercise 5 - Skills unique to each candidate
def exercise_5():
    candidate_a = {"Python", "SQL", "Excel"}
    candidate_b = {"Python", "Java", "Excel"}
    unique_skills = candidate_a ^ candidate_b
    print(sorted(unique_skills))
    # Symmetric difference (^) returns items that belong to exactly
    # one of the two sets, which is exactly "not shared by both".


# Exercise 6 - Subset check
def exercise_6():
    set_a = {1, 2}
    set_b = {1, 2, 3, 4}
    print("yes" if set_a <= set_b else "no")
    # The <= operator (or .issubset()) checks whether every element
    # of set_a also appears in set_b.


# Exercise 7 - Unique email domains
def exercise_7():
    emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@gmail.com"]
    domains = {email.split("@")[1] for email in emails}
    print(domains)
    # A set comprehension extracts the domain from each email and
    # automatically discards repeated domains.


# Exercise 8 - Words common to three lines
def exercise_8():
    line1 = "python is fun"
    line2 = "python is powerful"
    line3 = "python is easy"
    words1 = set(line1.split())
    words2 = set(line2.split())
    words3 = set(line3.split())
    common_words = words1 & words2 & words3
    print(common_words)
    # Chaining & across all three sets keeps only words present
    # in every one of them.


# Exercise 9 - Remove reverse-duplicate pairs
def exercise_9():
    pairs = [(1, 2), (2, 1), (3, 4), (4, 3), (5, 6)]
    unique_pairs = set()
    for a, b in pairs:
        # frozenset ignores order, so (1, 2) and (2, 1) become equal
        unique_pairs.add(frozenset((a, b)))
    print(unique_pairs)
    # Storing each pair as a frozenset treats (1, 2) and (2, 1) as the
    # same entry, since sets don't care about element order.


# Exercise 10 - Count of users who did only one action
def exercise_10():
    liked = {"u1", "u2", "u3", "u4"}
    commented = {"u3", "u4", "u5"}
    only_one_action = liked ^ commented
    print(len(only_one_action))
    # Symmetric difference gives exactly the users present in one
    # set but not the other; len() then counts them.


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()
