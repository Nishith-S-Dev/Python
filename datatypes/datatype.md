# Object Types / Data Types in Python

Python supports various data types to handle different kinds of data efficiently. Below is a categorized list of common object types and data structures in Python.

## 1. Basic Data Types

### Numbers
Python supports different numerical types:
- **Integer (`int`)**: Whole numbers without a decimal.  
  Example: `1234`, `-42`
- **Floating-point (`float`)**: Numbers with decimals.  
  Example: `3.1415`, `-0.001`
- **Complex (`complex`)**: Numbers with real and imaginary parts.  
  Example: `3+4j`, `5-2j`
- **Binary (`bin`)**: Binary representation of numbers.  
  Example: `0b111` (which is `7` in decimal)
- **Decimal (`decimal.Decimal`)**: High precision floating-point numbers.  
  Example: `Decimal('0.1')`
- **Fraction (`fractions.Fraction`)**: Rational numbers as fractions.  
  Example: `Fraction(1, 3)`

---

### Strings (`str`)
Strings represent text data and can be defined using single, double, or triple quotes:
- Example: `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'`
- Raw strings: `r'C:\path\to\file'`
- Multi-line strings: `"""This is a multi-line string."""`
- String operations: Concatenation (`+`), Repetition (`*`), Slicing (`[:]`), Formatting (`f"{value}"`)

---

## 2. Collections (Sequences & Mappings)

### Lists (`list`)
Lists are ordered, mutable collections of items.
- Example: `[1, 2, 'three', 4.5]`
- List functions: `append()`, `extend()`, `insert()`, `remove()`, `pop()`
- List comprehension: `[x**2 for x in range(5)]`

---

### Tuples (`tuple`)
Tuples are ordered, immutable collections of items.
- Example: `(1, 'spam', 4, 'U')`
- Named tuples: `collections.namedtuple`

---

### Dictionaries (`dict`)
Dictionaries store key-value pairs.
- Example: `{'food': 'spam', 'taste': 'yum'}`
- Dictionary functions: `keys()`, `values()`, `items()`, `get()`, `update()`
- Dictionary comprehension: `{x: x**2 for x in range(5)}`

---

### Sets (`set`)
Sets store unique, unordered elements.
- Example: `set('abc')`, `{'a', 'b', 'c'}`
- Set operations: Union (`|`), Intersection (`&`), Difference (`-`)

---

## 3. Special Data Types

### File Objects
Python provides built-in support for handling files.
- Example:  
  ```python
  with open('data.txt', 'r') as file:
      content = file.read()

### Strings (`str`)
Strings represent text data and can be defined using single, double, or triple quotes:
- Example: `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'`
- Raw strings: `r'C:\path\to\file'`
- Multi-line strings: `"""This is a multi-line string."""`
- String operations: Concatenation (`+`), Repetition (`*`), Formatting (`f"{value}"`)

---
## 2. Slicing in Python
Slicing allows extracting portions of sequences like lists, tuples, and strings using a specific syntax: like this is start from the [1:3] start with index(1) and end with index(3-1)= index(2)
```python
sequence[start:stop:step]