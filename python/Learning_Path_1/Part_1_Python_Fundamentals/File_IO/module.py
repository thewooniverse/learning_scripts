


# Open the file in read mode ('r')
with open('example.txt', 'r') as file:
    # Read the file content
    content = file.read()

# This is inside module.py
def print_text(txt):
    print(txt)

# print_text(content)
## when you import it and this is not commented out, it will print (contet again)
