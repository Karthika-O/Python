def factorial(n):
    "Factorial without using recursion"
    fact=1
    for i in range(n,0,-1):
        fact*=i;
    return fact
n=int(input('Enter any Number'))
print('Factorial of',n,' is ',factorial(n))
