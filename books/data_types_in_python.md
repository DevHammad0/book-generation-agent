# Data Types in Python

## Overview

You’re about to unlock one of Python’s superpowers: understanding the different kinds of data you can work with and how Python stores and manipulates them. Think of data types as the basic ingredients in your programming recipe. Knowing what each ingredient can do helps you write clearer, safer, and faster code.

🎯 Learning Objectives
- Identify the main built-in data types in Python (int, float, str, bool, list, tuple, dict, set).
- Understand mutability vs. immutability and how it affects code behavior.
- Recogn choose appropriate data types for common tasks and perform basic operations on them.
- Recognize common pitfalls and plain-language explanations for type-related errors.

**What you’ll learn in this micro-topic:**
- Core concepts of Python data types
- Simple operations for numbers, text, and collections
- How mutability impacts variable behavior
- Real-world examples to solidify understanding

## Key Concepts

- *Primitive vs. composite types*: Python’s built-in types include simple primitives (integers, floats, booleans, strings) and composite structures (lists, tuples, dictionaries, sets).
- *Mutability*: Some objects can be changed after creation (mutables: lists, dicts, sets); others cannot (immutables: ints, floats, strings, tuples).
- *Type inference*: Python infers the type automatically; you don’t usually declare types explicitly (but you can with type hints).
- *Common operations*: arithmetic on numbers, concatenation and formatting with strings, membership tests, indexing and slicing for sequences, and key-based access for dictionaries.

> Why this matters: Choosing the right data type helps your code be more readable, prevents certain bugs, and improves performance in some cases (e.g., using tuples for fixed data and lists for collections that change).

## Examples

- Numbers
  - Integers: 42, -3
  - Floats: 3.14, -0.001
  - Operations: +, -, *, /, // (floor division), ** (power)

- Text
  - Strings: "Hello", 'World'
  - Concatenation: "Hello" + " " + "World"
  - Repetition: "Hi" * 3
  - Slicing: "Python"[0:2] -> "Py"

- Booleans
  - True, False
  - Used in conditionals: if is_valid: ...

- Lists (mutable)
  - [1, 2, 3]
  - Change: my_list.append(4)

- Tuples (immutable)
  - (1, 2, 3)
  - Cannot assign: t[0] = 10  # error

- Dictionaries (mutable)
  - {"name": "Alex", "age": 30}
  - Access: d["name"]; Update: d["age"] = 31

- Sets (mutable)
  - {1, 2, 3}
  - Unique elements: set([1, 2, 2, 3]) -> {1, 2, 3}

- Type hints (optional)
  - def add(a: int, b: int) -> int: return a + b
  - Helps with readability and tooling

## Practice Problems

### Practice Problem 1: Basic Types
**Difficulty:** ⭐
**Problem:** Determine the type of each expression.
- a) 10
- b) 3.14
- c) "data"
- d) True

**Solution:**
- a) int
- b) float
- c) str
- d) bool

**Key Takeaway:** Python infers types from literal values.

### Practice Problem 2: Mutable vs Immutable
**Difficulty:** ⭐
**Problem:** What happens to a variable after appending to a list?
```
nums = [1, 2, 3]
nums.append(4)
```
- A) nums becomes [1, 2, 3, 4]
- B) nums becomes [1, 2, 3]
- C) It raises an error
- D) It becomes [4, 1, 2, 3]

**Solution:** A) nums becomes [1, 2, 3, 4]. Lists are mutable; append modifies the existing list.

### Practice Problem 3: Indexing and Slicing
**Difficulty:** ⭐
**Problem:** What is the result of `"Python"[1:4]`?
- A) "Pyt"
- B) "ytho"
- C) "ytho"
- D) "yth"

**Solution:** C) "ytho" (indexes 1 through 3)

### Practice Problem 4: Dictionaries
**Difficulty:** ⭐
**Problem:** Given `d = {"a": 1, "b": 2}`, how do you update the value for key "a" to 10?
- A) d["a"] = 10
- B) d.update("a": 10)
- C) d[0] = 10
- D) d("a") = 10

**Solution:** A) d["a"] = 10

### Practice Problem 5: Sets
**Difficulty:** ⭐
**Problem:** What does `set([1, 1, 2, 3])` produce?
- A) [1, 1, 2, 3]
- B) {1, 2, 3}
- C) {1, 1, 2, 3}
- D) An error

**Solution:** B) {1, 2, 3} (duplicates removed)

### Practice Problem 6: Type Hinting
**Difficulty:** ⭐
**Problem:** What is the purpose of type hints in Python?
- A) They enforce types at runtime
- B) They help tooling and readability
- C) They convert types automatically
- D) They slow down execution

**Solution:** B) They help tooling and readability (not enforced at runtime by default)

## Guided Practice

### Problem 1: Working with Numbers
**Difficulty:** ⭐⭐
**Prerequisites:** Basic arithmetic

**Problem Statement:**
Compute the value of the expression and explain the type of the result.
```
x = 7
y = 2.0
result = x / y
```

**Starter Code/Guidance:**
- Remember Python’s / yields a float.

**Solution:**
```
# Explanation
# x is int, y is float; / performs true division and yields a float.
x = 7
y = 2.0
result = x / y  # 3.5
# Type of result
result_type = type(result)  # <class 'float'>
```

**Key Takeaway:** Division with / always yields a float (even if operands are integers).

### Problem 2: String Manipulation
**Difficulty:** ⭐⭐
**Prerequisites:** Strings

**Problem Statement:**
Concatenate the first and last name with a space, then return the length of the full name.

**Solution:**
```
first = "Ada"
last = "Lovelace"
full = first + " " + last  # "Ada Lovelace"
length = len(full)         # 12
```

**Key Takeaway:** Strings support concatenation with + and length with len().

### Problem 3: List Operations
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Lists

**Problem Statement:**
Given `nums = [1, 2, 3]`, perform the following:
- Append 4
- Remove 2
- What is the final list?

**Solution:**
```
nums = [1, 2, 3]
nums.append(4)    # [1, 2, 3, 4]
nums.remove(2)    # [1, 3, 4]
```

**Key Takeaway:** Lists are mutable; methods like append and remove change the list in place.

### Problem 4: Tuple vs List
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Tuples, lists

**Problem Statement:**
Why would you choose a tuple over a list for storing coordinates (x, y) = (3, 5)?

**Solution:**
- Tuples are immutable (cannot change after creation), which makes them safer for fixed data like coordinates.
- They can be used as dictionary keys if they contain only immutable elements.
- They often incur less overhead than lists.

**Key Takeaway:** Use tuples for fixed collections of items; use lists for mutable collections.

### Problem 5: Dictionary Lookup
**Difficulty:** ⭐⭐⭐⭐
**Prerequisites:** Dictionaries

**Problem Statement:**
Safe retrieval: get the value for key "color" from `cfg = {"color": "blue"}` with a default of "red" if the key is missing.

**Solution:**
```
cfg = {"color": "blue"}
color = cfg.get("color", "red")  # "blue"

missing = {}.get("color", "red")  # "red"
```

**Key Takeaway:** Use dict.get(key, default) to avoid KeyError and provide defaults.

### Problem 6: Set Operations
**Difficulty:** ⭐⭐⭐⭐
**Prerequisites:** Sets

**Problem Statement:**
Compute the unique elements from two lists: [1, 2, 2, 3] and [2, 3, 4].

**Solution:**
```
a = [1, 2, 2, 3]
b = [2, 3, 4]
unique = set(a) | set(b)  # {1, 2, 3, 4}
```

**Key Takeaway:** Sets automatically deduplicate and support standard operations like union.

### Problem 7: Type Casting
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Basic types

**Problem Statement:**
Convert the string "2025" to an integer and add 5.

**Solution:**
```
s = "2025"
num = int(s)  # 2025
result = num + 5  # 2030
```

**Key Takeaway:** Use int(), float(), str() for explicit conversions when needed.

### Problem 8: Mixed Type Pitfalls
**Difficulty:** ⭐⭐⭐
**Prerequisites:** Basic arithmetic

**Problem Statement:**
Predict the result and type of `3 + 4.0` and explain why.

**Solution:**
```
# 3 + 4.0 -> 7.0
# Type is float because mixing int and float promotes to float
```

**Key Takeaway:** When mixing int and float in arithmetic, Python promotes to float.

## Independent Practice

### Practice Problem 1: Basic Type Inference
**Difficulty:** ⭐
**Problem:** What is the type of `"123" * 2`? What is the value?

**Hints:**
- Consider string repetition behavior.

**Solution:**
- Type: str
- Value: "123" repeated twice → "123123"

### Practice Problem 2: Mutable Collections
**Difficulty:** ⭐⭐
**Problem:** Start with `data = [1, 2, 3]`. Perform `data[1] = 20`. What is `data`?

**Solution:**
- data becomes [1, 20, 3]

### Practice Problem 3: Immutable Case
**Difficulty:** ⭐⭐
**Problem:** What happens if you try `t = (1, 2, 3); t[0] = 10`?

**Solution:**
- Raises TypeError: cannot assign to immutable object.

### Practice Problem 4: Dictionary Keys
**Difficulty:** ⭐⭐⭐
**Problem:** Can a dictionary key be a list? Why or why not?

**Solution:**
- No, lists are mutable and unhashable, so they cannot be dictionary keys.

### Practice Problem 5: Set Theory
**Difficulty:** ⭐⭐⭐
**Problem:** Given `s = {1, 2, 3}` and `t = {3, 4, 5}`, compute the intersection and union.

**Solution:**
- Intersection: {3}
- Union: {1, 2, 3, 4, 5}

### Practice Problem 6: Type Hints
**Difficulty:** ⭐⭐⭐
**Problem:** Write a function with type hints that adds two numbers.

**Solution:**
```python
def add(a: int, b: int) -> int:
    return a + b
```

### Practice Problem 7: String Formatting
**Difficulty:** ⭐⭐⭐
**Problem:** Format the string to say "Hello, Ada" using the name variable.

**Solution:**
```python
name = "Ada"
greeting = f"Hello, {name}"
```

### Practice Problem 8: List Comprehension with Types
**Difficulty:** ⭐⭐⭐
**Problem:** Create a list of squares for numbers 0 through 9.

**Solution:**
```python
squares = [n*n for n in range(10)]
```

## Mastery Challenge

### Challenge 1: Real-World Scenario — Student Records
**Difficulty:** ⭐⭐⭐⭐⭐
**Skills Tested:** Data types, mutability, dictionaries, lists, type hints, error prevention
**Time Estimate:** 45-90 minutes

**Scenario:**
You’re building a tiny in-memory student registry. Each student has a name (string), student_id (int), and a list of grades (floats). You need to:
- Create a registry that can add students, update grades, and compute average grade.
- Ensure the registry uses appropriate data types and handles edge cases (empty grade lists, missing students).

**Requirements:**
- Implement a Student class or data structure that holds name, id, and grades.
- Implement a Registry class with:
  - add_student(name: str, student_id: int) -> None
  - add_grade(student_id: int, grade: float) -> None
  - average_grade(student_id: int) -> float
  - get_student(student_id: int) -> dict or object
- Handle cases where a student has no grades (average should be None or handle gracefully).
- Provide a small demo showing adding students, adding grades, and printing averages.

**Solution Approach (Multiple Approaches Shown):**
- Approach A: Using a simple dictionary-based registry
  - Keys: student_id
  - Values: dict with name (str) and grades (list of float)
  - Implement methods with careful input validation
- Approach B: Using dataclasses (for clarity)
  - @dataclass class Student: name: str; student_id: int; grades: list[float]
  - Registry stores dict[int, Student]
- Edge cases:
  - Non-existent student_id: raise a clear error or return a friendly message
  - Non-float grades: coerce with float() or reject with a message
  - Empty grades list: average returns None

**Mentorship Notes:**
- Start simple and iteratively add features.
- Prefer immutable identifiers (student_id) as dictionary keys; keep mutable lists for grades.
- Use type hints throughout to improve readability and tooling support.
- Consider adding persistence later (e.g., JSON) if you extend this project.

**Best Practices Recap:**
- Keep data structures aligned with real-world concepts (students, grades).
- Validate inputs early to avoid subtle bugs.
- Use Python’s mutability rules to your advantage: choose mutable containers for aggregations (lists) and immutable identifiers (ints, strings) where appropriate.

## Summary

- Python provides a rich set of built-in data types, including numbers, strings, booleans, and collection types like lists, tuples, dictionaries, and sets.
- Understanding mutability helps you predict how data will behave when you modify it.
- Type inference makes Python easy to write, while type hints offer guidance for readability and tooling.
- Practice with a mix of problem types to build fluency in choosing and using the right data type for each task.

If you’d like, I can tailor additional micro-lessons (e.g., deep dives into dictionaries, sets, or type hints) or expand the mastery challenge into a full mini-project.