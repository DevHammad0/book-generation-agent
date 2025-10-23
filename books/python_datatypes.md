# Python Datatypes

## Overview  
Imagine you’re building a shopping cart app — you must store item names, quantities, prices, customer details, and whether an order is complete. Choosing the right way to represent each piece of information makes your code reliable, efficient, and easier to maintain.

Learning objectives (you will be able to):
- Identify and use Python's built-in datatypes: numbers, strings, booleans, lists, tuples, sets, dictionaries, and None.
- Convert between related datatypes safely and effectively.
- Choose appropriate datatypes for real-world problems and avoid common pitfalls.
- Write Python code that manipulates datatypes through indexing, slicing, iteration, and built-in methods.
- Debug and test datatype-related edge cases.

Brief theory:
Python provides a set of built-in datatypes to represent data. Each datatype has specific properties: mutability (can it change after creation?), order (is order preserved?), and operations supported (e.g., concatenation, membership tests). Understanding these properties allows you to pick the right structure for a task and avoid bugs.

Analogy:
Think of datatypes as containers in a kitchen: bowls (lists) you can put in, take out, and change; sealed jars (tuples) you can’t change; labeled drawers (dictionaries) where labels map to contents; and a pile of unique spices (sets) where duplicates are automatically removed.

Why it matters:
Correct datatype choice improves performance, clarity, and correctness. For example, using a set for membership checks is much faster than scanning a list for large collections; using tuples for fixed records can prevent accidental modification.

## Key Concepts
- Numbers: int, float, complex
  - int: whole numbers
  - float: floating-point numbers (approximate)
  - complex: complex numbers with real and imaginary parts
- Strings: immutable sequences of characters; support slicing, formatting, and many methods.
- Booleans: True and False; result of logical operations.
- None: a singleton representing absence of a value.
- Lists: ordered, mutable, allow duplicates.
- Tuples: ordered, immutable, allow duplicates, often used for fixed records.
- Sets: unordered, mutable (the set object), only unique elements, fast membership.
- Frozenset: immutable set.
- Dictionaries: unordered (preserve insertion order since Python 3.7), mutable mapping of keys → values.
- Mutability vs immutability: determines whether an object can be changed in place.
- Identity vs equality: `is` checks identity, `==` checks equality.
- Type conversion (casting): int(), float(), str(), list(), tuple(), set(), dict() (where appropriate).
- Sequence operations: indexing, slicing, concatenation (where supported), repetition, membership (`in`), iteration.
- Hashability: necessary for keys in dictionaries and elements in sets — immutable types are usually hashable.

## Examples
Basic literals and type checks:
```python
python
a = 42                # int
b = 3.14              # float
c = 2 + 3j            # complex
s = "Hello, World!"   # str
flag = True           # bool
nothing = None        # NoneType

print(type(a), type(b), type(c), type(s), type(flag), type(nothing))
```

List vs tuple:
```python
python
lst = [1, 2, 3]
tpl = (1, 2, 3)

lst[0] = 10           # allowed
# tpl[0] = 10         # TypeError: 'tuple' object does not support item assignment

lst.append(4)
# tpl.append(4)       # AttributeError: 'tuple' object has no attribute 'append'
```

Set uniqueness and dictionary mapping:
```python
python
items = ["apple", "banana", "apple", "orange"]
unique = set(items)   # {'apple', 'banana', 'orange'}

prices = {"apple": 0.99, "banana": 0.5}
prices["orange"] = 0.8
# iterate keys and values
for fruit, price in prices.items():
    print(fruit, price)
```

String slicing and formatting:
```python
python
name = "Ada Lovelace"
print(name[0])        # 'A'
print(name[-1])       # 'e'
print(name[0:3])      # 'Ada'
print(f"Hello, {name.split()[0]}!")  # f-string formatting
```

Type conversion:
```python
python
num_str = "123"
num = int(num_str)    # 123
flt = float("3.5")    # 3.5
s = str(42)           # "42"
lst = list("abc")     # ['a', 'b', 'c']
tpl = tuple([1, 2])   # (1, 2)
st = set([1, 2, 2])   # {1, 2}
```

## Knowledge Check (MCQs)
Q1: Which datatype is immutable?
a) list
b) dict
c) tuple
d) set

**Answer:** c) tuple — tuples cannot be changed after creation.

Q2: Which operation is fastest for membership checking with large collections?
a) list membership (`x in list`)
b) set membership (`x in set`)
c) string find
d) tuple membership

**Answer:** b) set membership — sets use hashed lookup O(1) average.

Q3: What does `None` represent?
a) A boolean False
b) An integer zero
c) Absence of a value
d) Empty string

**Answer:** c) Absence of a value — None is a singleton used to represent no value.

Q4: Which types are hashable by default? (Choose the best single answer)
a) list, dict
b) tuple (of hashable items), frozenset
c) set, list
d) dict, set

**Answer:** b) tuple (of hashable items), frozenset — hashable types can be dictionary keys or set elements.

Q5: After executing `a = [1, 2]; b = a; b.append(3)`, what's `a`?
a) [1, 2]
b) [1, 2, 3]
c) Error
d) None

**Answer:** b) [1, 2, 3] — both names refer to the same list object (mutability).

Q6: What will `float("nan") == float("nan")` return?
a) True
b) False
c) Error
d) None

**Answer:** b) False — NaN is not equal to itself per IEEE rules.

Q7: Which expression creates an empty dictionary?
a) {}
b) dict()
c) set()
d) both a and b

**Answer:** d) both a and b — {} and dict() create empty dicts; set() creates an empty set.

## Examples and Guided Practice

## Problem 1: Inspecting types
**Difficulty:** ⭐
**Prerequisites:** basic Python, printing

Problem Statement:
Write a function `describe(x)` that prints the type of `x` and whether it is mutable.

Starter Code/Guidance:
- Use `type()` and known mutability rules.

Solution:
```python
python
def describe(x):
    t = type(x)
    # Simple mutability check by type name
    mutable_types = (list, dict, set)
    is_mutable = isinstance(x, mutable_types)
    print(f"value: {x!r}")
    print(f"type: {t.__name__}")
    print("mutable:" , is_mutable)

# Examples
describe([1, 2])
describe((1, 2))
describe({"a": 1})
```

Explanation:
- We check membership in a tuple of known mutable types. This is a heuristic; custom classes may behave differently.

Key Takeaway:
Mutability is a property of the object type; for built-ins lists/dicts/sets are mutable, tuples/strings/numbers are not.

## Problem 2: Safe conversion to int
**Difficulty:** ⭐⭐
**Prerequisites:** casting, exception handling

Problem Statement:
Implement `to_int(s, default=0)` that attempts to convert `s` to int, returning `default` on failure.

Solution:
```python
python
def to_int(s, default=0):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default

# Tests
print(to_int("10"))     # 10
print(to_int("3.5"))    # default 0 because int("3.5") raises ValueError
print(to_int(None, -1)) # -1
```

Explanation:
- int() raises ValueError for non-integer strings and TypeError for None; catch both.

Key Takeaway:
Use exceptions for robust conversions.

## Problem 3: Counting unique words
**Difficulty:** ⭐⭐
**Prerequisites:** strings, sets, loops

Problem Statement:
Write `count_unique_words(text)` returning number of unique lowercase words (split on whitespace).

Solution:
```python
python
import re

def count_unique_words(text):
    # normalize by lowercasing and extracting word tokens
    tokens = re.findall(r"\b\w+\b", text.lower())
    return len(set(tokens))

# Example
print(count_unique_words("Apple apple banana."))  # 2
```

Explanation:
- Regex extracts word characters; set ensures uniqueness.

Key Takeaway:
Sets are ideal for de-duplicating items.

## Problem 4: Dictionary frequency map
**Difficulty:** ⭐⭐⭐
**Prerequisites:** dictionaries, loops, get/setdefault

Problem Statement:
Given a list of items, return a frequency dict mapping item→count.

Solution:
```python
python
def frequencies(items):
    freq = {}
    for it in items:
        freq[it] = freq.get(it, 0) + 1
    return freq

# Example
print(frequencies(["a", "b", "a"]))  # {'a': 2, 'b': 1}
```

Explanation:
- Use dict.get(key, default) for concise counting.

Common mistakes:
- Using list.count in a loop produces O(n^2). The shown approach is O(n).

Key Takeaway:
Dictionaries are efficient for counting and mapping.

## Problem 5: Immutable record with tuple
**Difficulty:** ⭐⭐⭐
**Prerequisites:** tuples, unpacking

Problem Statement:
Create a function `swap_pair(pair)` that takes a 2-tuple and returns a new tuple with elements swapped. Ensure input validation.

Solution:
```python
python
def swap_pair(pair):
    if not isinstance(pair, tuple) or len(pair) != 2:
        raise TypeError("Expected a 2-tuple")
    a, b = pair
    return (b, a)

# Example
print(swap_pair((1, 2)))  # (2, 1)
```

Explanation:
- Tuples are immutable; returning a new tuple preserves immutability.

Key Takeaway:
Use tuples for fixed-size records and safe copying via unpacking.

## Problem 6: Nested data traversal
**Difficulty:** ⭐⭐⭐⭐
**Prerequisites:** recursion, isinstance checks

Problem Statement:
Write `flatten(lst)` that converts a nested list/tuple structure into a flat list of elements (preserve order).

Solution:
```python
python
def flatten(seq):
    result = []
    for item in seq:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Example
print(flatten([1, [2, (3, 4)], 5]))  # [1, 2, 3, 4, 5]
```

Explanation:
- Recursively handle lists/tuples; other iterables (like strings) are treated as scalars here to avoid splitting characters.

Common mistakes:
- Iterating over strings as sequences would split characters; check desired behavior.

Key Takeaway:
Recursion plus isinstance checks handle arbitrary nesting.

## Problem 7: Hashability test
**Difficulty:** ⭐⭐⭐⭐
**Prerequisites:** try/except, set/dict behavior

Problem Statement:
Implement `is_hashable(x)` that returns True if `x` can be used as a dict key or set element.

Solution:
```python
python
def is_hashable(x):
    try:
        hash(x)
        return True
    except TypeError:
        return False

# Examples
print(is_hashable((1, 2)))  # True
print(is_hashable([1, 2]))  # False
```

Explanation:
- hash() raises TypeError for unhashable objects.

Key Takeaway:
Hashability is determined by the object's implemention of __hash__ and immutability guarantees.

## Problem 8: Merge two dictionaries (conflict resolution)
**Difficulty:** ⭐⭐⭐⭐
**Prerequisites:** dict methods, comprehension, function arguments

Problem Statement:
Write `merge_dicts(a, b, strategy="b")` that merges dict a and b. strategy can be:
- "b": values from b override a
- "a": keep a's values on conflict
- "sum": if values are numbers, sum them; otherwise prefer b

Solution:
```python
python
def merge_dicts(a, b, strategy="b"):
    result = a.copy()
    for k, v in b.items():
        if k in result:
            if strategy == "b":
                result[k] = v
            elif strategy == "a":
                pass  # keep existing
            elif strategy == "sum":
                try:
                    result[k] = result[k] + v
                except Exception:
                    result[k] = v
            else:
                raise ValueError("Unknown strategy")
        else:
            result[k] = v
    return result

# Example
print(merge_dicts({"x": 1}, {"x": 2, "y": 3}, strategy="sum"))  # {'x': 3, 'y': 3}
```

Explanation:
- Use copy() to avoid mutating inputs; handle exceptions when summing non-numeric types.

Key Takeaway:
Explicit conflict strategies make merges predictable.

## Independent Practice

## Practice Problem 1: Swap list ends
**Difficulty:** ⭐
Problem:
Write `swap_ends(lst)` that swaps the first and last elements of a list and returns the list. Handle lists shorter than 2 by returning them unchanged.

Hints:
- Remember to modify in place.

Solution:
```python
python
def swap_ends(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
```

## Practice Problem 2: Join unique words
**Difficulty:** ⭐⭐
Problem:
Given a list of strings, return a single string of unique words in insertion order separated by spaces.

Hints:
- Python 3.7+ dict preserves insertion order; use dict.fromkeys or collections.OrderedDict for older versions.

Solution:
```python
python
def unique_join(words):
    return " ".join(dict.fromkeys(words))
```

## Practice Problem 3: Deep copy vs shallow copy
**Difficulty:** ⭐⭐
Problem:
Show via code the difference between shallow and deep copying a list of lists and explain.

Solution:
```python
python
import copy
original = [[1], [2]]
shallow = list(original)          # or original.copy()
deep = copy.deepcopy(original)

shallow[0].append(99)
print(original)  # [[1, 99], [2]] -> changed because inner lists are shared
print(deep)      # [[1], [2]] -> unchanged
```

## Practice Problem 4: Numeric type promotion
**Difficulty:** ⭐⭐
Problem:
What is the type of the result for `1 + 2.0` and why?

Solution:
```python
python
res = 1 + 2.0
print(res, type(res))  # 3.0 <class 'float'>
```
Explanation: int promoted to float in mixed arithmetic.

## Practice Problem 5: Remove duplicates preserving order for large input
**Difficulty:** ⭐⭐⭐
Problem:
Efficiently remove duplicates from a large list while preserving order.

Hints:
- Use set for membership and list for result.

Solution:
```python
python
def remove_duplicates(seq):
    seen = set()
    out = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
```

## Practice Problem 6: Convert list of pairs to dict safely
**Difficulty:** ⭐⭐⭐
Problem:
Given list of (key, value) pairs where keys may repeat, create a dict mapping keys to lists of values.

Solution:
```python
python
from collections import defaultdict

def pairs_to_dict(pairs):
    d = defaultdict(list)
    for k, v in pairs:
        d[k].append(v)
    return dict(d)
```

## Practice Problem 7: Replace None with default in nested dict
**Difficulty:** ⭐⭐⭐⭐
Problem:
Given a dict possibly containing None values at any depth, replace all None with a provided default.

Hints:
- Use recursion and check types.

Solution:
```python
python
def replace_none(obj, default):
    if isinstance(obj, dict):
        return {k: replace_none(v, default) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_none(v, default) for v in obj]
    elif obj is None:
        return default
    else:
        return obj
```

## Practice Problem 8: Merge and sort unique elements
**Difficulty:** ⭐⭐⭐
Problem:
Given two lists of integers, return a sorted list of unique integers present in either list.

Solution:
```python
python
def union_sorted(a, b):
    return sorted(set(a) | set(b))
```

Expected time: 15–45 minutes total for all practice problems.

## Solutions
(Complete solutions are provided inline above with explanations.)

## Mastery Challenges

## Challenge 1: Schema validator for simple JSON-like structures
**Difficulty:** ⭐⭐⭐⭐⭐
Skills Tested: dictionaries, lists, recursion, type checking, error reporting
Time Estimate: 45–90 minutes

Scenario:
You need a lightweight validator that checks whether a nested JSON-like object (dicts/lists/scalars) matches a given schema. The schema format:
- {"type": "int"|"float"|"str"|"bool"|"list"|"dict"|"any", "items": <schema>} for lists, "props": {"name": <schema>, ...} for dict properties, "optional": True for optional keys.

Requirements:
- Validate types recursively.
- Return a list of human-readable error messages with paths (e.g., "root.users[2].age: expected int, got str").
- Support optional properties.

Solution Approach:
1. Recursively traverse the data structure with a path string.
2. For primitives, compare types.
3. For lists, validate each element against schema['items'].
4. For dicts, check required props and validate each present property.
5. Use try/except and isinstance checks; collect errors not exceptions.

Solution (one approach):
```python
python
def validate(data, schema, path="root"):
    errors = []

    typ = schema.get("type", "any")
    optional = schema.get("optional", False)
    if data is None:
        if optional:
            return []
        if typ == "any":
            return []
        errors.append(f"{path}: expected {typ}, got None")
        return errors

    if typ == "any":
        return []

    mapping = {
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
        "list": list,
        "dict": dict
    }

    if typ in ("int", "float", "str", "bool"):
        if not isinstance(data, mapping[typ]):
            errors.append(f"{path}: expected {typ}, got {type(data).__name__}")
        return errors

    if typ == "list":
        if not isinstance(data, list):
            errors.append(f"{path}: expected list, got {type(data).__name__}")
            return errors
        item_schema = schema.get("items", {"type": "any"})
        for i, item in enumerate(data):
            errors.extend(validate(item, item_schema, f"{path}[{i}]"))
        return errors

    if typ == "dict":
        if not isinstance(data, dict):
            errors.append(f"{path}: expected dict, got {type(data).__name__}")
            return errors
        props = schema.get("props", {})
        for key, prop_schema in props.items():
            if key in data:
                errors.extend(validate(data[key], prop_schema, f"{path}.{key}"))
            else:
                if not prop_schema.get("optional", False):
                    errors.append(f"{path}.{key}: missing required property")
        # allow extra keys by default
        return errors

    errors.append(f"{path}: unknown schema type {typ}")
    return errors

# Example usage
schema = {
    "type": "dict",
    "props": {
        "users": {"type": "list", "items": {
            "type": "dict",
            "props": {
                "name": {"type": "str"},
                "age": {"type": "int", "optional": True}
            }
        }}
    }
}

data = {"users": [{"name": "Alice"}, {"name": 123}]}
print(validate(data, schema))
```

Best practices:
- Keep schema expressive but simple.
- Return rich error messages to help debugging.
- For production use, prefer established libraries (jsonschema) but this approach is lighter.

Common pitfalls:
- Over-validating types that should be permissive (e.g., treating bool as int since isinstance(True, int) is True).
- Not handling optional keys properly.

Mentorship Notes:
Professionals would design schema-first and include clear error codes. They’d also consider performance for huge structures and possibly streaming validation.

## Challenge 2: Efficient membership across multiple large collections
**Difficulty:** ⭐⭐⭐⭐⭐
Skills Tested: sets, generators, memory/performance tradeoffs
Time Estimate: 45–90 minutes

Scenario:
You have many large read-only lists of user IDs stored on disk. You need to quickly answer membership queries "is id X present in ANY list?" with minimal memory.

Requirements:
- Design a strategy to answer queries quickly.
- Minimize memory if lists are too large to load simultaneously.

Solution Approaches:
1. Precompute a single on-disk index (e.g., a key-value store or a Bloom filter) that fits memory constraints.
2. Use a Bloom filter for memory-efficient probabilistic membership (false positives possible, no false negatives).
3. If exact answers needed, build a disk-backed hashed index (e.g., SQLite with primary key) for O(log n) or O(1) lookups.

Example Bloom filter approach (simple illustration):
```python
python
# This is a conceptual snippet; use a proper library in production
class SimpleBloom:
    def __init__(self, size):
        self.size = size
        self.bits = 0

    def _hashes(self, item):
        h1 = hash(item)
        h2 = hash(str(item))
        return [(abs(h1) + i * abs(h2)) % self.size for i in range(3)]

    def add(self, item):
        for h in self._hashes(item):
            self.bits |= 1 << h

    def __contains__(self, item):
        return all((self.bits >> h) & 1 for h in self._hashes(item))
```

Mentorship Notes:
Choose Bloom filters for fast, memory-light approximate checks; use exact disk-backed indexes for correctness.

## Challenge 3: Data normalization pipeline
**Difficulty:** ⭐⭐⭐⭐⭐
Skills Tested: strings, typing, dict transforms, edge-case handling
Time Estimate: 60–90 minutes

Scenario:
You receive user-submitted profile data with inconsistent types and missing fields. Build a normalization function that:
- Ensures expected keys are present with correct types (id:int, name:str, active:bool, tags:list[str], score:float).
- Coerces sensible conversions (e.g., "true" → True, "42" → 42).
- Rejects invalid inputs with clear messages.

Solution Approach:
1. Define per-field coercion functions returning (value, error).
2. Apply coercers and collect errors.
3. Return normalized dict or errors.

Example coercers and pipeline:
```python
python
def coerce_int(x):
    try:
        return int(x), None
    except Exception as e:
        return None, f"int: {e}"

def coerce_float(x):
    try:
        return float(x), None
    except Exception as e:
        return None, f"float: {e}"

def coerce_str(x):
    if x is None:
        return "", None
    return str(x), None

def coerce_bool(x):
    if isinstance(x, bool):
        return x, None
    if isinstance(x, str):
        if x.lower() in ("true", "1", "yes"):
            return True, None
        if x.lower() in ("false", "0", "no"):
            return False, None
    if isinstance(x, (int, float)):
        return bool(x), None
    return None, "bool: cannot coerce"

def coerce_tags(x):
    if x is None:
        return [], None
    if isinstance(x, str):
        return [t.strip() for t in x.split(",") if t.strip()], None
    if isinstance(x, list):
        return [str(t) for t in x], None
    return None, "tags: cannot coerce"

def normalize_profile(raw):
    errors = {}
    out = {}
    coercions = {
        "id": coerce_int,
        "name": coerce_str,
        "active": coerce_bool,
        "tags": coerce_tags,
        "score": coerce_float
    }
    for k, fn in coercions.items():
        val, err = fn(raw.get(k))
        if err:
            errors[k] = err
        else:
            out[k] = val
    if errors:
        return None, errors
    return out, None
```

Mentorship Notes:
Design pipelines to be tolerant but explicit; log rejections and provide corrective feedback to users.

## Common Pitfalls
- Confusing identity and equality: use `is` for singletons (None), `==` for value equality.
- Assuming immutability: lists/dicts are mutable — be careful when sharing references.
- Using mutable default arguments in functions (e.g., def f(a, lst=[]): ...) — avoid it.
- Treating bool as distinct from int: isinstance(True, int) is True; use explicit checks if needed.
- Expecting float equality: avoid direct equality checks for floats; use tolerances.
- Using large lists for membership checks — prefer sets or indexes when appropriate.
- Forgetting to handle None and empty values in conversion functions.

## Summary
- Python has a rich set of built-in datatypes, each with trade-offs (mutability, order, hashability).
- Choose sets for uniqueness and fast membership, lists for ordered mutable collections, tuples for fixed records, dictionaries for mappings.
- Understand identity vs equality, and mutability to avoid subtle bugs.
- Use type conversion and validation carefully, catching exceptions and providing clear error reports.
- For real-world systems, consider memory, performance, and correctness trade-offs (Bloom filters, databases, external libraries for validation).

Learning objectives checklist:
- Identify core datatypes: covered
- Convert safely between types: covered with examples and practice
- Choose datatypes for scenarios: covered in challenges and examples
- Manipulate datatypes (index/slice/iterate): shown in examples
- Debug datatype edge cases: common pitfalls and mastery challenges provided

References and further reading:
- Python official docs: Built-in Types section
- collections module (deque, defaultdict, OrderedDict)
- jsonschema and marshmallow for production validation libraries