"""Lesson 02 - Variables and Data Types
All three lesson examples, executable as-is.
"""

# --- Example 1: Storing and printing simple values ---
age = 25
height = 1.75
name = "Alice"
is_student = True

print(age)
print(height)
print(name)
print(is_student)


# --- Example 2: Checking types and reassigning variables ---
score = 90
print(type(score))

score = "A"          # reassigned - now holds text instead of a number
print(type(score))
print(score)


# --- Example 3: A practical example - a student profile ---
student_name = "Maria Lopez"
student_id = 10432
gpa = 3.8
is_enrolled = True

print("Student Profile")
print("Name:", student_name)
print("ID:", student_id)
print("GPA:", gpa)
print("Currently enrolled:", is_enrolled)
