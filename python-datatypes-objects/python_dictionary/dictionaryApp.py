students = {}

studentNumber1 = input('Number 1 : ')
studentName1 = input('Name 1 : ')
studentSurname1 = input('Surname 1 : ')
studentPhone1 = input('Phone 1 : ')

# students[studentNumber1] = {
#     'ad' : studentName1,
#     'soyad' : studentSurname1,
#     'telefon' : studentPhone1
# }

students.update({
    studentNumber1: {
        'ad': studentName1,
        'soyad': studentSurname1,
        'telefon': studentPhone1
    }
})

print(students)