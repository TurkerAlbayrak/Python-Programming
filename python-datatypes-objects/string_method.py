message = "Hello There. My name is Elliot Alderson"

message = message.upper() # hepsi büyük
print(message)
message = message.lower() # hepsi küçük
print(message)
message = message.title() # Baş harfler büyük
print(message)
message = message.capitalize() # Sadece baş harf büyük
print(message)

message = message.strip() # başından ve sonundan eklenen şeyleri çıkartır
print(message)

message = message.split() # boşluk karakterlerinden ayırır ve hepsini bir dizi elemanı yapar. içerisine '.' koyarsak noktadan ayırır
print(message)
print(message[0]) #Hello
message = ''.join(message) # split ayırırsan geri birleştirir

index = message.find('Hello') # pozitif bir sayı verir
print(index)

isFound = message.startswith('H')
print(isFound) # True cümle H ile başlıyor
isFound = message.endswith('n')

message = message.replace('Hello', "Hi") # Helloyu Hi ile değiştiriz
print(message)

message = message.center(50) # 50 karakter boşluk bırakır sağ ve soldan