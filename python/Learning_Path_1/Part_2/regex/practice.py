import re


test_text = """
emails
willynilly@gmail.com
willynilly@gmail.co.uk
()wb1234@5912mail.co.cn
}wb1}234@5912mail.ac.uk
shouldnotfindthisema()))})ilwb123?4@5912mail.ac.uk?
[email?@.com]
[email@email.com]

phone numbers
1(211)6012125
+14 583818231
+44 713588123


-- even for numbers, we should be detecting between mobile numbers and landline numbers as well
-- it is in fact probably better for various usecases to compile various patterns like UK landline, UK mobile etc etc...


websites:
https://chatgpt.com
http://openai.com
www.tally.co
down.com
foobar.vc
whatever.holdings
simpleton.group
"""

# eth address regex:
eth_address_pattern = r"0x[a-fA-F0-9]{40}"
eth_lookbehind_pattern = r"(?<=0x)[a-fA-F-0-9]{40}" # this does work but matched result excludes 0x so its not useful. good practice tho.




# email regex
email_pattern = re.compile(r"(([a-zA-Z0-9_.+%\-]+)@([A-Za-z0-9.-]+)(\.[a-zA-Z]{2,})?)")
result = email_pattern.findall(test_text)
# print(result)

# top level domain regex
website_pattern = r"(https://|http://|www)\.?(\w+)\.([\w]{2,24})([\w/]+)?"
result = re.findall(website_pattern, test_text)
# print(result)

# Depending on the exact format you want to match, 
# you might modify the pattern as follows to ensure there is a dot after the "www" and to be more specific about the path part:
website_pattern = r"(https://|http://|www\.)\w+\.[\w]{2,24}(/[\w/]+)?" # ChatGPT version

# Phone number regexes
uk_phone_pattern = r"(\+?44|0)([\d\s]{10,15})"

# GPT version
uk_phone_pattern = r"(\+44\s?|0)[1-9]\d{2}\s?\d{3}\s?\d{4}"
"""
Certainly! Let's break down the regex pattern `uk_mobile_pattern = r"(\+44\s?|0)[1-9]\d{2}\s?\d{3}\s?\d{4}"`:

- `(\+44\s?|0)`: This part is a capturing group with two options, and it defines the start of the phone number.
    - `\+44\s?`: This option matches the country code for the UK, "+44", followed by an optional space. The `?` means "0 or 1" of the preceding element, 
    so `\s?` matches either no space or a single space.
    - `|`: This is an OR operator, so the pattern matches either the preceding or the following part.
    - `0`: This option matches the leading zero that is common in UK phone numbers without an international dialing code.
    
- `[1-9]`: This part ensures that the first digit of the area code is between 1 and 9 (inclusive), meaning that it's not 0.

- `\d{2}`: This part matches two digits. `\d` is shorthand for `[0-9]`, so it matches any digit.

- `\s?`: This part matches an optional space. Again, the `?` means "0 or 1" of the preceding element.

- `\d{3}`: This part matches three more digits. Combined with the previous components, this forms the local area code part of the phone number.

- `\s?`: Another optional space.

- `\d{4}`: This part matches the last four digits of the phone number.

So, in summary, this pattern will match UK phone numbers that start with either "+44" (optionally followed by a space) or "0", 
followed by an area code of three digits (the first of which is not 0), and then the last four digits of the local number. 
Spaces between the various components are optional.

Some examples of phone numbers that would match this pattern:

- `+44 123 456 7890`
- `0123 456 7890`
- `+441234567890`
- `01234567890`
"""













"""
It is important to divide out what exactly you are searching for in regex.
If I want to detect ALL kinds of numbers in a single regex pattern (can get messy)
OR if I want to have different pattern searches US numbers, intl. numbers etc... and organize them into a different list
# """
# # try and write a generic phone number scraper
# generic_phone_pattern = r"""
# \b
# \+?               # optional + sign
# \d{1,3}?          # optional country code
# \(?\d{3}\)?        # optional US area code
# [\-.\s]?          # optional divider
# \d{3,4}           #
# \b
# """

# # write a US only number scraper

# # write a UK only number scraper

# # compare / test results



# phone_result = re.findall(phone_number_pattern, test_text)
# print(phone_result)

