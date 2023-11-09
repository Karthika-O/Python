l=input("Enter a list of integers ")
l=list(map(lambda x:x+x*0.1 if int(x)>1000 else x+x*0.5,l))
print(l)
