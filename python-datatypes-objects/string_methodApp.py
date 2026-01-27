text = ' Hello World '
text = text.strip()
text = text.lstrip() # soldan silme
text = text.rstrip() #  sağdan silme
print(text)

website = "http://www.sadikturan.com"
website = website[7::]
print(website)
# result = website.lstrip('/:pth')
# result1 = website.strip('w.comhttp://')

course = "Python Programming"
course = course.lower()
print(course)

result = website.count('a') #kaç tane a var
print(result)

response = website.startswith('www')
response2 = website.endswith('com')
print(response, response2)

findwebsite = website.find('.com')
print(findwebsite)

alphabetic = website.isalpha()
print(alphabetic)
digit = website.isdigit()
print(digit)

newText = 'Contents'
newText = newText.center(50, "*")
print(newText)

course = course.replace(" ", "-")
print(course)

textNew = "Hello World"
textNew = textNew.replace("World", "There")
print(textNew)

course = course.split('-') # - ile ayır 
print(course)

new = ' '.join(course) # boşluk karakteri ile birleştir
print(new)