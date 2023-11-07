def newstring(s):
    if s.startswith('Is') or s.startswith('is') :
        return s
    else:
        return 'Is' + s
s = input("Enter a string: ")
new = newstring(s)
print("New string:", new)
