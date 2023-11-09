def revname(fname):
  print("In reverse order, the name is ")
  for word in fname[::-1]:
      print(word,end=" ")
n=input("Enter a name ").split()
revname(n)
