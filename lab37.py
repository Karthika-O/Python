def even(num):
     for item in num:
         if(item==237):
            break
         elif not item%2:
             print(item)
n=input("Enter a list of numbers ")
n=list(map(int,n.split()))
print("Event numbers in the list are as follows: ")
even(n)

         
