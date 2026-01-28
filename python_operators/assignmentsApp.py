x,y,z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

a = int(input('number 1 : '))
b = int(input('number 2 : '))

firstX = a * b
secondPlus = x + y + z

result = (firstX - secondPlus)
print(result)

kalansizbolme = y // x
print(kalansizbolme)

modthree = secondPlus % 3
print(modthree)

üsalmaislemi = y ** x
print(üsalmaislemi)

x, *y, z = numbers
print(z**3)

x, *y, z = numbers

counter = 0
for eleman in y:
    counter = counter + eleman
print(counter)

toplam = sum(y)
print(toplam)