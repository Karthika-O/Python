string=input('Enter a String')
new=string[::-1]
print('Reverse of the given string is ',new)
if string==new:
    print(string," is Palindrome")
else:
 print("Not a palindrome")
