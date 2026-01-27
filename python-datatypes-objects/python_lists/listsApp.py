carBrandsList = ["Bmw", "Mercedes", "Opel", "Mazda"]
carBrandsListLength = len(carBrandsList)
print(carBrandsListLength) #4

carBrandsListFirstValue = carBrandsList[0]
carBrandsListLastValue = carBrandsList[carBrandsListLength - 1]
print(carBrandsListFirstValue) # Bmw
print(carBrandsListLastValue) # Mazda


carBrandsList[carBrandsListLength - 1] = "Toyota"
print(carBrandsList)

isMercedesOnList = carBrandsList.count('Mercedes')
print(isMercedesOnList) # 1

carBrandsList2 = ' '.join(carBrandsList)
print(carBrandsList2)

isMercedesOnListCheck = carBrandsList2.find("Mercedes")
print(isMercedesOnListCheck)

for brand in carBrandsList:
    if brand == "Mercedes":
        print("Mercedes is exists.")
        break
    else:
        print('Mercedes is not exists.')

value = carBrandsList[-2]
print(value) # Opel


last_value_of_list = carBrandsListLength - 1 # Mazda
last_second_value_of_list = carBrandsListLength - 2 # Opel

the3elementsOfList = carBrandsList[:last_value_of_list]
the3elementsOfList = carBrandsList[:3]
the3elementsOfList = carBrandsList[0:3]
the3elementsOfList = carBrandsList[-4:-1]
print(the3elementsOfList)

carBrandsList[last_second_value_of_list] = "Toyota"
carBrandsList[last_value_of_list] = "Renault"
print(carBrandsList)


carBrandsList3 = ["Bmw", "Mercedes", "Opel", "Mazda"]
carBrandsList3.append("Audi")
carBrandsList3.append("Nissan")
print(carBrandsList3)

carBrandsList4 = ["Bmw", "Mercedes", "Opel", "Mazda"]
carBrandsList4.pop()
print(carBrandsList4)

carBrandsList5 = ["Bmw", "Mercedes", "Opel", "Mazda"]
length = len(carBrandsList5)
last_value = length - 1
carBrandsList5.remove(carBrandsList5[last_value])
print(carBrandsList5)

carBrandsList6 = ["Bmw", "Mercedes", "Opel", "Mazda"]
carBrandsList6.remove("Mazda")
print(carBrandsList6)

carBrandsList7 = ["Bmw", "Mercedes", "Opel", "Mazda"]
carBrandsList7New = ' '.join(carBrandsList7)
carBrandsList7New = carBrandsList7New[::-1]
carBrandsList7New = carBrandsList7New.split()
print(carBrandsList7New) # ['adzaM', 'lepO', 'sedecreM', 'wmB']

carBrandsList8 = ["Bmw", "Mercedes", "Opel", "Mazda"]

counter = len(carBrandsList8) - 1 #3
newlist = []
for brand in carBrandsList8:
    value = carBrandsList8[counter]
    newlist.append(value)
    counter = counter - 1
    if counter == -1:
        break
    else: 
        continue
print(newlist)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["John", "Doe", 2000, [80,80,70]]
studentC = ["Domates", "Biber", 2020, [50,60,80]]

allStudents = [studentA, studentB, studentC]
print(allStudents[::])
