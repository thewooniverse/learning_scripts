

=========================================================================
Additional regex methods
=========================================================================

Certainly! Regular expressions (regex) are a powerful tool in Python and come with various methods for different use cases. Here are some commonly used methods along with `findall`, `search`, and `match`:

### 1. `sub(pattern, repl, string, count=0, flags=0)`

This method replaces occurrences of the pattern in the given string with a replacement string. If the pattern isn't found, the string is returned unchanged.

```python
import re

text = "Cat, Hat, Mat"
pattern = r'\b[C|M]at\b'
replacement = "Rat"

result = re.sub(pattern, replacement, text)
# Output: 'Rat, Hat, Rat'
```

### 2. `split(pattern, string, maxsplit=0, flags=0)`

This method splits the given string by the occurrences of the pattern.

```python
text = "apple;banana;cherry;date"
pattern = r';'

result = re.split(pattern, text)
# Output: ['apple', 'banana', 'cherry', 'date']
```

### 3. `finditer(pattern, string, flags=0)`

This method returns an iterator yielding `MatchObject` instances over all non-overlapping matches of the pattern in the string. This is similar to `findall`, but instead of returning the matched strings, it returns match objects.

```python
text = "apple banana cherry"
pattern = r'\b\w+\b'

for match in re.finditer(pattern, text):
    print(match.group())
```

### 4. `escape(string)`

This method returns a string with all non-alphanumeric characters escaped by a backslash. This is useful if you want to match a literal string that may have special characters in it.

```python
text = "a.b*c+?|"
pattern = re.escape(text)

result = re.findall(pattern, "a.b*c+?|")
# Output: ['a.b*c+?|']
```

### 5. `compile(pattern, flags=0)`

This method compiles a regex pattern into a regex object. This is useful if you are going to use the same pattern repeatedly since it saves the compiled object for reuse.

```python
pattern = re.compile(r'\d+')
result = pattern.findall("12 34 56")
# Output: ['12', '34', '56']
```

These are some of the other commonly used methods in regex that offer different functionalities for various use cases.