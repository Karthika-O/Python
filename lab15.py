num=input('Enter numbers')
x=num.split(',')
even=[i for i in x if int(i)%2==0]
print('Even numbers in the given list are ',even)
