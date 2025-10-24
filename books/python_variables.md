# Python Variables

## Overview
Hook: Imagine labeling jars in a pantry so you can find sugar, salt, and flour quickly — variables let you label and store data in your programs the same way.

Learning objectives
- 🎯 Define what a variable is and how Python stores them.
- 🎯 Create, assign, and reassign variables using correct syntax.
- 🎯 Identify and use common data types: integers, floats, strings, booleans.
- 🎯 Recognize naming rules and common pitfalls (e.g., reserved words, mutable vs immutable).
- 🎯 Apply variables in small code examples and solve practice problems.

Brief theory
A *variable* is a name that refers to a value stored in the computer's memory. In Python, assignment uses the equals sign (`=`) to bind a name to an object. Python is dynamically typed: you don't declare types explicitly — the interpreter infers the type at runtime. Variable names point to objects; multiple names can refer to the same object and names can be rebound to new objects.

Analogy
Think of a variable as a sticky note on a jar: the jar holds the actual contents (the value) and the sticky note (the name) points to it. You can move the sticky note to another jar or replace the jar contents.

Why it matters
Variables are fundamental — every program stores, transforms, and outputs data via variables. Clear naming and correct use prevent bugs and make code readable and maintainable.

## Key Concepts

- *Assignment:* `name = value` creates or updates a binding.
- *Dynamic typing:* A variable can hold any type and change types later.
- *Immutable vs Mutable:* Immutable objects (e.g., ints, strings, tuples) cannot be changed; mutable objects (e.g., lists, dicts, sets) can be modified in place.
- *Naming rules:* Use letters, digits, and underscores; cannot start with a digit; avoid Python reserved keywords (e.g., `for`, `if`, `class`).
- *Best practices:* Use descriptive, lowercase names with underscores (snake_case). Prefer immutability for simpler reasoning.

Knowledge check (MCQs)

Q1: Which of the following is a valid variable name?
a) 2nd_value
b) second-value
c) second_value
d) second value

**Answer:** c) second_value — starts with a letter and uses underscore.

Q2: After `x = 5; x = "hello"`, what is the type of x?
a) int
b) str
c) float
d) It depends on interpreter settings

**Answer:** b) str — Python dynamically rebinds x to a string.

Q3: Which operation modifies a list in place?
a) `a = a + [1]`
b) `a.append(1)`
c) `a = a * 2`
d) `a = list(a)`

**Answer:** b) `a.append(1)` — append mutates the original list.

Q4: Which statement is true about immutable objects?
a) Their value cannot be referenced by multiple names.
b) They can be modified without creating a new object.
c) Operations that seem to modify them create new objects.
d) They are always faster to work with than mutable ones.

**Answer:** c) Operations that seem to modify them create new objects.

Q5: Which of these is a Python keyword and cannot be used as a variable?
a) `value`
b) `def`
c) `data`
d) `item`

**Answer:** b) `def` — it's a keyword used to define functions.

## Examples

Example: basic assignments
```python
# integers and strings
age = 30
name = "Aisha"

# float and boolean
temperature = 36.6
is_member = True

# reassigning and dynamic typing
age = "thirty"
```

Example: multiple assignment and swapping
```python
# multiple assignment
x, y, z = 1, 2, 3

# swap without temp
x, y = y, x
```

Example: mutable vs immutable demonstration
```python
# immutable integer
a = 10
b = a  # b points to same int object 10
a = a + 1  # a now points to a new int object 11, b still 10

# mutable list
lst1 = [1, 2]
lst2 = lst1  # both names refer to same list
lst1.append(3)  # mutates the single shared list
# now lst2 is [1, 2, 3] as well
```

## Practice Problems

### Problem 1: Greeting message
Difficulty: ⭐
Problem: Assign your name to a variable `user_name` and create `greeting` that says "Hello, <name>!".
Hints:
- Use string concatenation or f-strings.

### Problem 2: Temperature conversion
Difficulty: ⭐⭐
Problem: Given `celsius = 25`, compute `fahrenheit` using formula F = C * 9/5 + 32.

### Problem 3: Swap values
Difficulty: ⭐⭐
Problem: Swap values of variables `a` and `b` without using a temporary variable.

### Problem 4: Sum and average
Difficulty: ⭐⭐⭐
Problem: Given `numbers = [4, 8, 15, 16, 23, 42]`, compute the sum and average, store them in `total` and `avg`.

### Problem 5: Mutable aliasing bug
Difficulty: ⭐⭐⭐⭐
Problem: Explain and fix the bug: two variables `config1 = {"mode": "dev"}` and `config2 = config1`; then `config2["mode"] = "prod"`. The intent was for `config2` to be an independent copy.

### Problem 6: Name validation
Difficulty: ⭐⭐⭐⭐
Problem: Write a function `is_valid_var(name)` that returns True if `name` is a valid Python identifier and not a keyword; otherwise False. (Hint: use `str.isidentifier()` and `keyword` module.)

## Solutions

### Solution 1
```python
user_name = "Aisha"
greeting = f"Hello, {user_name}!"
print(greeting)  # Hello, Aisha!
```
Key takeaway: use descriptive variables and f-strings for clarity.

### Solution 2
```python
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)  # 77.0
```
Key takeaway: numeric operations follow normal precedence; use floats when needed.

### Solution 3
```python
a = 5
b = 10
# swap
a, b = b, a
# now a == 10, b == 5
```
Key takeaway: tuple unpacking is the Pythonic swap.

### Solution 4
```python
numbers = [4, 8, 15, 16, 23, 42]
total = sum(numbers)
avg = total / len(numbers)
print(total, avg)  # 108 18.0
```
Key takeaway: built-ins like sum() simplify common tasks.

### Solution 5
Explanation: `config2 = config1` makes both names refer to the same dict (aliasing). Mutating one affects the other. Fix by copying.
```python
import copy

config1 = {"mode": "dev"}
# shallow copy
config2 = config1.copy()
config2["mode"] = "prod"
# config1 remains {"mode": "dev"}

# for nested structures use deepcopy
config3 = copy.deepcopy(config1)
```
Key takeaway: use copies to avoid unintended shared mutations.

### Solution 6
```python
import keyword

def is_valid_var(name):
    # must be a string identifier and not a Python keyword
    return isinstance(name, str) and name.isidentifier() and not keyword.iskeyword(name)

# examples
print(is_valid_var("var1"))   # True
print(is_valid_var("1var"))   # False
print(is_valid_var("def"))    # False
```
Key takeaway: use built-in helpers for robust validation.

## Common Pitfalls
- Using Python keywords as variable names (e.g., `class = 3`) — SyntaxError.
- Assuming assignment copies mutable objects — leads to aliasing bugs.
- Reusing ambiguous names like `l`, `O`, or `I` that look similar; use clear names.
- Relying on implicit type conversions; explicit conversion often clearer (e.g., `int("3")`).
- Modifying immutable objects expecting in-place change (strings are immutable — methods return new strings).

## Summary
Variables label and store values; Python uses dynamic typing and simple assignment. Choose clear names, understand immutability vs mutability, and watch for aliasing when copying mutable objects. Practice swapping, arithmetic, and type-aware operations to build confidence.