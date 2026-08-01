"""Lesson 02 - Exercise Solutions"""

# --- Exercise 1: City variable ---
# A single string variable, printed directly.
city = "Barcelona"
print(city)


# --- Exercise 2: First and last name on one line ---
# print() accepts multiple comma-separated arguments.
first_name = "Alice"
last_name = "Nguyen"
print(first_name, last_name)


# --- Exercise 3: Temperature with its type ---
temperature = 98.6
print(temperature)
print(type(temperature))


# --- Exercise 4: Boolean with a descriptive sentence ---
is_raining = False
print("Is it raining?", is_raining)


# --- Exercise 5: Reassigning a price ---
# The same variable name can point to a new value.
price = 19.99
price = 24.99
print(price)


# --- Exercise 6: Book description with four variables ---
title = "Automate the Boring Stuff"
author = "Al Sweigart"
year = 2015
in_stock = True

print("Title:", title)
print("Author:", author)
print("Year:", year)
print("In stock:", in_stock)


# --- Exercise 7: Same number, two different types ---
count = 10
count_text = "10"
print(type(count))
print(type(count_text))


# --- Exercise 8: Reassigning types on purpose ---
value = 5
print(type(value))
value = 5.0
print(type(value))
value = "five"
print(type(value))


# --- Exercise 9: Store product summary ---
product_name = "Wireless Mouse"
product_price = 29.99
quantity_in_stock = 42
on_sale = True

print("Product Summary")
print("Name:", product_name)
print("Price:", product_price)
print("Quantity in stock:", quantity_in_stock)
print("On sale:", on_sale)


# --- Exercise 10: Game character status report ---
character_name = "Elandor"
health = 100
attack_power = 15.5
is_alive = True

print("Character Status")
print("Name:", character_name)
print("Health:", health, "| Type:", type(health))
print("Attack power:", attack_power, "| Type:", type(attack_power))
print("Alive:", is_alive)
