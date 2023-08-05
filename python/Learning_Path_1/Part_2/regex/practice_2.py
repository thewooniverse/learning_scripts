import re

pattern = re.compile(r"\d+")  # Matches any sequence of digits

print(pattern.fullmatch("123"))  # Matches, because the entire string is digits
print(pattern.fullmatch("123abc"))  # Doesn't match, because the entire string isn't digits
print(pattern.fullmatch(" 123 "))


print(pattern.match("123"))  # Matches, because the string starts with digits
print(pattern.match("abc123"))  # Doesn't match, because the string doesn't start with digits

print(pattern.search("123"))  # Matches, because there are digits in the string
print(pattern.search("abc123"))  # Matches, because there are digits in the string

print(pattern.findall("123"))  # Returns ['123'], because there are digits in the string
print(pattern.findall("abc 123 def 456"))  # Returns ['123', '456'], because those are the sequences of digits in the string
print(pattern.findall("456123abc12385 12935"))

