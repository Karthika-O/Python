s=input("Enter a list of strings")
l=list(filter(lambda x:len(x)>5,s.split()))
print(l)
