# Python Variables: A Gentle Introduction to Storing Data

## Overview
Are you curious how Python stores information like numbers, words, or true/false values while a program runs? Welcome to the world of variables. Think of a variable as a labeled container in the memory of your computer. You put a value into it, and you can use that label to retrieve or change the value later.

This micro-topic will introduce you to:
- What a variable is and how to name it
- How assignment works and Python’s dynamic typing
- Basic data types commonly stored in variables
- Simple operations you can perform with variables
- Common mistakes and how to avoid them

By the end, you’ll be ready to create and manipulate variables confidently in small Python programs.

---

## Key Concepts

### What is a variable?
- A *variable* is a name that refers to a value stored in memory.
- You create a variable by giving it a name and assigning it a value.

### Naming rules (the basics)
- Variable names can include letters, digits, and underscores, but must start with a letter or underscore.
- Python is case-sensitive: `score`, `Score`, and `SCORE` are different variables.
- Avoid using Python keywords (like `for`, `while`, `class`, etc.) as names.

### Dynamic typing
- Python is dynamically typed: you don’t declare a type before using a variable.
- The type is inferred from the value you assign.
- You can reassign a variable to a value of a different type (e.g., from an int to a string).

### Basic data types you’ll store in variables
- Numbers: integers (`int`), floating-point numbers (`float`)
- Text: strings (`str`)
- Booleans: `True` and `False` (type: `bool`)
- More complex types exist (lists, dictionaries, etc.), but we’ll focus on basics here.

### Assignment and simple operations
- The `=` symbol assigns a value to a variable.
- You can perform arithmetic and string operations using operators like `+`, `-`, `*`, `/`, and more.

### Why variables matter
- They store data that your program manipulates.
- They enable you to write flexible, reusable code instead of hard-coding values.

---

## Knowledge Check

Q1: Which of the following is a valid Python variable name?
a) 2nd_place
b) second-place
c) _second_place
d) class

**Answer:** c) _second_place — starts with an underscore, uses only letters, digits, and underscores; not a Python keyword.

Q2: What does the following code do?
```python
x = 10
x = x + 5
```
a) Creates two variables, `x` and `y`
b) Sets `x` to 15
c) Throws a syntax error
d) Sets `x` to 10 and then to 5

**Answer:** b) Sets `x` to 15 — `x` is updated by adding 5 to its current value.

Q3: Which statement about Python variable types is true?
a) You must declare the type before assigning a value
b) The type of a variable can change after assignment
c) A variable can only store numbers
d) Variables are immutable

**Answer:** b) The type of a variable can change after assignment — Python uses dynamic typing.

Q4: What is the type of `s = "Hello"`?
a) int
b) float
c) str
d) bool

**Answer:** c) str

Q5: Which of the following will cause a runtime error?
a) `a = 5; b = "5"; c = a + b`
b) `a = 5; a = "five"; b = a + " more"`
c) `a = 5; b = a * 2`
d) `name = "Alex"; greeting = "Hello " + name`

**Answer:** a) `a + b` when `b` is a string and `a` is an int causes a TypeError.

Q6: What is the result of `type(3.14)` in Python?
a) int
b) float
c) complex
d) str

**Answer:** b) float

Q7: Which operator is used to assign a new value to a variable?
a) ==
b) :=
c) =
d) ->

**Answer:** c) =

Q8: Which of the following is a valid string in Python?
a) 'It\'s sunny'
b) "She said "hi""
c) `No quotes`
d) None

**Answer:** a) 'It\'s sunny' — properly escaped; strings must be enclosed in matching quotes.

---

## Guided Practice

Problem 1: Create and update a simple counter
**Difficulty:** ⭐⭐
**Prerequisites:** Basic understanding of variables and arithmetic

**Problem Statement:**
Create a variable named `counter` starting at 0. Then increment it by 1 three times. Print the final value.

**Starter Code/Guidance:**
```python
# Initialize
counter = 0
# Increment three times
# TODO
# Print
print(counter)
```

**Solution:**
```python
# Initialize
counter = 0
# Increment three times
counter = counter + 1  # 1
counter = counter + 1  # 2
counter = counter + 1  # 3
# Print
print(counter)  # 3
```

**Key Takeaway:**
You can update a variable by reassigning it using its current value.

Problem 2: Friendly greeting with a name
**Difficulty:** ⭐⭐
**Prerequisites:** Strings and variables

**Problem Statement:**
Ask for a user’s name (as a string) and create a greeting stored in a variable named `greeting`. Then print the greeting.

**Starter Code/Guidance:**
```python
name = "Alex"  # replace with input() for real interaction
greeting = "Hello, "
# Complete
print(greeting)
```

**Solution:**
```python
name = "Alex"  # or: name = input("What is your name? ")
greeting = "Hello, " + name + "!"
print(greeting)  # Hello, Alex!
```

**Key Takeaway:**
Strings can be concatenated with `+` to form longer messages.

Problem 3: Mixed types and dynamic typing
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Variables, basic types

**Problem Statement:**
Create a variable `value` assigned to an integer, then reassign it to a string. Print its type after each assignment.

**Starter Code/Guidance:**
```python
value = 42
print(type(value))
value = "forty-two"
print(type(value))
```

**Solution:**
```python
value = 42
print(type(value))  # <class 'int'>
value = "forty-two"
print(type(value))  # <class 'str'>
```

**Key Takeaway:**
Python allows changing the type of a variable by reassigning a new value.

Problem 4: Basic arithmetic operations
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Variables and numbers

**Problem Statement:**
Compute the area of a rectangle with width 7 and height 3 and store the result in `area`. Print the result.

**Starter Code/Guidance:**
```python
width = 7
height = 3
area = 0  # replace
print(area)
```

**Solution:**
```python
width = 7
height = 3
area = width * height
print(area)  # 21
```

**Key Takeaway:**
Use arithmetic operators to combine values stored in variables.

Problem 5: Type-aware printing
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Variables, strings

**Problem Statement:**
Store a number and a string in variables `num` and `text`. Print a sentence that includes both, without converting types manually.

**Starter Code/Guidance:**
```python
num = 5
text = "apples"
print("I have " + str(num) + " " + text)
```

**Solution:**
```python
num = 5
text = "apples"
print(f"I have {num} {text}")  # I have 5 apples
```

**Key Takeaway:**
F-strings provide a clean way to combine different types in a printable sentence.

---

## Independent Practice

Practice Problem 1: Temperature conversion
**Difficulty:** ⭐⭐
**Problem:**
Store a Celsius temperature in `c` (e.g., 25). Compute Fahrenheit as `f = c * 9/5 + 32`. Print both.

**Hints (optional):**
- Use the arithmetic operators
- Keep values in variables

**Solution:**
```python
c = 25
f = c * 9/5 + 32
print("Celsius:", c)
print("Fahrenheit:", f)
```

Practice Problem 2: Swapping values
**Difficulty:** ⭐⭐
**Problem:**
Given `a = 10` and `b = 20`, swap their values without a temporary variable. Print both after the swap.

**Solution:**
```python
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10
```

Practice Problem 3: Quote storage
**Difficulty:** ⭐⭐⭐
**Problem:**
Store the sentence: She said, "Python is fun!" in a variable `quote`. Print it.

**Solution:**
```python
quote = 'She said, "Python is fun!"'
print(quote)
```

Practice Problem 4: Type checks
**Difficulty:** ⭐⭐⭐
**Problem:**
Create a variable `flag` with value `True`. Print its type. Then assign `flag = "yes"` and print its type again.

**Solution:**
```python
flag = True
print(type(flag))  # <class 'bool'>
flag = "yes"
print(type(flag))  # <class 'str'>
```

Practice Problem 5: Simple accumulator
**Difficulty:** ⭐⭐⭐⭐
**Problem:**
Create a variable `sum` initialized to 0. Add numbers 1 through 5 to it in a loop. Print the final sum.

**Solution:**
```python
sum = 0
for i in range(1, 6):
    sum += i
print(sum)  # 15
```

Practice Problem 6: String repetition
**Difficulty:** ⭐⭐⭐
**Problem:**
Create a variable `name` and a variable `times` (an integer). Create a new string that repeats the name 3 times, separated by spaces, and print it.

**Solution:**
```python
name = "Ada"
times = 3
result = (name + " ") * times
print(result.strip())  # Ada Ada Ada
```

Practice Problem 7: Safe division
**Difficulty:** ⭐⭐⭐⭐
**Problem:**
Store two numbers `x` and `y` (make `y` nonzero). Compute `x / y` using floating-point division and print the result.

**Solution:**
```python
x = 7
y = 2
result = x / y
print(result)  # 3.5
```

Practice Problem 8: Exploring type change
**Difficulty:** ⭐⭐⭐⭐⭐
**Problem:**
Start with `value = 100`. Reassign to a float, then to a string, then to a boolean. After each change, print both the value and its type.

**Solution:**
```python
value = 100
print(value, type(value))  # 100 <class 'int'>
value = 100.0
print(value, type(value))  # 100.0 <class 'float'>
value = "one hundred"
print(value, type(value))  # one hundred <class 'str'>
value = False
print(value, type(value))  # False <class 'bool'>
```

---

## Mastery Challenge

Challenge 1: Student record snippet
**Difficulty:** ⭐⭐⭐⭐⭐
**Skills Tested:** Variables, strings, arithmetic, formatting

**Scenario:**
You are building a tiny student record snippet. Create variables for:
- `student_name` (string)
- `grades` (list of numbers, e.g., [85, 92, 78])
- `average` (float), computed as the average of `grades`
- `passed` (bool), True if average >= 60

**You should produce:**
- The computed `average` with two decimal places
- A printout like: "Student: Ada; Average: 86.33; Status: Passed"

**Solution Approach:**
```python
# Variables
student_name = "Ada"
grades = [85, 92, 78]

# Compute average
average = sum(grades) / len(grades)

# Pass/Fail
passed = average >= 60

# Output with formatting
status = "Passed" if passed else "Failed"
print(f"Student: {student_name}; Average: {average:.2f}; Status: {status}")
```

Challenge 2: Dynamic scoreboard (edge case handling)
**Difficulty:** ⭐⭐⭐⭐⭐
**Skills Tested:** Variables, input handling (conceptually), error checking

**Scenario:**
Simulate a small scoreboard update where you receive a new score. Validate the score is a non-negative number before updating a running total and a count of games. Compute and print the new average score.

**Solution Approach:**
```python
# Initial scoreboard
total_score = 0
games = 0

def add_score(score):
    global total_score, games
    # Basic validation
    if not isinstance(score, (int, float)) or score < 0:
        raise ValueError("Score must be a non-negative number")
    total_score += score
    games += 1
    average = total_score / games
    return average

# Example additions
avg1 = add_score(90)
avg2 = add_score(75)
print(f"Average after 2 games: {avg2:.2f}")  # 82.50
```

Challenge 3: Optional feature toggle
**Difficulty:** ⭐⭐⭐⭐⭐
**Skills Tested:** Booleans, conditionals, variables

**Scenario:**
Implement a simple feature toggle. If `feature_on` is True, print a special message using a variable `intro`. If False, print a default message. Show two runs: one with the feature on, one with it off.

**Solution Approach:**
```python
feature_on = True
intro = "Welcome to the Python Variables course!"

if feature_on:
    print(intro + " Enjoy the enhanced experience!")
else:
    print("Welcome to the Python Variables course!")

# Toggle
feature_on = False
if feature_on:
    print(intro + " Enjoy the enhanced experience!")
else:
    print("Welcome to the Python Variables course!")
```

Mentorship Notes:
- Start with clear, labeled containers (variables) for data you’ll reuse.
- Prefer meaningful, readable names to reduce cognitive load.
- Practice, then practice some more with small, real-world examples—like scores, names, and settings—to solidify the habit of thinking in terms of variables.
- When debugging, print the type and value of a variable to understand what the program is actually holding.

---

## Summary
- Variables are labeled containers for data in Python, created with simple assignment.
- Python uses dynamic typing; a variable can hold values of different types over its lifetime.
- Name your variables clearly, follow naming rules, and avoid Python keywords.
- Basic data types include integers, floats, strings, and booleans.
- Start simple with arithmetic and string operations, then expand to lists, dictionaries, and more complex structures as you grow.

You're now equipped to declare, update, and use variables in small Python programs. Practice with a few quick scripts to reinforce these concepts, and you’ll build a solid foundation for more advanced topics.