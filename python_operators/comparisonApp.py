a = int(input('a: '))
b = int(input('b: '))

result = (a>b)
print(f'{a} {b} den büyük mü?: {result}')

vize1 = int(input('vize 1: '))
vize2 = int(input('vize 2: '))
finalNot = int(input('final: '))

vize60 = vize1 * 0.60
vize60_= vize2 * 0.60

final40 = finalNot * 0.40
result = (vize60 + vize60_ + final40) / 3
print(result)

if result > 50:
    print('geçti')
else:
    print('kaldı')


sayi = int(input('Sayi : '))
if sayi % 2 == 0:
    print('çift')
else:
    print('tek')

sayi1 = int(input('Sayi 1: '))
if sayi1 < 0:
    print('neg')
elif sayi1 == 0:
    print('0')
else:
    print('poz')

email = 'mail'
passw = 123

gire = input('Ema:')
girp = input('Pass: ')

if gire == email and girp == passw:
    print('both of them true')
else:
    print('please check')