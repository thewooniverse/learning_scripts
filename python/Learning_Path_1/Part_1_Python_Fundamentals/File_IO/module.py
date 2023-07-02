


# Open the file in read mode ('r')
with open('example.txt', 'r') as file:
    # Read the file content
    content = file.read()

# This is inside module.py
def print_text(txt):
    print(txt)

print_text(content)