Sure, here are some exercises to get you started with using regular expressions in Python:

1. Email Addresses:
   Write a regular expression to find all the email addresses in a given string. Consider an email address to be a string that contains letters, numbers, periods, and/or underscores, followed by `@`, followed by more letters, periods, or underscores, ending with a domain suffix like `.com`, `.net`, `.org`, etc.

2. Web URLs:
   Write a regular expression to find all the web URLs in a given string. You can simplify the task by considering a URL to be any string that starts with `http://` or `https://`, followed by one or more characters, and ends when it encounters a whitespace character, or the end of the line.

3. Dates:
   Write a regular expression to find all dates in a string. You can limit yourself to the MM-DD-YYYY or the YYYY-MM-DD format for simplicity.

4. Phone numbers:
   Write a regular expression to find all phone numbers in a given string. Consider a phone number to be a string of digits that are separated by dashes, spaces, or nothing at all. You can further simplify by only looking for US phone numbers, which have the format 1-800-123-4567 or (800) 123-4567.

5. Ethereum addresses:
   Write a regular expression to find all Ethereum addresses in a string. An Ethereum address is a 42-character string that starts with `0x` followed by 40 hexadecimal characters.

Once you've written these regular expressions, test them out with the `re` module's `findall()` function on a variety of strings to see if they work as expected. 

Remember to import the `re` module with `import re` before you start.

If you get stuck, don't hesitate to ask for help. Regular expressions can be tricky at first, but with practice, you'll get the hang of it.