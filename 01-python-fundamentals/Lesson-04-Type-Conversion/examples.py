"""Lesson 04 - Type Conversion
All three lesson examples, executable as-is.
"""

# --- Example 1: Converting user-style text input to numbers ---
age_text = "28"
age_number = int(age_text)

next_year = age_number + 1
print(next_year)
print(type(age_number))


# --- Example 2: Building a message that mixes numbers and text ---
score = 87
message = "Your score is " + str(score) + " points."
print(message)

pi_value = 3.14159
label = "Pi is approximately " + str(round(pi_value, 2))
print(label)


# --- Example 3: A practical example - parsing form-style data ---
form_age = "34"
form_height = "1.82"
form_subscribed = "True"

age = int(form_age)
height = float(form_height)
subscribed = form_subscribed == "True"   # manual boolean check, see lesson note

print("Age:", age, type(age))
print("Height:", height, type(height))
print("Subscribed:", subscribed, type(subscribed))
