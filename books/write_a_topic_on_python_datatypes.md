# Python Datatypes

## Overview
Hook: Imagine you're building an app that stores user profiles, messages, and preferences. Choosing the right datatype for each piece of information keeps your app fast, correct, and easy to maintain.

Learning Objectives
- 🎯 Identify and explain Python's built-in datatypes (numbers, strings, booleans, lists, tuples, sets, dictionaries, None).
- 🎯 Choose appropriate datatypes for real-world tasks and convert between them safely.
- 🎯 Perform common operations on each datatype and recognize common pitfalls.

Brief Theory
Python provides several built-in datatypes to represent different kinds of values. Numeric types (int, float, complex) represent numbers. Strings represent text. Booleans represent truth values. Collections — lists, tuples, sets, and dictionaries — let you group values. The special value None represents absence of a value. Datatypes determine the operations available and how memory and equality behave.

Analogy
Think of datatypes as different containers: a list is like a shopping bag (ordered, changeable), a tuple is a sealed box (ordered, fixed), a set is a basket that discards duplicates (unordered), and a dictionary is a labeled cabinet (key → value).

Why It Matters
Correct datatype choice improves correctness, performance, and code clarity. Mistakes (like treating a string as a number) cause runtime errors or subtle bugs.

## Key Concepts
- int: whole numbers (unbounded in Python).
- float: floating-point numbers (approximate real numbers).
- complex: complex numbers with real and imaginary parts.
- str: immutable sequence of Unicode characters.
- bool: True or False (subclass of int).
- list: mutable ordered sequence, allows duplicates.
- tuple: immutable ordered sequence.
- set: mutable unordered collection of unique elements.
- dict: mutable mapping from keys to values.
- None: singleton indicating "no value".

Mutability and identity
- Mutable objects (list, dict, set) can change in place; immutable objects (int, float, str, tuple) cannot.
- Use `is` to compare identity, `==` to compare value equality.

Type conversion
- Built-ins: `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()` (for suitable inputs).

## Examples
```python
# Numbers and strings
a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex
s = "Hello"     # str
flag = True     # bool

# Collections
l = [1, 2, 3]               # list
t = (1, 2, 3)               # tuple
st = {1, 2, 3}              # set
d = {"name": "Ava", "age": 30}  # dict

# None
x = None
```

Common operations
```python
# Access and modify list
l[0] = 10
l.append(4)

# Tuple unpacking
a, b, c = t

# Set operations
st.add(4)
st.remove(2)

# Dict access
age = d["age"]
d["city"] = "NY"

# String methods
s_lower = s.lower()
```

## Knowledge Check
Q1: Which datatype is immutable?
a) list
b) dict
c) tuple
d) set

**Answer:** c) tuple — tuples cannot be changed after creation.

Q2: What is the result type of 3 / 2 in Python 3?
a) int
b) float
c) complex
d) str

**Answer:** b) float — division produces a float.

Q3: Which collection disallows duplicate elements?
a) list
b) tuple
c) set
d) dict

**Answer:** c) set — sets contain unique items.

Q4: What does `bool("")` evaluate to?
a) True
b) False
c) Raises an error
d) None

**Answer:** b) False — empty strings are falsy.

Q5: Which expression creates a dictionary?
a) [("a", 1), ("b", 2)]
b) {"a": 1, "b": 2}
c) ("a", 1)
d) {"a", 1}

**Answer:** b) {"a": 1, "b": 2} — key:value pairs inside braces create a dict.

Q6: Which is the correct way to convert the string "123" to an integer?
a) int("123")
b) float("123")
c) str(123)
d) bool("123")

**Answer:** a) int("123")

Q7: What is the value of `type(True)`?
a) bool
b) int
c) str
d) bool subclass of int

**Answer:** a) bool — bool is a distinct type (internally a subclass of int).

## Guided Practice

## Problem 1: Basic number operations
Difficulty: ⭐
Prerequisites: assignment, arithmetic

Problem Statement:
Compute the area of a rectangle with width 7 and height 3, store as a float.

Solution:
```python
# Compute area
width = 7
height = 3
area = float(width * height)  # multiply ints, convert to float
print(area)  # 21.0
```
Key Takeaway: Multiplication returns an int when both operands are ints; convert to float if needed.

## Problem 2: String formatting
Difficulty: ⭐⭐
Prerequisites: strings, f-strings

Problem Statement:
Create greeting "Hello, Alice! You are 30." using variables.

Starter Code:
```python
name = "Alice"
age = 30
```

Solution:
```python
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age}."
print(greeting)
```
Key Takeaway: f-strings easily combine str and non-str types; no manual conversion needed.

## Problem 3: List vs Tuple behavior
Difficulty: ⭐⭐
Prerequisites: lists, tuples, indexing

Problem Statement:
Given a list `a = [1,2,3]` and tuple `b = (1,2,3)`, attempt to change the first element to 10. Show what happens.

Solution:
```python
a = [1, 2, 3]
b = (1, 2, 3)

a[0] = 10  # works because list is mutable
print(a)   # [10, 2, 3]

try:
    b[0] = 10  # raises TypeError because tuple is immutable
except TypeError as e:
    print("Error:", e)
```
Common mistake: Expecting tuple elements to be assignable.

Key Takeaway: Use lists for changeable sequences, tuples for fixed collections.

## Problem 4: Counting unique words
Difficulty: ⭐⭐⭐
Prerequisites: strings, sets, loops

Problem Statement:
Count unique words in "apple banana apple orange banana".

Solution:
```python
text = "apple banana apple orange banana"
words = text.split()        # ['apple', 'banana', 'apple', 'orange', 'banana']
unique = set(words)         # {'apple', 'banana', 'orange'}
count = len(unique)
print(count)                # 3
```
Why: `split()` produces a list; `set()` removes duplicates.

Key Takeaway: Sets are ideal for uniqueness tests.

## Problem 5: Inverting a dictionary
Difficulty: ⭐⭐⭐⭐
Prerequisites: dicts, loops, comprehension

Problem Statement:
Given `d = {"a":1, "b":2, "c":1}`, produce an inverted mapping where values map to lists of keys: `{1: ["a","c"], 2: ["b"]}`.

Solution:
```python
d = {"a": 1, "b": 2, "c": 1}
inv = {}
for k, v in d.items():
    inv.setdefault(v, []).append(k)
print(inv)  # {1: ['a', 'c'], 2: ['b']}
```
Common mistake: Overwriting keys when values repeat; use list-accumulation.

Key Takeaway: Use `setdefault` or defaultdict(list) to group keys by value.

## Practice Problems

## Practice Problem 1: Convert types
Difficulty: ⭐⭐
Problem:
Convert "3.5" to float then to int. What is the result?

Hints:
- Use float() then int()

Solution:
```python
val = "3.5"
f = float(val)
i = int(f)  # truncates to 3
```

## Practice Problem 2: Merge lists
Difficulty: ⭐⭐
Problem:
Given [1,2] and [3,4], create [1,2,3,4].

Solution:
```python
a = [1,2]
b = [3,4]
c = a + b
```

## Practice Problem 3: Remove duplicates preserving order
Difficulty: ⭐⭐⭐
Problem:
From [1,2,2,3,1], produce [1,2,3] preserving first occurrences.

Hints:
- Use a seen set and loop.

Solution:
```python
lst = [1,2,2,3,1]
seen = set()
out = []
for x in lst:
    if x not in seen:
        seen.add(x)
        out.append(x)
# out == [1,2,3]
```

## Practice Problem 4: Safe dict lookup
Difficulty: ⭐⭐
Problem:
Get value for key "x" from d={"x":10}, default to 0 if missing.

Solution:
```python
d = {"x": 10}
val = d.get("x", 0)
```

## Practice Problem 5: Join strings
Difficulty: ⭐
Problem:
Join ["a","b","c"] into "a-b-c".

Solution:
```python
parts = ["a", "b", "c"]
s = "-".join(parts)
```

## Practice Problem 6: Boolean check
Difficulty: ⭐
Problem:
Which values are falsy: 0, "", [], {}, None, False? Return a list of falsy items from [0,"",[],{},None,False,1,"x"].

Solution:
```python
items = [0, "", [], {}, None, False, 1, "x"]
falsy = [x for x in items if not x]  # [0, '', [], {}, None, False]
```

## Practice Problem 7: Tuple assignment
Difficulty: ⭐⭐
Problem:
Swap variables a and b without a temp variable.

Solution:
```python
a = 1
b = 2
a, b = b, a
```

## Practice Problem 8: Dict comprehension
Difficulty: ⭐⭐⭐
Problem:
Create {1:1, 2:4, 3:9} using comprehension.

Solution:
```python
squares = {i: i*i for i in range(1, 4)}
```

Estimated time: 20–45 minutes total for all practice problems.

## Solutions
All practice problem solutions are provided directly after each problem above.

## Common Pitfalls
- Confusing mutability: modifying a list passed into a function will affect the caller.
- Using `==` vs `is`: `is` checks identity, not equality.
- Converting strings to numbers without validation causes ValueError.
- Float precision: 0.1 + 0.2 != 0.3 exactly due to binary representation.
- Using mutable default arguments in functions (e.g., `def f(a, lst=[])`) leads to shared state.

## Mastery Challenges

## Challenge 1: Type-safe JSON loader
Difficulty: ⭐⭐⭐⭐⭐
Skills Tested: dicts, lists, type validation, exceptions
Time Estimate: 45-90 minutes

Scenario:
You receive JSON data with user records where fields may be wrong types. Write a function `normalize_user(record)` that ensures:
- "id" → int (raise ValueError if not convertible)
- "name" → str (strip whitespace)
- "age" → int or None if missing or null
- "tags" → list of unique strings (empty list if missing)
Return normalized dict. Show two approaches: defensive (try/except per field) and declarative (schema mapping).

Solution Approach:
- Defensive: validate and convert each field with try/except and explicit checks.
- Declarative: create a small schema mapping functions and iterate over it.

Example implementation (defensive):
```python
def normalize_user(record):
    out = {}
    # id
    try:
        out["id"] = int(record["id"])
    except Exception:
        raise ValueError("Invalid id")
    # name
    out["name"] = str(record.get("name", "")).strip()
    # age
    age = record.get("age")
    out["age"] = None if age is None else int(age)
    # tags
    tags = record.get("tags") or []
    out["tags"] = list(dict.fromkeys(str(t) for t in tags))
    return out
```

Mentorship Notes:
- Validate inputs early.
- Prefer explicit error messages.
- Consider libraries (pydantic) for larger schemas.

## Challenge 2: Memory-efficient counting
Difficulty: ⭐⭐⭐⭐⭐
Skills Tested: sets, dicts, generator expressions, memory considerations
Time Estimate: 60 minutes

Scenario:
Count unique IP addresses in a very large log file without loading all lines into memory, and report the top 10 most frequent IPs.

Requirements:
- Process file line-by-line.
- Use a memory-efficient counter (consider collections.Counter with streaming or manual dict).
- Provide approach for extremely large distinct IPs (use HyperLogLog approximation or external storage).

Solution Approach:
- Stream file, extract IPs, update counts in a dict (or Counter).
- For huge distinct sets, use probabilistic structures or external DB.

Example (streaming Counter):
```python
from collections import Counter
def top_ips(path, n=10):
    cnt = Counter()
    with open(path) as f:
        for line in f:
            ip = line.split()[0]
            cnt[ip] += 1
    return cnt.most_common(n)
```

Common Pitfalls:
- Building a full set of IPs may exceed memory if billions of unique addresses.

## Challenge 3: Immutable keys and hashing
Difficulty: ⭐⭐⭐⭐
Skills Tested: tuples vs lists, hashing, dict/set keys
Time Estimate: 45 minutes

Scenario:
Design a caching system that uses a function's positional arguments as a cache key. Arguments may include lists; you must create a hashable, canonical key.

Requirements:
- Convert mutable arguments (lists, dicts) into immutable, hashable equivalents.
- Preserve nested structures.
- Provide two approaches: recursive conversion and serialization with canonical JSON.

Solution Approach:
- Recursive conversion: lists → tuples, dicts → sorted tuples of (key, value converted).
- JSON approach: use json.dumps with sort_keys=True then hash the string.

Example (recursive):
```python
def make_hashable(obj):
    if isinstance(obj, dict):
        return tuple((k, make_hashable(obj[k])) for k in sorted(obj))
    if isinstance(obj, list):
        return tuple(make_hashable(x) for x in obj)
    return obj

def key_from_args(*args, **kwargs):
    return (tuple(make_hashable(a) for a in args),
            tuple((k, make_hashable(v)) for k, v in sorted(kwargs.items())))
```

Mentorship Notes:
- Ensure conversion is deterministic.
- Beware of unhashable custom objects — consider providing a serialization hook.

## Summary
You learned Python's core datatypes, their behavior (mutability, operations), and how to choose and convert types. You practiced common operations and solved real-world challenges: data normalization, streaming counting, and building hashable cache keys. Keep experimenting with small programs to solidify these concepts.