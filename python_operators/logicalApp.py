sayi1 = int(input("Sayi1 : "))
control = (sayi1>0) and (sayi1<100)
print(f'Sayi1 kontrol durumu 0 ile 100 arasında mı?: {control}')

girilenSayi = int(input('Sayı: '))
controlCift2 = girilenSayi % 2 == 0
controlTek2 = girilenSayi % 2 == 1

print(f'Girilen sayı tek mi {controlTek2}, çift mi {controlCift2}.')


email = 'email'
passw = 'passw'

userEmail = input('Email: ')
userPassw = input('Password: ')

controlAuth = (userEmail == email) and (userPassw == passw)

print(f'Giriş yapabilir mi {controlAuth}')

a = int(input('Sayi1 : '))
b = int(input('Sayi2 : '))
c = int(input('Sayi3 : '))

controlA = (a>b) and (a>c)
controlB = (b>a) and (b>c)
controlC = (c>b) and (c>a)

print(f'A en büyük mü {controlA}, B en büyük mü {controlB}, C en büyük mü {controlC}')

kilo = float(input('Kilo: '))
boy = float(input('Boy: ')),

formül = (kilo / (boy**2))
print(formül)