"""Lesson 03 - Exercise Solutions"""

# --- Exercise 1: Basic arithmetic on two variables ---
x = 12
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)


# --- Exercise 2: Seconds into minutes and leftover seconds ---
seconds = 90
minutes = seconds // 60
leftover_seconds = seconds % 60
print("Minutes:", minutes)
print("Leftover seconds:", leftover_seconds)


# --- Exercise 3: Exponent ---
print(2 ** 10)


# --- Exercise 4: Total cost ---
price = 9.99
quantity = 3
print(price * quantity)


# --- Exercise 5: Sensor reading as a percentage of max ---
reading = 98
max_reading = 120
percentage = reading / max_reading * 100
print(round(percentage, 1))


# --- Exercise 6: Splitting pizza slices among people ---
pizzas = 5
people = 12
slices_per_pizza = 8
total_slices = pizzas * slices_per_pizza

slices_each = total_slices // people
slices_left_over = total_slices % people
print("Slices each:", slices_each)
print("Slices left over:", slices_left_over)


# --- Exercise 7: Rectangle area and perimeter ---
width = 12.5
height = 7.25
area = width * height
perimeter = 2 * (width + height)
print("Area:", round(area, 2))
print("Perimeter:", round(perimeter, 2))


# --- Exercise 8: Average speed ---
distance_km = 42.195
time_hours = 3.5
average_speed = distance_km / time_hours
print("Average speed (km/h):", round(average_speed, 2))


# --- Exercise 9: Discount then tax ---
price = 45.00
discount_percent = 15
tax_percent = 8

discounted_price = price - (price * discount_percent / 100)
final_price = discounted_price + (discounted_price * tax_percent / 100)

print("Discounted price:", round(discounted_price, 2))
print("Final price:", round(final_price, 2))


# --- Exercise 10: Total seconds into hours, minutes, seconds ---
total_seconds = 9045

hours = total_seconds // 3600
remaining_after_hours = total_seconds % 3600

minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60

print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
