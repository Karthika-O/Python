def sum(n):
    if len(n)==1:
        return n[0]
    else:
        return n[0]+sum(n[1:])
l=input("Enter the elements ")
l=list(map(int,l.split()))
print("Sum Of Elements in the list is ",sum(l))
