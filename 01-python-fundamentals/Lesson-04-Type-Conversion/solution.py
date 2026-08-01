"""Lesson 04 - Exercise Solutions"""

# --- Exercise 1: String to int, then add 5 ---
value = int("15") + 5
print(value)


# --- Exercise 2: Number to string, check its type ---
number_as_text = str(42)
print(type(number_as_text))


# --- Exercise 3: String to float, then multiply ---
value = float("3.75") * 2
print(value)


# --- Exercise 4: Concatenating a converted integer ---
quantity = 8
print("Quantity: " + str(quantity))


# --- Exercise 5: Total cost from text values ---
price_text = "19.99"
quantity_text = "3"

price = float(price_text)
quantity = int(quantity_text)
total_cost = price * quantity
print(total_cost)


# --- Exercise 6: Float to int truncates, it does not round ---
temperature = 36.6
temperature_int = int(temperature)
print(temperature_int)
# int() truncates the decimal part rather than rounding, so 36.6
# becomes 36, not 37. round() would be used if rounding was intended.


# --- Exercise 7: Building a message from converted input ---
raw_input = "100"
number = int(raw_input)
message = "You entered: " + str(number)
print(message)


# --- Exercise 8: bool() on text does not check its meaning ---
flag_text = "False"
print(bool(flag_text))          # True - any non-empty string is truthy

corrected_flag = flag_text == "True"
print(corrected_flag)           # False - compares the actual text


# --- Exercise 9: Product summary from text values ---
name_text = "Notebook"
price_text = "4.50"
qty_text = "20"

price = float(price_text)
qty = int(qty_text)
total_value = price * qty

summary = name_text + " - total stock value: " + str(total_value)
print(summary)


# --- Exercise 10: Seconds to hours and minutes, as a message ---
seconds_text = "5000"
total_seconds = int(seconds_text)

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60

result_message = str(hours) + " hours and " + str(minutes) + " minutes"
print(result_message)
