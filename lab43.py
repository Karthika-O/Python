n=int(input("Enter Value of N "))
sum=0
for i in range(n):
    sum=sum+i
print('Sum of first',n,'whole numbers is',sum)

def sum_num(n):
    "Using Recursion"
    if n==0:return 0
    else:
        return n+sum_num(n-1)

print('Using recursion SUM = ',sum_num(n-1))

