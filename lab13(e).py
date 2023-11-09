futureyear=int(input('Enter a future year : '))
print('Leaf years from 2023 to ',futureyear,' is ')
for year in range(2023,futureyear+1):
    if((year%4==0 and year%100!=0) or year%400==0):
        print(year)
