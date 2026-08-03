# Lesson 12 — Exercises: Inheritance and Polymorphism

## Easy

1. Create a base class `Employee` with `name` and `salary`. Create a subclass `Manager` that inherits from it without adding anything new. Create a `Manager` and print their `name` and `salary`.

2. Create a class `Bird` with a method `fly()` that returns `"Flying high!"`. Create a subclass `Penguin` that overrides `fly()` to return `"Penguins can't fly, but they can swim!"`. Create one of each and print the results.

3. Create a base class `Shape` with a method `describe()` returning `"I am a shape"`. Create a subclass `Triangle` that overrides `describe()` to return `"I am a triangle"`. Print both descriptions.

## Medium

4. Create a class `Employee` with `__init__(self, name, salary)`. Create a subclass `Manager` with `__init__(self, name, salary, team_size)` that uses `super()` to set `name` and `salary`, and also stores `team_size`. Print all three values for a manager.

5. Create a class `Vehicle` with a method `fuel_type()` returning `"Unknown"`. Create subclasses `ElectricCar` (returns `"Electric"`) and `GasCar` (returns `"Gasoline"`). Put instances of both in a list and print each one's `fuel_type()` in a loop.

6. Create a class `PaymentMethod` with a method `process(amount)` that returns `f"Processing ${amount} via generic method"`. Create subclasses `CreditCard` and `PayPal`, each overriding `process()` with their own message. Loop through a list of both and call `process(50)` on each.

7. Create a base class `Student` with `name` and a method `status()` returning `"Regular student"`. Create a subclass `HonorsStudent` that overrides `status()` to return `"Honors student"` — but have it also call `super().status()` and combine both messages into one string.

## Hard

8. Build an inventory/grade-book style hierarchy: a class `Product` with `name` and `price`, and a method `final_price()` that just returns `price`. Create a subclass `DiscountedProduct` that adds a `discount_percent` and overrides `final_price()` to apply the discount. Create a small list of mixed `Product` and `DiscountedProduct` objects and print each one's final price using a single loop (polymorphism — no `type()` checks allowed).

9. Create a class `Animal` with `name` and a method `speak()` returning `"..."`. Create three subclasses `Dog`, `Cat`, and `Snake`, each overriding `speak()` differently. Write a function `animal_chorus(animals)` that takes a list of animals and returns a single string joining every animal's `speak()` result, separated by commas.

10. Model a simple ATM login system with roles: a base class `Account` with `username`, `pin`, and a method `access_level()` returning `"basic"`. Create a subclass `AdminAccount` that overrides `access_level()` to return `"admin"` and adds a method `reset_account(other_account)` (only usable by admin accounts) that resets `other_account`'s pin to `"0000"`. Demonstrate a regular account being reset by an admin account.
