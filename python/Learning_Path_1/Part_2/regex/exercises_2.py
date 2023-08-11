import re

#URL Extractor
url_text = "Visit my blog at http://myblog.com or check out the website https://coolwebsite.net!"
url_pattern = re.compile(r"(http[s]?://|www.)([\w_-]+).([\w.]{2,14})")
result = re.finditer(url_pattern, url_text)
for group in result:
    print(group.group())

#DATE extractor
date_text = "My birthday is on 05/08/1990 and my sister's birthday is on 15-07-1985."
date_pattern = re.compile(r"([3][0-1]|[0-2][0-9])[\s/.-]([1][0-2]|[0][0-9]|)[\s/.-]([\d]{1,4})")
print(re.findall(date_pattern, date_text))


#CURRENCY extractor
currency_text = "The laptop costs $1,299.99 while the phone is just $799."
currency_pattern = re.compile(r'([\$\£])([1-9][0-9]{0,2})(\,[0-9]{3})*(\.[0-9]{0,})?')
matches = re.findall(currency_pattern, currency_text)
for match in matches:
    print(''.join(match))

#USERNAME extractor from email
username_text = "The emails are: john_doe@gmail.com, alice.bob@mywebsite.org"
username_pattern = re.compile(r'([\w._-]+(?=@))')
print(re.findall(username_pattern, username_text))

#HTML tag remover
html_text = "<div>Hello World</div><p>This is a paragraph.</p>"
html_pattern = re.compile(r'<\w+>|<\/\w+>')
print(re.findall(html_pattern, html_text))
result = re.sub(html_pattern, "", html_text)
print(result)

#MATCH IP address
ip_text = "The valid IPs are: 192.168.1.1, 10.0.0.1 and this is not an IP: 300.300.300.300."
# ip_pattern = re.compile(r'\b(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d\d?)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d\d?)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d\d?)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d\d?)\b')
ip_pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
print(re.findall(ip_pattern,ip_text))

#SERIALNUM 
sn_text = "These are the valid serials: ABC-DEF-GHI, XYZ-XYZ-XYZ and this is invalid: abc-def-ghi."
sn_pattern = re.compile(r'[A-Z]{3}-[A-Z]{3}-[A-Z]{3}')
print(re.findall(sn_pattern, sn_text))
