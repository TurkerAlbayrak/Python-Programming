# x = 5
# y = 10
# z = 20

# x, y, z = 5, 16, 20

# x, y = y, x
# x += 5          # x = x + 5
# x -= 5          # x = x - 5
# x *= 5          # x = x * 5
# x /= 5          # x = x / 5
# x %= 5          # x = x % 5
# y //= 5         # y = y // 5
# y **= z         # y = y ** z


values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values #x i ve yi ata geri kalan elemanları z ye ata liste olarak

print(x, y, z)
print(x, y, z[1]) # z = [3,4,5]