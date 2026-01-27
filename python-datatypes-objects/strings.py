name = "John"
surname = "Doe"
age = 36

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.'

print('My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.')
print(greeting)
length = len(greeting)

print(greeting[0])
print(greeting[2])
print(len(greeting))
print(greeting[len(greeting) - 1])
print(greeting[-1])
print(greeting[3:7])
print(greeting[3:])
print(greeting[:16])
print(greeting[2:40:2])