def countstrings(s):
    count=0
    for item in s.split():
        if len(item)>1 and item[0]==item[-1]:
            count+=1
    return count
s=input("Entr a Collection  of string ")
print("Number of strings with first and last characters are same: ",countstrings(s))
