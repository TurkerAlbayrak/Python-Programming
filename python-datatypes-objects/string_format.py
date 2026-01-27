name = "Jonh"
surname = "Doe"
age = 36

print('My name is {} {}'.format(name, surname))
print('My name is {0} {1}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {n} {s}'.format(n=name, s=surname))
print('My name is {} {} and I am {} years old.'.format(name, surname, age))

result = 200 / 500

print(f'{result} is like this')
print('the result is {r:1.4}'.format(r=result)) # 1 boşluk bırak 4 e kadar al