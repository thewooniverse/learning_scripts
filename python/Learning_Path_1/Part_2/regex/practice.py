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

websites:
https://chatgpt.com
http://openai.com
www.tally
down.com
foobar.vc
"""

email_pattern = r"\b[a-zA-Z0-9_.+%\-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,}\b"
# email_result = re.findall(email_pattern, test_text)
# print(email_result)


"""
It is important to divide out what exactly you are searching for in regex.
If I want to detect ALL kinds of numbers in a single regex pattern (can get messy)
OR if I want to have different pattern searches US numbers, intl. numbers etc... and organize them into a different list
"""
# try and write a generic phone number scraper
generic_phone_pattern = r"""
\b
\+?               # optional + sign
\d{1,3}?          # optional country code
\(\d{3}\)?        # optional US area code
[\-.\s]?          # optional divider
\d{3,4}           #
\b
"""


phone_number_pattern = r"\b(\+?([0-9]{1,3})?([.\-\s])?([0-9]{5,10}))\b"


# write a US only number scraper

# write a UK only number scraper

# compare / test results



phone_result = re.findall(phone_number_pattern, test_text)
print(phone_result)

