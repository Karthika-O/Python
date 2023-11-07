numbers=input('Enter a list of numbers ')
numbers=list(map(int,numbers,split()))
for i in range(len(numbers)):
  if numbers[i]>100:
    numbers[i]='over'
print('Modified list:',numbers)
