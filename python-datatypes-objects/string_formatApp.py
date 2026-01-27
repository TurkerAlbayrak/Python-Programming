website = "https://www.google.com"
course = "Lorem ipsum dolor sit amet."

courseLenght = len(course)
print(courseLenght)

websiteStringwww = website[8:11]
print(websiteStringwww)

websiteStringcom = website[19:] 
print(websiteStringcom)

x = website[0:15]
print(x)

y = website[-15:]
print(y)


reverse = course[::-1]
print(reverse)

response = 'Hello world'
response = response[0:6] + 'W' + response[-4:]
# response.replace('w',"W")

result = 'abc' * 3
print(result)


name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'
result = f'Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}'
print(result)