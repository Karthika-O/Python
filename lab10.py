li=input('Enter a list of colors :')
colors=li.split(',')
print('List of colors are : ',colors)
print('Alternate colours :')
for i in range (0,len(colors),2):
 print(colors[i])
