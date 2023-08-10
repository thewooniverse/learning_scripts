Great! Let's delve into regular expressions.
https://regex101.com/


=========================================================================
Basics
=========================================================================

Regular expressions (regex) are a powerful tool used to match and manipulate strings. In Python, the built-in `re` module is used to work with regular expressions. They can be extremely helpful in extracting information from text such as log files or writing servers, parsing and restructuring text data, or even in machine learning tasks like text preprocessing and cleaning.

Here are the basics of using the `re` module and regular expressions in Python:

1. **Importing the module**: First, we need to import the `re` module using `import re`.

2. **Basic patterns**: Regular expressions use special (meta) characters to match specific types of characters. For example:

   - `\d`: Matches any decimal digit. Equivalent to `[0-9]`.
   - `\D`: Matches any non-digit character.
   - `\s`: Matches any whitespace character.
   - `\S`: Matches any non-whitespace character.
   - `\w`: Matches any alphanumeric character (digits and alphabets). Equivalent to `[a-zA-Z0-9_]`.
   - `\W`: Matches any non-alphanumeric character.

3. **Special Characters**: Some characters like `.` `^` `$` `*` `+` `?` `{` `}` `[` `]` `\` `|` `(` `)` `:` `#` have special meaning in regex. If you want to match them literally, you need to escape them by `\` (backslash).

4. **Using the `re` module functions**: The `re` module offers several functions to work with regular expressions:

   - `re.search(pattern, string)`: This function searches the string for a match to the pattern, returning a match object if found. 

     Example: 
     ```python
     import re

     if re.search("\d", "hello 123"):
         print("There are digits in the string.")
     ```

   - `re.match(pattern, string)`: This function tries to match the pattern at the start of the string.

   - `re.findall(pattern, string)`: This function returns all non-overlapping matches of pattern in string, as a list of strings.

   - `re.sub(pattern, repl, string)`: This function returns the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.

5. **Compiling a pattern for performance**: If a pattern will be used several times, it may be more efficient to compile it into a pattern object first.

   Example:
   ```python
   import re

   pattern = re.compile("\d")
   if pattern.search("hello 123"):
       print("There are digits in the string.")
   ```

Regular expressions can get quite complex, but these basics should be enough to get you started with most of the common tasks. Always test your regular expressions thoroughly to ensure they're working as expected.



================================================================================================
Regular expressions (regex) are sequences of characters that form a search pattern. Regex can be used to check if a string contains a specified pattern. 

Here are some basics:

1. **Special characters**: `. ^ $ * + ? { } [ ] \ | ( )`

    - `.`: Matches any character except newline
    - `^`: Matches the start of the string
    - `$`: Matches the end of the string
    - `*`: Matches zero or more repetitions
    - `+`: Matches one or more repetitions
    - `?`: Matches zero or one repetition
    - `{m,n}`: Matches at least m and at most n repetitions
    - `[abc]`: Matches any of the characters a, b or c
    - `\`: Escapes special characters or signals a special sequence
    - `|`: Acts as a boolean OR
    - `()`: Defines a scope for operators

2. **Special sequences**: `\d \D \s \S \w \W \b \B`

    - `\d`: Matches any decimal digit, equivalent to `[0-9]`
    - `\D`: Matches any non-digit character, equivalent to `[^0-9]`
    - `\s`: Matches any whitespace character
    - `\S`: Matches any non-whitespace character
    - `\w`: Matches any alphanumeric character, equivalent to `[a-zA-Z0-9_]`
    - `\W`: Matches any non-alphanumeric character, equivalent to `[^a-zA-Z0-9_]`
    - `\b`: Matches where the specified characters are at the beginning or at the end of a word
    - `\B`: Matches where the specified characters are present, but NOT at the beginning (or at the end) of a word

3. **Sets**: `[ ] - ^`

    - `[arn]`: Returns a match where one of the specified characters (a, r, or n) are present
    - `[a-z]`: Returns a match for any lowercase character
    - `[A-Z]`: Returns a match for any uppercase character
    - `[0-5][0-9]`: Returns a match for any two-digit numbers from 00 and 59
    - `[^arn]`: Returns a match for any character EXCEPT a, r, and n

Here's a simple example of Python code using a regular expression:

```python
import re

txt = "Hello, my phone number is 123-456-7890 and my email is myemail@gmail.com"
phone = re.search(r'\d{3}-\d{3}-\d{4}', txt)
email = re.search(r'\S+@\S+', txt)

print(f"Phone number: {phone.group()}")
print(f"Email: {email.group()}")
```

In the above example, we use two different regex patterns. The first one `\d{3}-\d{3}-\d{4}` is for matching a phone number, and the second one `\S+@\S+` is for matching an email address.

The best way to learn regular expressions is by practice. A great tool for testing and learning is https://regex101.com. It allows you to enter a regular expression and text to match against, and it provides a real-time explanation and visualization of the regex. 

Remember, regular expressions are very powerful but they can also become very complex and hard to understand. It's good practice to comment your regexes to explain what they're doing.



=========================================================================
Whitespaces:
=========================================================================

A whitespace character is any character or series of characters that represent horizontal or vertical space in typography. When rendered, a whitespace character does not correspond to a visible mark, but typically does occupy an area on a page.

In programming, the most common whitespace characters include:

1. **Space (" ")**: This is the regular space that you enter through the space bar.

2. **Tab ("\t")**: This is the tab space that you get when you press the Tab key.

3. **Newline ("\n")**: This is the space you get when you press the Enter or Return key. It's typically used to separate lines of text.

4. **Carriage Return ("\r")**: This is a control character used to reset a device's position to the beginning of a line of text.

5. **Form Feed ("\f")**: This is a page break character.

6. **Vertical Tab ("\v")**: It's a vertical version of a tab.

The actual list of characters that are considered whitespace can vary depending on the programming language or context. For example, in HTML, non-breaking spaces and other special types of spaces are also considered whitespace. 

In many programming languages, including Python, there are often functions or methods available to identify and deal with whitespace. For example, in Python, the string methods `strip()`, `lstrip()`, and `rstrip()` can be used to remove whitespace from strings. The method `isspace()` can be used to check if a string consists solely of whitespace.






=========================================================================
Examples:
=========================================================================

Sure, I can provide some basic regex patterns for these cases. Note that these are simple examples and might not cover every possible case. 

1. **Email**

```python
import re

pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
email = "example@example.com"
match = re.search(pattern, email)
if match:
    print("Email found:", match.group())
```
This pattern matches a sequence of alphanumeric characters (also allowing for underscores, dots, pluses, and hyphens), followed by the `@` symbol, followed by another sequence of alphanumeric characters (also allowing for hyphens), followed by a dot and another sequence of alphanumeric characters (also allowing for hyphens and dots).

2. **Phone number**

Let's search for US phone numbers, which have the format `xxx-xxx-xxxx`, `(xxx) xxx-xxxx`, `xxx.xxx.xxxx`, or just `xxxxxxxxxx`:

```python
import re

pattern = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
phone_number = "(123) 456-7890"
match = re.search(pattern, phone_number)
if match:
    print("Phone number found:", match.group())
```
This pattern searches for three digits (optionally surrounded by parentheses), followed by an optional separator (a dash, dot, or space), then three more digits, another optional separator, and four more digits.

3. **Ethereum address**

Ethereum addresses are 40 hexadecimal digits long and are often represented with a `0x` prefix:

```python
import re

pattern = r"0x[a-fA-F0-9]{40}"
ethereum_address = "0xc0ffee254729296a45a3885639AC7E10F9d54979"
match = re.search(pattern, ethereum_address)
if match:
    print("Ethereum address found:", match.group())
```
This pattern matches the sequence `0x` followed by 40 hexadecimal digits. 

Remember that regex patterns can get complicated and there's usually a trade-off between simplicity and accuracy. These patterns might not cover all possible cases, but they serve as a good starting point. Always be sure to thoroughly test your regex patterns to ensure they're behaving as expected!



=========================================================================
Escape characters
=========================================================================
In the context of regular expressions, "escaping" a character means treating it as a literal character rather than a special symbol with a specific function. 

For instance, consider the period `.` character. In regex, a `.` has the special function of matching any character (except a newline). If you want to match a literal period (like in a web address or an email address), you need to "escape" it by preceding it with a backslash `\`.

Here's a small example:

```python
import re

# Without escaping the period
pattern = r"a.b"
string = "axb ayb a.b"
matches = re.findall(pattern, string)
print(matches)  # prints ['axb', 'ayb', 'a.b']

# Escaping the period
pattern = r"a\.b"
string = "axb ayb a.b"
matches = re.findall(pattern, string)
print(matches)  # prints ['a.b']
```

In the first case, `a.b` matches any three-character sequence that starts with 'a' and ends with 'b'. In the second case, `a\.b` only matches the exact string 'a.b'.

So, escaping is a way to tell the regex engine to treat a special character as a literal character.





=========================================================================
\bWORD\b
=========================================================================

In this regular expression, the `\b` at the start and end are word boundary matches. They ensure that the pattern they surround must exist as a standalone word, and not as a part of another word.

Let's break this down:

- `\b`: This is a word boundary. This means that the pattern after this must either be at the start of the string, or must follow a non-word character (a character that is not a letter, number, or underscore).

- `[A-Za-z0-9._%+-]+`: This matches any word character (letters, digits, underscore), or any of the characters inside the square brackets `.` `%` `+` `-`. The `+` sign after the square brackets indicates that the pattern inside the square brackets must occur one or more times.

- `@`: This matches the `@` character literally.

- `[A-Za-z0-9.-]+`: This matches any word character (letters, digits, underscore), or any of the characters inside the square brackets `.` `-`. The `+` sign after the square brackets indicates that the pattern inside the square brackets must occur one or more times.

- `\.`: This matches the `.` character literally.

- `[A-Z|a-z]{2,}`: This matches two or more occurrences of any of the characters inside the square brackets `A-Z` `a-z`.

- `\b`: This is a word boundary. This means that the pattern before this must either be at the end of the string, or must be followed by a non-word character (a character that is not a letter, number, or underscore).

So, in this email regular expression, the `\b` at the start and end ensure that the email address is a standalone word and is not part of another word. For example, without the word boundaries, `hello@domain.com` in `myhello@domain.comemail` would be a valid match, but with the word boundaries, it is not a valid match. This helps to avoid false positives when matching.






=========================================================================
Using separate regexes for different patterns
=========================================================================
Absolutely. It's often better to use more specific regular expressions when you can, since they're less likely to match unwanted patterns. 

In the case of phone numbers, having a distinct pattern for each country or a set of countries that share a similar pattern, allows you to be more precise in your matching, and it also allows you to add country-specific validations, for example, area codes or number lengths.

For example, you might use one pattern for North American phone numbers, which follow the format `+1 (555) 555-5555`, and a different pattern for UK phone numbers, which might look like `+44 20 1234 5678`.

Here's an example how you can handle this in Python:

```python
import re

# Pattern for North American phone numbers
na_pattern = re.compile(r"\+1\s*\(\d{3}\)\s*\d{3}-\d{4}")

# Pattern for UK phone numbers
uk_pattern = re.compile(r"\+44\s*\d{2}\s*\d{4}\s*\d{4}")

phone_numbers = [
    "+1(234)5681231",
    "+44 20 1234 5678",
    # Add more numbers for testing
]

for number in phone_numbers:
    if na_pattern.fullmatch(number):
        print(f"'{number}' is a valid North American phone number.")
    elif uk_pattern.fullmatch(number):
        print(f"'{number}' is a valid UK phone number.")
    else:
        print(f"'{number}' is not a valid phone number.")
```

This way, you are more certain that a match really is a valid phone number, and not some other kind of number that happens to match your pattern. However, the trade-off is that you need to maintain multiple patterns and know which one(s) to use in a given situation. And there are still many other formats for different countries which you might need to consider, so it can become complex.




=========================================================================
Full Match
=========================================================================
Sure! In Python's `re` module, there are four methods that can be used to match regex patterns: `match()`, `search()`, `findall()`, and `fullmatch()`. Here is how `fullmatch()` is different from the others:

1. **fullmatch()**: Determines if the **entire string** strictly matches the pattern. This means no extra characters before or after the pattern. If the entire string matches the pattern, a match object is returned, else `None` is returned.

2. **match()**: Determines if the **start of the string** matches the pattern. If the start of the string matches the pattern, a match object is returned, else `None` is returned.

3. **search()**: Searches the string for a match to the pattern anywhere in the string (not just at the start). It returns a match object for the **first occurrence**. If no matches are found, it returns `None`.

4. **findall()**: Returns a list containing **all** matches of the pattern in the string. If no matches are found, it returns an empty list.

Here are some examples to illustrate the differences:

```python
import re

pattern = re.compile(r"\d+")  # Matches any sequence of digits

print(pattern.fullmatch("123"))  # Matches, because the entire string is digits
print(pattern.fullmatch("123abc"))  # Doesn't match, because the entire string isn't digits

print(pattern.match("123"))  # Matches, because the string starts with digits
print(pattern.match("abc123"))  # Doesn't match, because the string doesn't start with digits

print(pattern.search("123"))  # Matches, because there are digits in the string
print(pattern.search("abc123"))  # Matches, because there are digits in the string

print(pattern.findall("123"))  # Returns ['123'], because there are digits in the string
print(pattern.findall("abc 123 def 456"))  # Returns ['123', '456'], because those are the sequences of digits in the string
```




=========================================================================
: in regex
=========================================================================
The colon `:` itself does not have a special meaning in regular expressions. It is simply matched literally.

However, it is worth noting that the colon is often used in conjunction with other characters to form certain constructs. For example:

1. **In lookaheads and lookbehinds:** A colon is used after `?` in the syntax of lookaheads and lookbehinds, which are special types of non-capturing groups. For instance, `(?<=:)` is a lookbehind that checks if a colon is before the current position.

2. **In POSIX character classes:** A colon is used in the syntax of POSIX character classes. These are special sequences that represent certain types of characters. They are written in the format `[:classname:]`, where `classname` is the name of the character class. For instance, `[:digit:]` matches any decimal digit.

But outside these and similar constructs, if you see a `:` in a regular expression, it is probably just matching a literal colon.

Example:

```python
import re

# Matches a literal colon
print(re.findall(r':', 'Hello:World'))  # Output: [':']

# Matches any digit characters due to the use of POSIX character class [:digit:]
print(re.findall(r'[[:digit:]]', 'Hello123'))  # Output: ['1', '2', '3']
```



=========================================================================
(?:) in regex
=========================================================================

In a regular expression (regex), the colon `:` doesn't have any special meaning on its own. However, in the context you're referring to, the `:` is within a `(?:)` structure, which is a non-capturing group.

Here's a breakdown:

- **Parentheses `()`**: In regex, parentheses are used to define a group. Anything within the parentheses is treated as a single unit and can be quantified, or have other operations applied to it. The match of this group can be retrieved separately in the results.

- **Question mark and colon `(?:)`**: Normally, the regex engine will capture the text that a group matches and store them in a backreference. However, sometimes you want to group the pattern, but you don't want to store the match. This is when you use the `(?:)` syntax. The `?:` inside the parentheses tells the regex engine to treat the parentheses as a non-capturing group, i.e., a group that's used for grouping only, and not for capturing the result. 

In your regex pattern `phone_number_pattern = r"\+?\d{1,3}?[-.\s]?\(?(?:\d{2,3})?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}"`, `(?:\d{2,3})?` is a non-capturing group that matches 2 or 3 digits, and the group itself is optional (because of the trailing `?`), but its match is not captured or stored for later use. This means you can't refer back to this match in the regex or retrieve it separately in the results. It's purely for grouping in this pattern.



=========================================================================
Lookahead and lookbehinds
=========================================================================
In regular expressions, lookaheads and lookbehinds (collectively called "lookaround") are types of zero-width assertions. This means they match a pattern based on what comes before or after it, without consuming characters in the string. 

1. **Lookahead**: This checks if the lookahead assertion can be matched ahead of the current point in the regex. It doesn't consume characters, and it doesn't alter where the pattern is applied in the string. There are two types of lookaheads:

    - **Positive Lookahead (?=...)**: This succeeds if the contained regular expression successfully matches at the current position, and fails otherwise. But, again, it doesn't consume any of the string.
    
        For example, the pattern `r"\w+(?=\.)"` would match any word immediately followed by a period, but the period itself would not be part of the match.
    
        ```python
        import re
        s = "Hello. This is a test."
        print(re.findall(r"\w+(?=\.)", s))  # Output: ['Hello', 'test']
        ```

    - **Negative Lookahead (?!...)**: This is the opposite of positive lookahead. It succeeds if the contained regular expression does not match at the current position in the string.
    
        For example, the pattern `r"\b\w*(?!test)\b"` would match any word that is not 'test'.
    
        ```python
        import re
        s = "test pass fail test success"
        print(re.findall(r"\b\w*(?!test)\b", s))  # Output: ['', ' pass', ' fail', '', ' success', '']
        ```

2. **Lookbehind**: This checks if the lookbehind assertion can be matched before the current point in the regex. Like lookahead, it doesn't consume characters, but there is a limitation: lookbehinds must be a fixed length. There are two types of lookbehinds:

    - **Positive Lookbehind (?<=...)**: This succeeds if the contained regular expression successfully matches coming before the current point.
    
        For example, the pattern `r"(?<=@)\w+"` would match any word that is preceded by '@'.
    
        ```python
        import re
        s = "@user mentioned @handle in a tweet."
        print(re.findall(r"(?<=@)\w+", s))  # Output: ['user', 'handle']
        ```
    
    - **Negative Lookbehind (?<!...)**: This succeeds if the contained regular expression does not match coming before the current point.
    
        For example, the pattern `r"(?<!@)\b\w+\b"` would match any word that is not preceded by '@'.
    
        ```python
        import re
        s = "@user mentioned handle in a tweet."
        print(re.findall(r"(?<!@)\b\w+\b", s))  # Output: ['mentioned', 'handle', 'in', 'a', 'tweet']
        ```
    
Lookaheads and lookbehinds can be very useful in a variety of circumstances when you need to match a pattern based on what comes before or after it. Note, however, that because they are zero-width assertions, they don't consume characters in the string, and the matched assertion is not part of the returned match.







=========================================================================
() and grouping
=========================================================================
Parentheses `()` in regular expressions have two main functions: 

1. **Grouping:** Parentheses can be used to define the scope and precedence of operators. For example, in the pattern `(ab)+`, the `+` applies to the entire group `ab`, meaning "one or more repetitions of 'ab'". Without parentheses, as in `ab+`, the `+` applies only to `b`.

    ```python
    import re

    text = "ababab aba abbb"
    pattern = r"(ab)+"
    print(re.findall(pattern, text))  # Output: ['ab', 'ab', 'ab']

    pattern2 = r"ab+"
    print(re.findall(pattern2, text))  # Output: ['ab', 'ab', 'ab', 'abbb']
    ```

2. **Capturing:** By default, parentheses also create a capturing group. The part of the string matched by the group is saved for later use, such as backreferences (accessed via `\1`, `\2`, etc, depending on the group number). The groups are numbered from left to right, and you can also give them explicit names using the `(?P<name>...)` syntax.

    ```python
    import re

    text = "12ab34 56ab78"
    pattern = r"(\d+)(ab)(\d+)"
    print(re.findall(pattern, text))  # Output: [('12', 'ab', '34'), ('56', 'ab', '78')]

    # using backreference
    replace_pattern = r"\1-\2-\3"
    print(re.sub(pattern, replace_pattern, text))  # Output: '12-ab-34 56-ab-78'
    ```

    Here, each pair of parentheses creates a capturing group, and the matches are returned as tuples.

    ```python
    import re

    # using named groups
    text = "12ab34"
    pattern = r"(?P<first>\d+)(?P<second>ab)(?P<third>\d+)"
    match = re.search(pattern, text)
    print(match.group('first'))  # Output: '12'
    print(match.group('second'))  # Output: 'ab'
    print(match.group('third'))  # Output: '34'
    ```

    This code creates three named groups: 'first', 'second', and 'third'. The `group` method is then used to retrieve the parts of the string that matched these groups.

If you want to use parentheses for grouping, but you don't want them to create capturing groups, you can use the `(?:...)` syntax.

```python
import re

text = "ababab ababab"
pattern = r"(?:ab)+"
print(re.findall(pattern, text))  # Output: ['ababab', 'ababab']
```

In this case, `(?:ab)+` matches one or more repetitions of 'ab', but the parentheses do not create a capturing group.







=========================================================================
Compiling vs Non Compiling
=========================================================================
You don't necessarily have to compile the regular expression pattern with `re.compile()` when using a pattern like `r'\bword\b'`. The `re.compile()` method is used to compile a regular expression pattern into a pattern object, which you can then use multiple times. This can be useful for efficiency when you're using the same pattern many times, but it's not required.

You can use the pattern directly in functions like `re.search()`, `re.match()`, `re.findall()`, etc., without compiling it first.

### Without Compiling:

```python
import re

pattern = r'\bword\b'
string = "This is a word in a sentence."

result = re.findall(pattern, string)
print(result)  # Output: ['word']
```

### With Compiling:

```python
import re

pattern = re.compile(r'\bword\b')
string = "This is a word in a sentence."

result = pattern.findall(string)
print(result)  # Output: ['word']
```

Both of these examples will have the same result. Compiling the pattern is optional and is more about code organization and potential performance benefits if the pattern is used repeatedly. If you're using the pattern just once, or if you prefer the more concise syntax, you can use the pattern directly without compiling it.








=========================================================================
Greedy vs Non-Greedy
=========================================================================
Regular expressions work based on pattern matching, and the way they match can be influenced by various factors such as the order of elements in the pattern, greedy versus non-greedy matching, and the use of groups.

### 1. Priority in Matching:
- **Order**: Regular expressions are evaluated from left to right, and the first matching pattern is usually returned. For example, in alternation patterns like `a|ab`, the pattern `a` will be matched first if the input string is `"ab"`.
- **Greedy vs Non-Greedy**: This plays a crucial role in how much text is matched.

### 2. Greedy Matching:
By default, quantifiers in regular expressions (like `*`, `+`, and `?`) are "greedy," meaning they will try to match as much text as possible.

Consider the pattern `".*"` applied to the string `"a<b>c<d>e"`. The `.*` will match everything from the first `a` to the last `e`, including the `<` and `>` characters.

Example:
```python
import re

pattern = r'<.*>'
string = "a<b>c<d>e"
match = re.search(pattern, string)

print(match.group())  # Output: '<b>c<d>'
```

### 3. Non-Greedy Matching:
You can make these quantifiers "non-greedy" by following them with a `?`. Non-greedy quantifiers will try to match as little text as possible.

Using the previous example, if you change the pattern to `"<.*?>"`, it will match only `"<b>"`.

Example:
```python
pattern = r'<.*?>'
match = re.search(pattern, string)

print(match.group())  # Output: '<b>'
```

The non-greedy pattern `.*?` tries to match as little as possible, so it stops at the first `>` it encounters, rather than the last one.

### Summary:
- Regular expressions prioritize patterns from left to right.
- Greedy quantifiers try to match as much as possible, whereas non-greedy quantifiers (with a trailing `?`) try to match as little as possible.
- Choosing between greedy and non-greedy depends on what you want to accomplish with your pattern. Non-greedy matching is often useful when you're working with nested structures, like HTML or XML tags.