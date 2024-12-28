---
title: "Improving Python Function Usability with wrapping"
date: 2024-12-27T12:00:00Z
slug: /12-28-improving-function-usability-a-practical-tip/
description: "A simple approach to modifying Python functions for better usability without altering their core behaviour."
image: images/2024/12-28-function-usability.png
caption: an AI generated image of a python function
categories:
  - til
tags:
  - python
  - coding
  - til
draft: false
---

### **Improving Function Usability: A Practical Tip**

Today I was doing a Solveit tutorial and it touched on a simple way to improve the usability of functions without altering their core behaviour. 

---

### Wrapping Functions for Easier Use

Take Python’s `re.finditer`, for example. It returns an iterator, which you might often need to convert into a list for processing. Instead of repeating `list(re.finditer(...))` all over your code, you can wrap it in a helper function:

```python
import re

def finditer(*args, **kw): 
    return list(re.finditer(*args, **kw))

# Example usage
pattern = r'\d+'
text = "The year is 2024, and the day is 28th."
matches = finditer(pattern, text)
print(matches)  # Output: [<re.Match object>, <re.Match object>]
```

---

### Key Points for Wrapping Functions

#### 1. **Maintain Original Logic**
You need to make sure your wrapper explicitly calls the original function (e.g., `re.finditer`). If you don't do this, you'll lose the functionality of the original function.

#### 2. **Avoid Overwriting the Original**
Instead of reassigning `re.finditer` to the new function (which might have unexpected side effects) you can use a different name - or a similar name that isn't scoped the same way - i.e. `finditer` instead of `re.finditer`.

#### 3. **Keep all the params the same with `*args` and `**kw`**
Use `*args` (to capture positional arguments as a tuple) and `**kw` (to capture keyword arguments as a dictionary). You pass them to the original function.
