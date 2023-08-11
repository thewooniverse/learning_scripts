Of course! Here are some regex exercises to practice with:

1. **URL Extractor**:
   Extract all URLs from a given text. Assume that the URLs start with `http://` or `https://` and end with `.com`, `.org`, `.net`, etc.
   - Sample input: "Visit my blog at http://myblog.com or check out the website https://coolwebsite.net!"
   - Expected output: ['http://myblog.com', 'https://coolwebsite.net']

2. **Match Dates**:
   Match all the dates in the format `dd/mm/yyyy` or `dd-mm-yyyy`.
   - Sample input: "My birthday is on 05/08/1990 and my sister's birthday is on 15-07-1985."
   - Expected output: ['05/08/1990', '15-07-1985']

3. **Currency Extractor**:
   Extract all the amounts that are prefixed with the `$` sign and optionally followed by a comma separator.
   - Sample input: "The laptop costs $1,299.99 while the phone is just $799."
   - Expected output: ['$1,299.99', '$799']

4. **Username Extractor from an Email**:
   Extract just the username from a list of email addresses.
   - Sample input: "The emails are: john_doe@gmail.com, alice.bob@mywebsite.org"
   - Expected output: ['john_doe', 'alice.bob']

5. **HTML Tag Remover**:
   Write a regex pattern to identify and remove all HTML tags from a text. 
   - Sample input: "<div>Hello World</div><p>This is a paragraph.</p>"
   - Expected output: "Hello WorldThis is a paragraph."

6. **Match IP Addresses**:
   Extract valid IPv4 addresses from a given text.
   - Sample input: "The valid IPs are: 192.168.1.1, 10.0.0.1 and this is not an IP: 300.300.300.300."
   - Expected output: ['192.168.1.1', '10.0.0.1']

7. **Capture Serial Numbers**:
   Capture serial numbers of the format: `XXX-XXX-XXX` where X is an uppercase alphabetic character.
   - Sample input: "These are the valid serials: ABC-DEF-GHI, XYZ-XYZ-XYZ and this is invalid: abc-def-ghi."
   - Expected output: ['ABC-DEF-GHI', 'XYZ-XYZ-XYZ']

Try to create regex patterns for each of these exercises. They'll help you get familiar with different regex techniques and broaden your understanding of regular expressions.






==== Feedback to solution ====

Let's review each of the provided solutions:

1. **URL Extractor**:
   - Your regex works, but it captures the URLs in three parts. Instead of using `findall`, you might consider using a `finditer` loop to get the entire matched URL. 
   
   ```python
   urls = [match.group(0) for match in url_pattern.finditer(url_text)]
   print(urls)
   ```
   
2. **Date Extractor**:
   - The regex is working correctly, but again, you get the day, month, and year separately because of multiple capture groups. Using the technique suggested above for the URL extractor, you can solve this problem.

3. **Currency Extractor**:
   - This regex works for the provided example. The only thing I'd note is that it's structured to capture separate parts of the currency, so you're combining them at the end. A simpler approach might be to construct the regex to match the entire amount at once, but your method works and gives you more control over individual parts if needed.

4. **Username Extractor from an Email**:
   - This works well. It's simple and straightforward.

5. **HTML Tag Remover**:
   - The `findall` you used is just for demonstration since you've shown the found tags and then the replaced text. The tags themselves are matched correctly.
   - For better removal of all types of tags, consider this pattern: `<[^>]+>` to match everything inside angle brackets.

6. **Match IP Addresses**:
   - Both patterns provided will work, and you correctly used the second one. The results show the components of each IP address separately due to capture groups. Again, the `finditer` approach I mentioned would help you grab each complete IP address.

7. **Capture Serial Numbers**:
   - This works correctly. Your pattern matches uppercase serial numbers in the provided format.

Overall, your solutions demonstrate a good understanding of regex. Your main area of improvement would be understanding the nuances of capture groups and how they affect the output of methods like `findall`. Remember, each pair of parentheses is a capture group, and in `findall`, if there are capture groups in the pattern, the method returns a list of tuples containing the captured groups. If you just want the full matches, you might want to avoid using capture groups or utilize other methods like `finditer`.