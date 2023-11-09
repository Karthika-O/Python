original_list=input('Enter numbers ')
unique_list=[]
for item in original_list.split():
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
