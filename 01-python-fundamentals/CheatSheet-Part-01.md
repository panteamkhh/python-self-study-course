# Cheat Sheet — Part 01 (Lessons 01–05)

A one-page quick reference for everything covered in the first five lessons: printing output, variables, data types, arithmetic, type conversion, and boolean logic.

---

## Printing Output

| Syntax | Result |
|---|---|
| `print("text")` | Displays `text` |
| `print(a, b)` | Displays `a` and `b`, separated by a space |
| `# comment` | Ignored by Python; a note for humans |

---

## Variables and Data Types

| Type | Example | Description |
|---|---|---|
| `int` | `age = 25` | Whole number |
| `float` | `price = 9.99` | Decimal number |
| `str` | `name = "Alice"` | Text, in quotes |
| `bool` | `is_active = True` | `True` or `False` |

```python
type(x)     # returns the current data type of x
```

Rules for variable names: cannot start with a digit, are case-sensitive, and must be assigned before use.

---

## Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | True division (always `float`) | `5 / 2` | `2.5` |
| `//` | Floor division (whole number) | `5 // 2` | `2` |
| `%` | Modulo (remainder) | `5 % 2` | `1` |
| `**` | Exponent | `5 ** 2` | `25` |

**Order of operations:** parentheses, then `**`, then `*` `/` `//` `%`, then `+` `-` (left to right within the same level).

`round(value, decimals)` rounds a number for readable output (e.g., currency).

---

## Type Conversion

| Function | Converts to | Example |
|---|---|---|
| `int(x)` | integer | `int("42")` → `42` |
| `float(x)` | decimal | `float("3.5")` → `3.5` |
| `str(x)` | text | `str(42)` → `"42"` |
| `bool(x)` | boolean | `bool("")` → `False`, `bool("anything")` → `True` |

Important gotchas:
* `int()` on a float **truncates**, it does not round (`int(9.99)` → `9`).
* `int("abc")` raises `ValueError` — text must look like a real number.
* `bool("False")` is `True` — any non-empty string is "truthy." Compare text directly instead: `text == "True"`.
* `str(number)` is required before concatenating a number into a string with `+`.

---

## Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

All comparisons produce a `bool`.

## Boolean Operators

| Operator | Returns `True` when... |
|---|---|
| `and` | both sides are `True` |
| `or` | at least one side is `True` |
| `not` | flips the value (`not True` → `False`) |

Use parentheses to make grouping explicit when combining `and`, `or`, and `not` in one expression.

---

## Common Mistakes to Avoid

* Using `=` (assignment) where `==` (comparison) is needed.
* Forgetting quotes around text, or mismatching quote types.
* Expecting `/` to return an `int` — it always returns a `float`.
* Using `%` expecting a percentage calculation — it returns a remainder.
* Concatenating a number into a string without `str()` first.
* Assuming `bool("False")` is `False` — it is `True`.
* Dividing by zero — raises `ZeroDivisionError`.

---

## Best Practices

* Use descriptive variable names (`total_price`, not `tp`).
* Convert external data (form input, file contents) to the correct type before calculating with it.
* Use `round()` for any value shown to a user as currency.
* Use parentheses to make the order of operations and boolean logic unambiguous, even when not strictly required.
* Keep one clear idea per line of code — readability matters as much as correctness.
