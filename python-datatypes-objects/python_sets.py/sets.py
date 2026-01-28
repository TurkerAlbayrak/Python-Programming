fruits = {'orange', 'apple', 'banana'}

#print(fruits[0]) # is return a error because the sets are not have index

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango', 'grape'])

myList = [1,2,3,45,6,7,12,321,2]
print(set(myList)) # aynı elemanlar tekrar gözülmez

fruits.remove('mango')
fruits.discard('apple')
fruits.pop()
fruits.clear()