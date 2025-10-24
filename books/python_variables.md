# Python Variables

## Overview
A variable in Python is a name that refers to a value stored in memory. You use variables to hold data (numbers, text, collections) so your program can read, modify, and reuse it. This lesson teaches what variables are, how to create and use them, common naming conventions, and typical mistakes.

Learning objectives
- Explain what a variable is and how Python binds names to values.
- Create and update variables of common types (int, float, str, bool).
- Use multiple assignment, swapping, and variable naming best practices.
- Recognize and fix common variable-related errors.

Brief theory
In Python, variables are labels that refer to objects. Assignment uses the = operator: the expression on the right is evaluated to produce an object, and the name on the left is bound to that object. Python is dynamically typed: a variable can refer to different types at different times. Names live in namespaces; most beginner code uses the global namespace or local function namespaces.

Analogy
Think of a variable as a sticky note attached to an item. The sticky note has a label (the variable name) and points to the item (the value). You can remove the note and attach it to a different item without changing the items themselves.

Why it matters
Variables let you write reusable, readable code. They make algorithms adaptable to different inputs, support debugging by isolating values, and are the foundation of control flow and data structures.

## Key Concepts

Basic assignment
```python
x = 10          # x refers to an integer object 10
name = "Ada"    # name refers to a string object "Ada"
pi = 3.14159    # float
is_ready = True # boolean
```

Rebinding and dynamic typing
```python
v = 5
v = "five"    # same name now refers to a string
```

Multiple assignment and swapping
```python
a, b = 1, 2           # parallel assignment
a, b = b, a           # swap without temporary variable
```

Mutable vs immutable
- Immutable types (int, float, str, tuple) cannot be changed in place; rebinding creates a new object.
- Mutable types (list, dict, set) can be modified in place.
```python
lst = [1, 2]
lst.append(3)  # modifies the same list object
```

Naming rules and best practices
- Start with a letter or underscore; follow with letters, digits, or underscores.
- Case-sensitive: `count` and `Count` are different.
- Avoid Python keywords (e.g., `for`, `if`, `class`).
- Use descriptive names, e.g., `user_age` instead of `u`.

Memory note (brief)
Names point to objects; multiple names can refer to the same object (aliasing). For immutable objects aliasing is harmless; for mutable objects it can cause side effects.

Knowledge check (MCQs)
Q1: What does the statement `x = 3` do?
a) Creates a variable named 3  
b) Binds the name x to the integer object 3  
c) Declares the type of x to be int  
d) Allocates memory for x but leaves it empty

**Answer:** b) Binds the name x to the integer object 3 — assignment evaluates the right side and binds the name.

Q2: Which is a valid variable name?
a) 2nd_value  
b) total-sum  
c) _result  
d) for

**Answer:** c) _result — starts with underscore, valid. Others start with digit, contain hyphen, or are a keyword.

Q3: After `a = [1, 2]; b = a; b.append(3)`, what is `a`?
a) [1, 2]  
b) [1, 2, 3]  
c) Error — cannot append  
d) None

**Answer:** b) [1, 2, 3] — a and b reference the same list (aliasing).

Q4: Which statement swaps values without a temporary variable?
a) temp = a; a = b; b = temp  
b) a, b = b, a  
c) swap(a, b)  
d) a = b; b = a

**Answer:** b) a, b = b, a — Python supports tuple unpacking for swapping.

Q5: Which of these is immutable?
a) list  
b) dict  
c) tuple  
d) set

**Answer:** c) tuple — tuples are immutable; others are mutable.

## Examples

Example: Basic operations with variables
```python
# assign
x = 7
y = 2

# arithmetic
sum_xy = x + y
ratio = x / y

# string interpolation
name = "Sam"
greeting = f"Hello, {name}!"

print(sum_xy, ratio, greeting)
```

Example: Aliasing pitfalls with lists
```python
a = [0, 1, 2]
b = a          # aliasing: b references same list
b[0] = 99
# a is now [99, 1, 2]

# to avoid aliasing, copy the list
c = a.copy()
c[0] = 0
# a remains [99, 1, 2]; c is [0, 1, 2]
```

Example: Constants convention
```python
PI = 3.14159   # by convention, uppercase signals a constant
MAX_RETRIES = 5
```

## Practice Problems

## Problem 1: Create and print variables
**Difficulty:** ⭐
**Problem:**
Create variables `first_name`, `last_name`, and `age`. Print "My name is <first_name> <last_name> and I am <age> years old."

Hints:
- Use f-strings.

## Problem 2: Swap two variables
**Difficulty:** ⭐⭐
**Problem:**
Given variables `a = 10` and `b = 20`, swap them so `a` becomes 20 and `b` becomes 10 without using a temporary variable.

Hints:
- Use tuple unpacking.

## Problem 3: Sum numeric inputs
**Difficulty:** ⭐⭐
**Problem:**
Read two numbers (strings), convert them to integers, store them in variables, and print their sum.

Hints:
- Use int() conversion.

## Problem 4: Avoid aliasing
**Difficulty:** ⭐⭐⭐
**Problem:**
Given `original = [1, 2, 3]`, create a variable `copied` that is a separate list. Modify `copied` and show `original` is unchanged.

Hints:
- Use list.copy() or slicing.

## Problem 5: Type reassignment
**Difficulty:** ⭐⭐⭐
**Problem:**
Start with `value = 100`. Reassign `value` to be the string "one hundred", then to a list containing the number 100. Print the type after each assignment.

Hints:
- Use type() to inspect types.

## Challenge 1: Word frequency map
**Difficulty:** ⭐⭐⭐⭐⭐
Skills Tested: variables, dict, loops, string methods
Time Estimate: 45 minutes

Scenario:
Write code that reads a string sentence and builds a dictionary mapping each lowercase word to its frequency. Ignore punctuation `.,!?` and treat words separated by spaces.

Requirements:
- Use variables for the sentence, cleaned words list, and the frequency dictionary.
- Show top 3 most frequent words.

## Challenge 2: Safe update of configuration
**Difficulty:** ⭐⭐⭐⭐
Skills Tested: variables, dict copying, functions
Time Estimate: 45 minutes

Scenario:
Given a default configuration dict `defaults`, and a user-provided dict `user_conf`, create a new `effective_conf` that starts from defaults and updates with user overrides without mutating `defaults`. Provide two approaches and explain pros/cons.

Requirements:
- Demonstrate shallow copy and copy via dict()
- Show what happens if a value is a nested mutable object

## Challenge 3: Rolling average
**Difficulty:** ⭐⭐⭐⭐
Skills Tested: variables, lists, math
Time Estimate: 45-60 minutes

Scenario:
Implement a function that maintains the last N numeric readings in a variable and returns the rolling average when a new reading arrives. Do not use external libraries.

Requirements:
- Use a list to store last N readings
- Efficiently update state and compute average

## Solutions

Solution to Problem 1
```python
first_name = "Jane"
last_name = "Doe"
age = 28
print(f"My name is {first_name} {last_name} and I am {age} years old.")
```

Key takeaway: Use clear variable names and f-strings for readable output.

Solution to Problem 2
```python
a = 10
b = 20
a, b = b, a
# a is now 20, b is 10
```

Key takeaway: Tuple unpacking swaps cleanly without temporary variables.

Solution to Problem 3
```python
s1 = "7"
s2 = "13"
n1 = int(s1)
n2 = int(s2)
print(n1 + n2)  # 20
```

Key takeaway: Convert input strings to numeric types before arithmetic.

Solution to Problem 4
```python
original = [1, 2, 3]
copied = original.copy()  # or original[:] for a shallow copy
copied.append(4)
# original remains [1, 2, 3]; copied is [1, 2, 3, 4]
```

Key takeaway: Copy mutable objects to avoid unintended aliasing.

Solution to Problem 5
```python
value = 100
print(type(value))  # <class 'int'>

value = "one hundred"
print(type(value))  # <class 'str'>

value = [100]
print(type(value))  # <class 'list'>
```

Key takeaway: Variables can be rebound to different types freely in Python.

Solution sketch for Challenge 1 (word frequency)
```python
import string

sentence = "Hello, world! Hello world."
# remove punctuation
clean = sentence.translate(str.maketrans("", "", ".,!?"))
words = clean.lower().split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# top 3
top3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
print(top3)
```

Solution sketch for Challenge 2 (config copy)
```python
defaults = {"theme": "light", "retries": 3, "paths": ["a", "b"]}
user_conf = {"theme": "dark", "paths": ["x"]}

# approach 1: shallow copy
effective_conf = defaults.copy()
effective_conf.update(user_conf)

# approach 2: copy via dict()
effective_conf2 = dict(defaults)
effective_conf2.update(user_conf)

# note: if 'paths' is a list, both copies still reference the same list object unless you deep-copy
```

Solution sketch for Challenge 3 (rolling average)
```python
class RollingAverage:
    def __init__(self, n):
        self.n = n
        self.window = []
        self.total = 0.0

    def add(self, value):
        self.window.append(value)
        self.total += value
        if len(self.window) > self.n:
            removed = self.window.pop(0)
            self.total -= removed
        return self.total / len(self.window)

# usage
ra = RollingAverage(3)
print(ra.add(10))  # 10.0
print(ra.add(20))  # 15.0
print(ra.add(30))  # 20.0
print(ra.add(40))  # (20+30+40)/3 = 30.0
```

## Common Pitfalls
- Using a hyphen or starting a name with a digit: causes SyntaxError.
- Expecting assignment to copy mutable objects: leads to aliasing bugs.
- Modifying a list while iterating over it: can skip elements or cause unexpected behavior.
- Relying on variable names across functions without passing them: use arguments/returns or proper scope.
- Assuming types: check or convert types before operations.

## Summary
Variables are fundamental labels that bind names to objects. Learn assignment, naming conventions, reassigning across types, and the difference between mutable and immutable objects. Practice creating, updating, and safely copying variables to avoid common bugs.