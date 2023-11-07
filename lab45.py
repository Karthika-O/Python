n=int(input('Enter a number'))
def sum(n):
    if n<10:
        return n
    else:
        return n%10+sum(n//10)
print('Sum of Digits of ',n,' is ',sum(n))
sum=0
while n>0:
    d=n%10
    sum+=d
    n//=10
print('Sum of Digits using recursion is ',sum)