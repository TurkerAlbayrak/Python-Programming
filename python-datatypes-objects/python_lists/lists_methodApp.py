names = ['John', 'Mike', 'Micheal', 'Carl']
years = [2000, 1999, 1998, 2003]

names.append('Cenk')
print(names)

names.insert(0, 'Sena')
print(names)

names.remove('Carl')
print(names)

value = names.index('Carl')
print(value)

isAliValueOfList = 'Ali' in names
print(isAliValueOfList)

names.reverse()
print(names)

names.sort()
print(names)

years.sort()
print(years)

str = "Chevrolet,Dacia"
newList = str.split(',')
print(newList)

maxValue = max(years)
minValue = min(years)

print(f'max: ', (maxValue), 'min: ', (minValue))

counter = years.count(1998)
print(counter)

years.clear()
print(years)

brand1 = input('Brand 1 : ')
brand2 = input('Brand 2 : ')
brand3 = input('Brand 3 : ')

brandsList = []

brandsList.append(brand1)
brandsList.append(brand2)
brandsList.append(brand3)
print(brandsList)