# Python Variables

## Overview

Imagine you’re building a tiny pantry in your computer. You want to store ingredients like flour, sugar, and salt so you can use them later. In Python, those “ingredients” are values, and the containers you store them in are called variables. Variables let you name, store, and manipulate data as your program runs. They’re fundamental: every line of Python code interacts with variables in some way—assigning values, changing them, or using them to perform calculations.

In this chapter, you’ll learn:
- What a variable is and how Python treats data values
- How to create and use variables effectively
- The rules for naming variables
- How to update and delete variables
- How different data types interact with variables
- Common pitfalls and best practices

By the end, you’ll be able to declare variables confidently, choose meaningful names, and write basic programs that rely on holding data in memory.

---

## Key Concepts

### What is a variable?
- A variable is a named location in memory that stores a value.
- The value can be of various types: numbers, text, booleans, lists, dictionaries, and more.
- Variables have a name (identifier) and a value. The value can be changed, but the name remains the same.

### Assignment
- Assignment binds a name to a value.
- The simplest form is: `name = value`
- After assignment, you can use the name to refer to that value.

### Dynamic typing
- Python is dynamically typed: you don’t declare a type when you create a variable.
- The interpreter determines the type from the value you assign.
- You can rebind the same variable name to a different type later.

### Data types (quick refresher)
- Numbers: integers and floats (e.g., `42`, `3.14`)
- Strings: text data (e.g., `"Hello"`, `'World'`)
- Booleans: `True` or `False`
- Lists: ordered collections (e.g., `[1, 2, 3]`)
- Tuples: immutable ordered collections (e.g., `(1, 2, 3)`)
- Dictionaries: key-value mappings (e.g., `{"name": "Alex"}`)
- None: absence of a value (special constant `None`)

### Variable naming rules
- Must start with a letter (a–z, A–Z) or underscore `_`
- Remaining characters can be letters, digits, or underscores
- Case-sensitive: `age` and `Age` are different
- Cannot be Python keywords (e.g., `for`, `while`, `class`, `import`)

### Updating and deleting
- You can reassign a variable to a new value: `x = 10` → `x = 20`
- To delete a variable: `del x`
- After deletion, using the variable name will raise a `NameError`

### Scope and lifetime
- Variables have scope: where they are accessible (global vs. local)
- In simple scripts, variables are global to the module. Inside functions, variables can be local unless declared `global`.

### Printing and formatting
- Use `print()` to display variable values.
- You can format strings with f-strings: `name = "Alex"; print(f"Hello, {name}!")`

---

## Examples

### Basic assignment
```python
# Simple variable assignment
x = 5
y = 2.7
name = "Alex"

print(x)      # 5
print(y)      # 2.7
print(name)   # Alex
```

### Reassigning a variable (dynamic typing)
```python
# Reassigning to a different type
value = 10        # int
print(type(value))  # <class 'int'>

value = 3.14      # float
print(type(value))  # <class 'float'>

value = "ten"     # str
print(type(value))  # <class 'str'>
```

### Multiple assignments
```python
a = b = c = 0
print(a, b, c)  # 0 0 0

# Or assign different values in one line
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3
```

### Names and readability
```python
# Good naming
user_count = 42
average_score = 3.75
```

### Strings and concatenation
```python
first_name = "Taylor"
last_name = "Lee"
full_name = first_name + " " + last_name
print(full_name)  # Taylor Lee
```

### Lists and mutability
```python
numbers = [1, 2, 3]
print(numbers)  # [1, 2, 3]

numbers[0] = 10
print(numbers)  # [10, 2, 3]
```

### Dictionaries (mapping)
```python
person = {"name": "Alex", "age": 30}
print(person["name"])  # Alex
person["city"] = "New York"
print(person)  # {'name': 'Alex', 'age': 30, 'city': 'New York'}
```

### None and empty values
```python
result = None
print(result is None)  # True

empty_list = []
print(len(empty_list))  # 0
```

### Printing with formatting (f-strings)
```python
name = "Jordan"
score = 95
print(f"{name} scored {score} on the test.")
# Jordan scored 95 on the test.
```

---

## Practice Problems

### Problem 1: Simple variable creation
**Difficulty:** ⭐
**Prerequisites:** None

**Problem Statement:**
Create three variables: an integer `a` with value 7, a float `b` with value 2.5, and a string `c` with value "Python".

**Starter Code/Guidance:**
```
# Your code here
```

**Solution:**
```
a = 7
b = 2.5
c = "Python"

print(a, b, c)
```

**Key Takeaway:**
You can store different types of data in separate variables and print them together.

---

### Problem 2: Variable reassignment and type change
**Difficulty:** ⭐⭐
**Prerequisites:** Problem 1 concepts

**Problem Statement:**
Start with `msg = "Hi"`. Reassign it to the number 100, then to the boolean `True`. Print the value and its type after each change.

**Starter Code/Guidance:**
```
msg = "Hi"
# Reassign and print after each step
```

**Solution:**
```
msg = "Hi"
print(msg, type(msg))  # Hi <class 'str'>

msg = 100
print(msg, type(msg))  # 100 <class 'int'>

msg = True
print(msg, type(msg))  # True <class 'bool'>
```

**Key Takeaway:**
Python variables are dynamically typed; their type can change with reassignment.

---

### Problem 3: List and indexing
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Basic variable types; lists

**Problem Statement:**
Create a list `letters` containing the vowels `['a', 'e', 'i', 'o', 'u']`. Print the first and last elements. Change the second element to `'é'` and print the list.

**Starter Code/Guidance:**
```
letters = ['a', 'e', 'i', 'o', 'u']
# print first and last, then modify
```

**Solution:**
```
letters = ['a', 'e', 'i', 'o', 'u']
print(letters[0])  # a
print(letters[-1]) # u

letters[1] = 'é'
print(letters)  # ['a', 'é', 'i', 'o', 'u']
```

**Key Takeaway:**
Lists are mutable; you can access and modify elements by index.

---

### Problem 4: Dictionary basics
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Problem 3 concepts

**Problem Statement:**
Create a dictionary `student` with keys `name` (string), `grade` (float), and `passed` (boolean). Update `passed` to reflect whether `grade` is at least 60. Print the dictionary before and after.

**Starter Code/Guidance:**
```
student = {"name": "Alex", "grade": 58.0, "passed": False}
# update and print
```

**Solution:**
```
student = {"name": "Alex", "grade": 58.0, "passed": False}
print(student)

student["grade"] = 72.5
student["passed"] = student["grade"] >= 60
print(student)
```

**Key Takeaway:**
Dictionaries store key-value pairs and can be updated dynamically.

---

### Problem 5: Variable scope basics
**Difficulty:** ⭐⭐⭐⭐
**Prerequisites:** Basic functions (if you know them)

**Problem Statement:**
Write a function `add_five(x)` that creates a local variable `result` equal to `x + 5` and returns it. Call the function with `10` and print the returned value. Also, try to print `result` outside the function and explain what happens.

**Starter Code/Guidance:**
```
def add_five(x):
    # local variable
    result = x + 5
    return result

print(add_five(10))
print(result)  # what happens here?
```

**Solution:**
```
def add_five(x):
    # local variable
    result = x + 5
    return result

print(add_five(10))  # 15

# The following line will raise a NameError because 'result' is local to the function
try:
    print(result)
except NameError as e:
    print("NameError:", e)
```

**Key Takeaway:**
Variables defined inside a function are local; they aren’t accessible outside, illustrating scope.

---

### Problem 6: String formatting with variables
**Difficulty:** ⭐⭐⭐⭐
**Prerequisites:** Problem 5 concepts

**Problem Statement:**
Create variables `city = "Paris"`, `year = 2024`, and `temperature = 18.5`. Print a sentence: "The temperature in Paris in 2024 was 18.5°C." using an f-string.

**Starter Code/Guidance:**
```
city = "Paris"
year = 2024
temperature = 18.5
# print formatted sentence
```

**Solution:**
```
city = "Paris"
year = 2024
temperature = 18.5

print(f"The temperature in {city} in {year} was {temperature}°C.")
```

**Key Takeaway:**
F-strings provide readable, convenient string interpolation using variables.

---

## Independent Practice

### Practice Problem 1: Variable arithmetic
**Difficulty:** ⭐⭐
**Problem:**
Create two variables `x = 9` and `y = 4`. Compute and print their sum, difference, product, and quotient. Also print integer division and remainder.

**Hints:**
- Use `+`, `-`, `*`, `/`, `//`, `%`.

**Solution:**
```
x = 9
y = 4

print("sum:", x + y)        # 13
print("difference:", x - y) # 5
print("product:", x * y)    # 36
print("quotient:", x / y)   # 2.25
print("integer division:", x // y)  # 2
print("remainder:", x % y)          # 1
```

### Practice Problem 2: Mutable vs immutable
**Difficulty:** ⭐⭐⭐
**Problem:**
Explain in your own words why a list is mutable and a string is immutable. Provide a short code example that shows mutability of a list and attempted mutation of a string that fails.

**Hints:**
- Try changing an element of a list vs. replacing a character in a string.

**Solution:**
```
# Mutable: list
fruits = ["apple", "banana"]
fruits[0] = "cherry"
print(fruits)  # ['cherry', 'banana']

# Immutable: string
text = "hello"
try:
    text[0] = "H"
except TypeError as e:
    print("Error:", e)  # 'str' object does not support item assignment
```

### Practice Problem 3: Variable naming and style
**Difficulty:** ⭐⭐
**Problem:**
Rename the following poorly named variables to meaningful ones, preserving their values:
```
a = 3.14159
b = "pi"
c = True
```

**Solution:**
```
pi_value = 3.14159
pi_label = "pi"
is_pi_approximated = True
```

### Practice Problem 4: Deleting variables
**Difficulty:** ⭐⭐⭐
**Problem:**
Create a variable `temp = 25`, print it, delete it, and show that accessing `temp` afterwards raises an error.

**Solution:**
```
temp = 25
print(temp)  # 25
del temp
try:
    print(temp)
except NameError as e:
    print("NameError:", e)
```

### Practice Problem 5: Combining types
**Difficulty:** ⭐⭐⭐⭐⭐
**Problem:**
Create a small program that stores a student record as a dictionary with keys `id` (int), `name` (str), `grades` (list of floats). Add a new grade to the `grades` list, update `average` key to the average of grades, and print the final dictionary.

**Solution:**
```
student = {
    "id": 12345,
    "name": "Sam",
    "grades": [88.0, 92.5, 79.0]
}

# Add a new grade
student["grades"].append(85.5)

# Compute average
grades = student["grades"]
average = sum(grades) / len(grades)
student["average"] = average

print(student)
```

---

## Solutions (Expanded Explanations)

### Why variables matter
Variables are the essential building blocks for storing inputs, intermediate results, and final outputs in a program. They enable you to:
- Keep track of user input and computed results
- Pass data between functions
- Build dynamic programs that react to changing values

### Choosing good names
- Use descriptive, readable names that reflect the data’s meaning (e.g., `user_age`, `item_price`, `is_valid`).
- Prefer nouns for data storage and verbs for actions or predicates (e.g., `count` vs. `increment`).
- Use underscores for readability (snake_case) in Python.

### Common mistakes and how to avoid them
- Overusing global variables: Cluttered namespaces and harder-to-maintain code. Prefer local variables inside functions and clear interfaces.
- Rebinding to different types accidentally: If you expect a variable to hold a number but it becomes a string, calculations will fail. Use clear naming and tests.
- Name collisions with built-in names: Avoid names like `list`, `str`, or `dict` as your variables.

### Quick tips
- Always print intermediate results when debugging to verify your understanding of what a variable holds.
- Use comments near complex variable logic to explain why the value is assigned or updated.
- When working with user input, convert and validate early to avoid type errors later.

---

## Summary

- A variable is a named container that stores a value. You create it with an assignment, e.g., `x = 5`.
- Python is dynamically typed: a variable’s type can change through reassignment.
- Names must follow Python’s rules and be descriptive to improve readability.
- Variables have scope: inside functions, variables are local unless declared otherwise.
- You can store many data types in variables: numbers, strings, lists, dictionaries, booleans, and more.
- Practice with naming, updating, and combining different types to build flexible programs.

Keep experimenting with small snippets to reinforce these concepts. As you gain confidence, you’ll start writing larger programs that rely on well-managed variables to store and transform data.

