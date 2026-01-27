text = "John Doe"
textSplit = text.split()
print(textSplit)
print(type(textSplit))

textWith = " ".join(textSplit)
print(textWith)
print(type(textWith))

liste = [1,2,3,"John",True,12.3]
print(liste)
print(liste[0])

list1 = ['one','two','three']
list2 = ['four', 'five', 6]

sumofList = list1 + list2
print(sumofList)

print(len(textSplit))

userA = ["John", 10]
userB = ["Johny", 15]

users = [userA, userB]
print(users)
print(users[1])
a = users[1]
print(a[0])
print(users[1][0])