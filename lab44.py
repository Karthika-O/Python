def reverse(s):
    if not len(s):
        return s
    else:
        return s[-1]+reverse(s[:-1])
st=input('Enter a String ')
print(reverse(st))
