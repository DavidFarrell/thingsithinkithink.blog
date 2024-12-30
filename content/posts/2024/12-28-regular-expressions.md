---
title: "Regular Expression Basics"
date: 2024-12-28T12:00:00Z
slug: /12-28-regular-expressions/
description: "Notes and examples on regular expressions"
image: images/2024/12-28-regular-express.png
caption: an AI generated image of some wee guy doing regex by hand
categories:
  - til
tags:
  - til
  - regex
  - coding
draft: false
---

### **Regular Expressions**

Regular expressions have always been a pain in the arse for me. I usually use online generators, or more recently AI to create them.  On a recent Solveit tutorial, I finally got my head around some basics. 

A thing to note: I’m using the [wrapped version of `finditer`]({{< relref "12-28-improving-function-usability-a-practical-tip" >}}) here, so it always returns a list.

---

### Finding a Simple Char Using Regex  

If I have a string like this:  

```python
ss = "467...114...35...633...#...617...+...58...592...755...$...664...598."
```  

Then this regex finds `7`s in the string.
```python
finditer('7', ss)
```
Output:
```
[<re.Match object; span=(2, 3), match='7'>,
<re.Match object ; span=(42, 43), match='7'>,
<re.Match object; span=(76, 77), match='7'>]
```

You can see that (as with similar Python functions like [`slice`](https://docs.python.org/3/library/functions.html#slice)), the first number in the [`Match`](https://docs.python.org/3/library/re.html#re.Match) object is the index of the "find" (e.g., at position 2, there is indeed a `7`), and the second number is the first space outside the match (e.g., at position 3, we are no longer matching).

---

### Finding Any Items in a Set  

This syntax (square brackets `[]`) finds any items in the set:  

```python
finditer('[0123456789]', ss)
```  

Output:  

```python
[<re.Match object; span=(0, 1), match='4'>,
 <re.Match object; span=(1, 2), match='6'>,
 <re.Match object; span=(2, 3), match='7'>,
 ...]
```  

That works, but it’s annoying to put all the numbers in. You can use a hyphen to say "all things between these two" (e.g., `0-9` or `a-z`):  

```python
finditer('[0-9]', ss)
```  

---

### Character Classes  

A character class includes everything in the set `[0-9]`. You can define a character class like that.  

Some character classes are used so often there are shortcuts:  

- `\d` is the character class for digits.  

So this also works the same:  

```python
finditer(r'\d', ss)
```  

---

### Using `r` for Raw Strings  

You need the `r` first because `\d` is a command character, so the `r` communicates not to treat the backslash that way.  

`r` basically tells Python, "everything in this string—see where you see a `\`, I actually mean `\`, not to interpret the next char as a command or special char, etc."  

It’s not a bad idea to always use `r` whenever you’re writing a regular expression.

---

### Finding Instances of Multiple Items  

If we do a search like above, we’d find each instance of a digit in the string:  

```python
[<re.Match object; span=(0, 1), match='4'>,
 <re.Match object; span=(1, 2), match='6'>,
 <re.Match object; span=(2, 3), match='7'>,
 <re.Match object; span=(5, 6), match='1'>,
 ...]
```  

We probably (I dunno in general, but in this case for sure) want to find a whole number, not each of the digits in that number (e.g., in our string, we’d want to find `467`, `114`, etc., not `4`, `6`, `7`, `1`, `1`, `4`).  

You can specify how many instances of the character class you want using notation after the character class, like this:  

```python
finditer(r'[0-9]+', ss)
```  

This matches one or more of that character class in a row - hence finding the numbers in the string in the way we want. 

```
[<re.Match object; span=(0, 3), match='467'>,
<re.Match object; span=(5, 8), match='114'>,
<re.Match object; span=(22, 24), match='35'>,
<re.Match object; span=(26, 29), match='633'>,
<re.Match object; span=(40, 43), match='617'>,
<re.Match object; span=(57, 59), match='58'>,
<re.Match object; span=(62, 65), match='592'>,
<re.Match object; span=(76, 79), match='755'>,
<re.Match object; span=(91, 94), match='664'>,
<re.Match object; span=(95, 98), match='598'>] 
```

### Finding everything that isn't a digit

You can use the `^` to find everything that isn't a digit.

```python
finditer(r'[^0-9]', ss)
```

### Escaping Special Characters

Special characters are characters that have a special meaning in regex. For example, `.` matches any character and `*` matches zero or more of the previous character. 

Therefore, if you want to find a dot, you need to escape it with a backslash.
```python
finditer(r'\.', ss)
```

### A bunch of common special chars

```
.      Matches any single character except a newline.
^      Matches the start of a line or string.
$      Matches the end of a line or string.
*      Matches zero or more occurrences of the preceding character or group.
+      Matches one or more occurrences of the preceding character or group.
?      Matches zero or one occurrence of the preceding character or group (makes quantifiers lazy if placed after them).
|      Acts as an OR operator between patterns.
()     Groups characters or expressions and captures them for back-referencing.
[]     Denotes a character class. Matches any character inside the brackets.
       - Example: [a-z] matches any lowercase letter.

{}     Specifies the number of occurrences of the preceding character or group.
       - Example: a{2,4} matches "aa", "aaa", or "aaaa".

\      Escapes special characters or introduces special sequences.
       - Example: \. matches a literal dot.

\d     Matches any digit (equivalent to [0-9]).
\D     Matches any non-digit.
\w     Matches any word character (letters, digits, and underscores).
\W     Matches any non-word character.
\s     Matches any whitespace character (spaces, tabs, etc.).
\S     Matches any non-whitespace character.
\b     Matches a word boundary.
\B     Matches a non-word boundary.
\n     Matches a newline character.
\t     Matches a tab character.

(?=...) Positive lookahead. Asserts that what follows is a match for the pattern in parentheses.
(?!...) Negative lookahead. Asserts that what follows is NOT a match for the pattern in parentheses.
(?<=...) Positive lookbehind. Asserts that what precedes is a match for the pattern in parentheses.
(?<!...) Negative lookbehind. Asserts that what precedes is NOT a match for the pattern in parentheses.
(?:...) Non-capturing group. Groups expressions but does not capture them.
```

---

### Playing with Regex  

[regex101.com](https://regex101.com/) is a handy site where you can work on your regex iteratively in a webpage.  

It will show you matches but also explain in plain English what is going on.  
![Regex Example](/images/2024/regexexample.png)

See alsp: [pythonium.net](https://pythonium.net/regex) (thx [cyr1l0u](https://github.com/cyr1l0u)) , offering a visual regex tester specifically designed for Python.  