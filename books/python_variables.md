# Python Variables

## Overview

Imagine you’re cooking with a kitchen station. You need a bowl, a spoon, and a recipe card to hold your ingredients and steps. In programming, a variable is like that bowl and recipe card: a named storage location that holds a value (like a number or text) so you can use it later in your program.

🎯 Learning Objectives
- Define what a variable is and how to name it in Python.
- Create and assign values to variables using different data types.
- Understand basic rules for valid variable names and common naming conventions.
- Use variables in simple operations and print their values.
- Recognize when to update a variable’s value (reassignment).

Python variables are fundamental building blocks. They let you store data, perform computations, and make your programs behave intelligently. Let’s break down the concept from first principles and build up with hands-on practice.

---

## Key Concepts

- *Variable*: a named container that stores a value.
- *Assignment*: giving a value to a variable using the equals sign, e.g., `x = 5`.
- *Data types*: common kinds of values Python can store, such as integers, floats, strings, booleans, and more complex types.
- *Type inference*: Python automatically knows the type of a value based on what you assign.
- *Reassignment*: you can change the value stored in a variable at any time.
- *Variable naming rules*: letters, digits, and underscores; cannot start with a digit; case-sensitive.

Analogy: Think of a variable like a labeled cup. The label is the variable name, the liquid inside is the value, and you can pour in a new liquid (reassign) without changing the label.

Why it matters: Variables let you store user input, keep track of counts, build dynamic text, and perform computations. Without variables, a program would have to recompute the same values repeatedly or rely on hard-coded literals.

---

## Examples

- Basic integer variable
```python
age = 16
print(age)  # 16
```

- Floating-point number
```python
price = 19.99
print(price)  # 19.99
```

- String variable
```python
name = "Alex"
print("Hello,", name)  # Hello, Alex
```

- Boolean variable
```python
is_student = True
print(is_student)  # True
```

- Updating (reassigning) a variable
```python
score = 0
score = score + 1  # or score += 1
print(score)  # 1
```

- Variable naming rules (valid vs. invalid)
```python
# Valid
first_name = "Jamie"
_age = 25
x1 = 10

# Invalid (will cause a syntax error)
# 1st_place = 2
# first-name = "Sam"
```

- Case sensitivity
```python
value = 5
Value = 10
print(value)  # 5
print(Value)  # 10
```

---

## Practice Problems (Guided Practice)

### Problem 1: Create and print basic variables
**Difficulty:** ⭐

**Prerequisites:** Basic understanding of Python syntax

**Problem:**
Create three variables: `city` with your city name, `year` with the current year, and `temperature` with a float value. Print a sentence using all three.

**Starter Code/Guidance:**
```python
city = ...
year = ...
temperature = ...
print(...)
```

**Solution:**
```python
city = "Seattle"
year = 2025
temperature = 18.5

print(f"Welcome to {city} in {year}! The temperature is {temperature}°C.")
```

**Key Takeaway:**
You can store different data types in variables and combine them in output.

---

### Problem 2: Simple arithmetic with variables
**Difficulty:** ⭐⭐

**Prerequisites:** Basic variables and print

**Problem:**
Create two variables `a` and `b` with values 7 and 3. Compute and print their sum, difference, product, and quotient.

**Solution:**
```python
a = 7
b = 3

sum_ = a + b
diff = a - b
prod = a * b
quot = a / b

print("sum:", sum_)
print("diff:", diff)
print("prod:", prod)
print("quot:", quot)
```

**Key Takeaway:**
Variables can participate in expressions to produce new values.

---

### Problem 3: String concatenation with variables
**Difficulty:** ⭐⭐⭐

**Prerequisites:** Strings and variables

**Problem:**
Create `first` and `last` variables and print a full name by concatenation. Use an explicit space between them.

**Solution:**
```python
first = "Jordan"
last = "Lee"

full_name = first + " " + last
print(full_name)
```

**Key Takeaway:**
Use `+` to join strings, but include any needed separators.

---

### Problem 4: Reassignment and incremental change
**Difficulty:** ⭐⭐

**Prerequisites:** Variable creation, basic arithmetic

**Problem:**
Start with `count = 5`. Increase by 2, then multiply by 3. Print the final value.

**Solution:**
```python
count = 5
count += 2      # 7
count *= 3      # 21
print(count)    # 21
```

**Key Takeaway:**
Compound assignment operators simplify updates.

---

### Problem 5: Booleans and condition-ready variables
**Difficulty:** ⭐⭐⭐

**Prerequisites:** Basic variables

**Problem:**
Create `logged_in` as True if a user is authenticated and `credit_ok` as False if their balance is insufficient. Print both.

**Solution:**
```python
logged_in = True
credit_ok = False

print("Logged in:", logged_in)
print("Credit OK:", credit_ok)
```

**Key Takeaway:**
Variables can store boolean states used in decisions.

---

## Independent Practice

### Practice Problem 1: Temperature converter (Celsius to Fahrenheit)
**Difficulty:** ⭐⭐

**Problem:**
Given a Celsius temperature `c = 25`, compute Fahrenheit using the formula `f = c * 9/5 + 32`. Print the result.

**Hints:**
- Use float division for precision.
- Print with a descriptive message.

**Solution:**
```python
c = 25
f = c * 9/5 + 32
print(f"{c}°C is {f}°F")
```

---

### Practice Problem 2: Variable swap without a temporary variable
**Difficulty:** ⭐⭐⭐

**Problem:**
Swap values of `a = 4` and `b = 9` without a temporary variable. Print both after swap.

**Solution:**
```python
a = 4
b = 9

a, b = b, a

print("a =", a)
print("b =", b)
```

---

### Practice Problem 3: Safe string formatting
**Difficulty:** ⭐⭐

**Problem:**
Create `name = "Sam"`, `age = 30`. Print: "Sam is 30 years old." using an f-string.

**Solution:**
```python
name = "Sam"
age = 30

print(f"{name} is {age} years old.")
```

---

### Practice Problem 4: Mixed types in a message
**Difficulty:** ⭐⭐⭐

**Problem:**
Given `item = "apples"`, `quantity = 12`, `price = 0.5`, print: "You have 12 apples at $0.50 each." Ensure price formats to 2 decimals.

**Solution:**
```python
item = "apples"
quantity = 12
price = 0.5

print(f"You have {quantity} {item} at ${price:.2f} each.")
```

---

### Practice Problem 5: Basic if-ready variables (conceptual)
**Difficulty:** ⭐⭐⭐

**Problem:**
Create `inventory` with value 5. Create `order` with value 7. Print whether you need to restock (inventory < order).

**Solution:**
```python
inventory = 5
order = 7

needs_restock = inventory < order
print("Restock needed:", needs_restock)
```

---

### Practice Problem 6: Case-sensitive variables
**Difficulty:** ⭐

**Problem:**
What will be printed?
```python
value = 1
Value = 2
print(value, Value)
```

**Solution:**
```
1 2
```

---

### Practice Problem 7: Large numbers and underscores for readability
**Difficulty:** ⭐

**Problem:**
Create `population` with value 7_800_000_000 and print it.

**Solution:**
```python
population = 7_800_000_000
print(population)
```

---

### Practice Problem 8: Combining user input (simulated)
**Difficulty:** ⭐⭐⭐

**Problem:**
Assume you read a user’s name and age as strings: `name = "Alex"`, `age_str = "21"`. Create an integer `age` from `age_str` and print a greeting including the age.

**Solution:**
```python
name = "Alex"
age_str = "21"

age = int(age_str)
print(f"Hello, {name}! You are {age} years old.")
```

---

## Mastery Challenge

### Challenge 1: Real-world budget tracker (multiple variables, basic logic)
**Difficulty:** ⭐⭐⭐⭐⭐
**Skills Tested:** Variables, types, arithmetic, f-strings, basic logic

**Time Estimate:** 45-75 minutes

**Scenario:**
You’re building a tiny budget tracker for a weekend trip. You have a list of expenses with their amounts in dollars. You’ll store the total budget, add expenses, and determine if you’re under budget or over.

**Requirements:**
- Set `budget` to 250.0
- Create a list of expenses (e.g., [40.0, 15.50, 60.75, 120.0])
- Compute `total_spent` by summing expenses
- Compute `remaining` = `budget` - `total_spent`
- Print a clear report showing budget, total spent, and remaining with two decimals
- If you’re over budget, print a friendly warning

**Solution Approach:**
- Use a list to store expenses
- Use `sum(...)` to total
- Use f-strings for formatted output
- Include a conditional for over-budget

**Mentorship Notes:**
- Start simple: track a few categories, then expand.
- Consider edge cases: empty expenses, negative values (invalid), or float precision.

**Solution:**
```python
# Budget setup
budget = 250.0

# Expenses (in dollars)
expenses = [40.0, 15.50, 60.75, 120.0]

# Calculations
total_spent = sum(expenses)
remaining = budget - total_spent

# Report
print("Trip Budget Report")
print(f"Budget: ${budget:.2f}")
print(f"Total spent: ${total_spent:.2f}")
print(f"Remaining: ${remaining:.2f}")

# Over-budget check
if remaining < 0:
    print("⚠️ Warning: You are over budget!")
else:
    print("✅ You are within budget. Nice planning!")
```

---

### Challenge 2: Inventory-worth calculation (multiple item types)
**Difficulty:** ⭐⭐⭐⭐

**Skills Tested:** Variables, lists, loops, arithmetic

**Scenario:**
You manage a small shop. You have items with names, quantities, and unit prices. Compute total inventory value and print a summary.

**Requirements:**
- Define `items` as a list of dictionaries with keys: `name`, `qty`, `price`
- Compute total value = sum(qty * price) for all items
- Print per-item value and the grand total with two decimals

**Solution Approach:**
```python
items = [
    {"name": "Notebook", "qty": 30, "price": 2.50},
    {"name": "Pen", "qty": 100, "price": 0.75},
    {"name": "Sticker Pack", "qty": 20, "price": 1.25},
]

# Individual values
total_value = 0.0
print("Inventory Value by Item:")
for item in items:
    item_value = item["qty"] * item["price"]
    total_value += item_value
    print(f"- {item['name']}: {item['qty']} units * ${item['price']:.2f} = ${item_value:.2f}")

print(f"Total inventory value: ${total_value:.2f}")
```

---

### Challenge 3: Data-type robustness (input validation concept)
**Difficulty:** ⭐⭐⭐⭐⭐

**Skills Tested:** Variables, type conversion, basic validation

**Scenario:**
You’re building a simple form parser. You receive `raw_age = "27"` or `"twenty-seven"`. Normalize to an integer if possible, otherwise report invalid input.

**Requirements:**
- Try to convert to int; if it fails, set `age` to None
- Print a friendly message depending on whether a valid age exists

**Solution Approach:**
```python
raw_age = "27"  # try changing this to "twenty-seven" to test

try:
    age = int(raw_age)
except ValueError:
    age = None

if age is not None:
    print(f"Age parsed successfully: {age}")
else:
    print("Invalid age input. Please enter a numeric value.")
```

---

## Summary

- Variables are named storage for values and are essential for building dynamic programs.
- You can store integers, floats, strings, booleans, and more, and reassign values as needed.
- Practice reinforces how to combine variables in expressions, format outputs, and keep code readable.

---

## Solutions (Key Explanations)

- Stage 2 (Knowledge Check): Answers included in each problem above.
- Stage 3 (Guided Practice): Fully worked solutions with explanations and common pitfalls noted in each problem.
- Stage 4 (Independent Practice): Solutions provided for all practice problems.
- Stage 5 (Mastery Challenge): Real-world scenarios with clear solution approaches and mentorship notes.

If you’d like, I can tailor the difficulty, swap in different practice problems, or expand any section.