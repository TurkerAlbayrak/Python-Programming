plakalar = {
    'kocaeli': 41,
    'istanbul': 34
}

print(plakalar['kocaeli'])
print(plakalar['istanbul'])

print(plakalar)

plakalar['ankara'] = 6,
plakalar['kocaeli'] = 'new value'

print(plakalar)

users = {

    'john': 10,
    'mike' : 11,

    'trevor': {
        'age': 20,
        'roles': ['user'],
        'email' : 'mail',
        'address' : 'Turkey'

    },

    'adam': {
        'age': 20,
        'roles': ['admin', 'user'],
        'email' : 'mail',
        'address' : 'Turkey'

    },

    'clem': {
        'age': 20,
        'email' : 'mail',
        'address' : 'Turkey'

    }
}

print(users['adam']['age'])
print(users['adam']['email'])
print(users['adam']['address'])
print(users['trevor']['roles'][0])