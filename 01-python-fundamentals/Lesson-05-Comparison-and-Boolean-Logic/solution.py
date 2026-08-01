"""Lesson 05 - Exercise Solutions"""

# --- Exercise 1: Greater than comparison ---
x = 15
y = 9
print(x > y)


# --- Exercise 2: Password equality check ---
password = "letmein"
print(password == "letmein123")


# --- Exercise 3: Not equal comparison ---
temperature = 72
print(temperature != 100)


# --- Exercise 4: Flipping a boolean with not ---
is_logged_in = True
print(not is_logged_in)


# --- Exercise 5: Age range check with and ---
age = 16
print(age >= 18 and age <= 65)


# --- Exercise 6: Weekend check with or ---
day = "Friday"
print(day == "Saturday" or day == "Sunday")


# --- Exercise 7: Purchase eligibility ---
stock = 0
is_preorder = True
can_be_purchased = stock > 0 or is_preorder
print(can_be_purchased)


# --- Exercise 8: Full access check ---
username = "guest"
role = "admin"
has_full_access = role == "admin" and username != "guest"
print(has_full_access)


# --- Exercise 9: VIP lounge access ---
has_ticket = True
is_vip = False
age = 15
can_enter_vip_lounge = has_ticket and (is_vip or age >= 21)
print(can_enter_vip_lounge)


# --- Exercise 10: Transaction approval with overdraft rule ---
balance = 250
withdrawal_amount = 300
is_overdraft_allowed = False

transaction_approved = balance >= withdrawal_amount or is_overdraft_allowed
print(transaction_approved)
