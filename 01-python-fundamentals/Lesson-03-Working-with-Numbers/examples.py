"""Lesson 03 - Working with Numbers
All three lesson examples, executable as-is.
"""

# --- Example 1: Basic arithmetic ---
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# --- Example 2: Floor division, modulo, and exponents ---
total_minutes = 130

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)

squared = 4 ** 2
cubed = 4 ** 3
print("4 squared:", squared)
print("4 cubed:", cubed)


# --- Example 3: A practical example - restaurant bill splitter ---
meal_cost = 60.00
tax_rate = 0.08
tip_rate = 0.15
number_of_people = 4

tax = meal_cost * tax_rate
tip = meal_cost * tip_rate
total = meal_cost + tax + tip

per_person = total / number_of_people

print("Meal cost:", meal_cost)
print("Tax:", round(tax, 2))
print("Tip:", round(tip, 2))
print("Total:", round(total, 2))
print("Amount per person:", round(per_person, 2))
