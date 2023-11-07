my_list = input("Enter a list of items separated by spaces: ").split()
item = input("Enter the item you want to search for: ")
if item in my_list:
   count = my_list.count(item)
   print('The item',item,'appears',count,'times in the list.')
else:
   print('The item',item,'is not found in the list')
