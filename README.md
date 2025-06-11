# Stack_python

Data structure implemented in Python (Stack)

---

# Stack in Data Structures

## 📋 Stack

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. The last element added to the stack is the first one to be removed. Think of it like a stack of plates, where you add and remove plates only from the top.

---

## Characteristics
- Follows **LIFO** order  
- Insertion (`push`) and deletion (`pop`) happen at the **top** only  
- Supports:
  - `push`: add an element to the top  
  - `pop`: remove the top element  
  - `peek` or `top`: view the top element without removing it  
  - `is_empty`: check if the stack is empty  

---

## Example (Python)

```python
stack = []

# Push elements
stack.append(1)
stack.append(2)
stack.append(3)

# Peek top element
print(stack[-1])  # Output: 3

# Pop element
print(stack.pop())  # Output: 3
print(stack)        # Output: [1, 2]
```

---

## Use Cases

- Undo and redo functionality in applications
- Function call management in recursion (call stack)
- Expression evaluation and syntax parsing
- Browser back/forward navigation history
- Depth-first search (DFS) algorithm in graphs and trees

---

## 🚀 Summary

| Feature      | Stack         |
|--------------|---------------|
| Ordering     | LIFO          |
| Insertions   | Top only      |
| Deletions   | Top only      |
| Indexable    | No            |
| Use Case Examples | Undo/redo, function call stack, expression evaluation, DFS |

---
The attached codes are Stacks implemented in Python including a Stack implemented as an array (function version and class), program for reversing strings, algorithm for checking parentheses, algorithm for calculating postfix expressions, program for converting infix expressions to postfix expressions, maze search function using DFS.
All utilize stacks.

