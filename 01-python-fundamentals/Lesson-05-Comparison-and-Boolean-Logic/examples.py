"""Lesson 05 - Comparison and Boolean Logic
All three lesson examples, executable as-is.
"""

# --- Example 1: Basic comparisons ---
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(b <= 20)


# --- Example 2: Combining conditions with and, or, not ---
age = 20
is_student = True
has_coupon = False

qualifies_for_discount = is_student and age >= 18
print(qualifies_for_discount)

gets_free_shipping = has_coupon or age >= 18
print(gets_free_shipping)

is_minor = not (age >= 18)
print(is_minor)


# --- Example 3: A practical example - a simple login check ---
stored_username = "admin"
stored_password = "secure123"

entered_username = "admin"
entered_password = "secure123"

username_correct = entered_username == stored_username
password_correct = entered_password == stored_password

login_successful = username_correct and password_correct
print("Login successful:", login_successful)

wrong_password_attempt = "wrongpass"
password_correct_2 = wrong_password_attempt == stored_password
print("Second attempt correct:", password_correct_2)
