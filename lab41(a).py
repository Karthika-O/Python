def sum_list(l):
    sum=0
    for i in l:
        sum+=i
    return sum
n=input('Enter the elements')
n=list(map(int,n.split(',')))
print('Sum = ',sum_list(n))
