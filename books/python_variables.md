# Python Variables

## Overview
Hook: Imagine you need to store a user's score in a game and update it as they play — how does Python remember that number? Variables are the labeled boxes Python uses to store and manipulate data.

Learning Objectives
- 🎯 Define what a variable is and identify common data types in Python.
- 🎯 Create, update, and delete variables using correct syntax.
- 🎯 Apply variable naming rules and best practices for readable code.
- 🎯 Use variables in expressions and simple programs.

Brief Theory
A *variable* is a name that refers to a value stored in memory. In Python, assignment uses the equals sign `=` to bind a name to an object (value). Python is dynamically typed: the type of the object is determined at runtime, and the same variable can refer to different types over time.

Analogy
Think of a variable as a labelled jar: the label is the variable name and the contents are the value. You can replace the contents without changing the jar.

Why It Matters
Variables let you store inputs, compute results, manage program state, and make code readable and maintainable. Practically every program uses variables.

## Key Concepts
- Variable assignment: `name = value`
- Data types: integers (`int`), floating-point numbers (`float`), strings (`str`), booleans (`bool`), lists (`list`), dictionaries (`dict`), and more.
- Dynamic typing: variable type is the type of its current value.
- Naming rules: start with a letter or underscore, use letters, digits, and underscores; case-sensitive; avoid reserved keywords.
- Mutable vs immutable: some objects (like lists, dicts) can be changed in place; others (ints, strings, tuples) cannot.

Short examples (concept illustration)

```python
# integer assignment
score = 0

# string assignment
player_name = "Asha"

# float assignment
accuracy = 99.5

# boolean assignment
is_active = True

# list (mutable)
levels = [1, 2, 3]

# reassigning to a different type (allowed)
score = "zero"  # dynamic typing: now score holds a string
```

## Examples (Guided Practice)

## Problem 1: Simple assignment and use
**Difficulty:** ⭐  
**Prerequisites:** None

Problem Statement:
Create two variables `a` and `b`, assign values 3 and 4, compute their sum and print: "Sum is 7".

Starter Code/Guidance:

```python
a = 3
b = 4
# compute sum and print result
```

Solution:

```python
a = 3
b = 4
total = a + b  # add numbers; result stored in 'total'
print("Sum is", total)  # prints: Sum is 7
```

Key Takeaway:
Use `=` to assign and `+` to add; `print` can display variables.

## Problem 2: Reassigning and types
**Difficulty:** ⭐⭐  
**Prerequisites:** Problem 1

Problem Statement:
Assign `x = 10`, then change `x` to `"ten"`. Print the type of `x` after each assignment.

Starter Code/Guidance:

```python
x = 10
# print type
x = "ten"
# print type again
```

Solution:

```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"       # reassign; dynamic typing changes the value's type
print(type(x))  # <class 'str'>
```

Key Takeaway:
Variables can be rebound to values of different types.

## Problem 3: Multiple assignment and swapping
**Difficulty:** ⭐⭐  
**Prerequisites:** Problem 1

Problem Statement:
Swap two variables `a` and `b` without using a temporary variable.

Solution:

```python
a = 5
b = 8
a, b = b, a  # tuple packing/unpacking swaps values
print(a, b)  # prints: 8 5
```

Why it works: Python evaluates the right side as a tuple `(b, a)` then unpacks into `a, b`.

Key Takeaway:
Multiple assignment is concise and Pythonic.

## Problem 4: Mutability demo
**Difficulty:** ⭐⭐⭐  
**Prerequisites:** Lists basics

Problem Statement:
Show how modifying a list through one variable affects another variable that references the same list.

Solution:

```python
list1 = [1, 2, 3]
list2 = list1       # both names refer to same list object
list2.append(4)     # mutate the list via list2
print(list1)        # prints: [1, 2, 3, 4]
print(list2)        # prints: [1, 2, 3, 4]
```

Common mistake: expecting `list1` to remain unchanged. To copy the list instead:

```python
list1 = [1, 2, 3]
list2 = list1.copy()  # creates a shallow copy
list2.append(4)
print(list1)  # still [1, 2, 3]
```

Key Takeaway:
Understand references and mutability to avoid accidental shared-state bugs.

## Problem 5: Constants and naming conventions
**Difficulty:** ⭐⭐  
**Prerequisites:** Naming rules

Problem Statement:
Define a constant PI with value 3.14159 and use it to compute the area of a circle with radius 2.

Solution:

```python
PI = 3.14159  # convention: uppercase name signals constant
radius = 2
area = PI * radius * radius
print(area)  # prints 12.56636
```

Key Takeaway:
Python has no true constants; naming conventions communicate intent.

## Practice Problems (Independent Practice)

## MCQ Knowledge Check
Q1: Which of these is a valid variable name in Python?  
a) 2nd_place  
b) second-place  
c) second_place  
d) second place

**Answer:** c) second_place — starts with a letter and uses underscore.

Q2: After executing `x = 5; x = x + 2`, what is x?  
a) 5  
b) 2  
c) 7  
d) Error

**Answer:** c) 7 — variable updated to new value.

Q3: What does `type("123")` return?  
a) int  
b) str  
c) float  
d) bool

**Answer:** b) str — quotes make it a string.

Q4: Which statement about Python variables is true?  
a) Variable types must be declared before use.  
b) Variables are constant by default.  
c) Variables are references to objects; types determined at runtime.  
d) You cannot reassign a different type to a variable.

**Answer:** c) Variables are references to objects; types determined at runtime.

Q5: Given `a = [1, 2]; b = a; b.append(3)`, what is `a`?  
a) [1, 2]  
b) [1, 2, 3]  
c) Error  
d) [3]

**Answer:** b) [1, 2, 3] — `a` and `b` reference the same list.

Independent Practice Problems (short list)
1. Create variables `first_name` and `last_name`, then print full name in one line. (⭐)  
2. Given `n = 10`, compute `n_squared` and `n_cubed`. (⭐)  
3. Read a number from user input, convert to int, and print whether it is even or odd. (⭐⭐)  
4. Create a list `nums = [1,2,3]`, assign `alias = nums`, then set `alias = alias + [4]`. Does `nums` change? Explain. (⭐⭐⭐)  
5. Write a function `scale(point, factor)` where `point` is a tuple `(x, y)` and return a new scaled tuple. (⭐⭐⭐)

Estimated time: 15–45 minutes.

## Solutions (Independent Practice)

1.

```python
first_name = "Sam"
last_name = "Li"
print(first_name, last_name)  # Sam Li
```

2.

```python
n = 10
n_squared = n * n
n_cubed = n * n * n
print(n_squared, n_cubed)  # 100 1000
```

3.

```python
user = input("Enter a number: ")
num = int(user)            # convert string to integer
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

4. Explanation: Using `alias = nums` makes both names reference the same list. But `alias = alias + [4]` creates a new list and rebinds `alias` to it; `nums` remains unchanged.

```python
nums = [1, 2, 3]
alias = nums
alias = alias + [4]  # creates new list; alias now different
print(nums)   # [1, 2, 3]
print(alias)  # [1, 2, 3, 4]
```

5.

```python
def scale(point, factor):
    x, y = point     # unpack tuple
    return (x * factor, y * factor)

print(scale((2, 3), 3))  # (6, 9)
```

## Common Pitfalls
- Using invalid names: starting with digits or including spaces (e.g., `2nd` or `my var`) causes syntax errors.
- Confusing assignment `=` with equality `==`.
- Mutability surprises: changing a mutable object through one name affects all references.
- Assuming types persist: you can reassign different types to the same variable.
- Relying on implicit globals: prefer passing variables explicitly to functions.

## Summary
Variables are fundamental: they name values, enable computation, and manage program state. Remember the naming rules, the dynamic typing behavior, and the difference between mutability and immutability. Practice with assignments, reassignments, and simple functions to build fluency.