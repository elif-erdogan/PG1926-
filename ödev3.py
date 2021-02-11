x = input('birinci sayıyı girin: ')
y = input('ikinci sayıyı girin: ')
z = input('üçüncü sayıyı girin: ')
t = input('dördüncü sayıyı girin: ')
m = input('beşinci sayıyı girin: ')
n = input('altıncı sayıyı girin: ')
k = input('yedinci sayıyı girin: ')

x, n = n, x
print(x)
print(n)

y, k = k, y
print(y)
print(k)

z, n = n, z
print(z)
print(n)

t, k = k, t
print(t)
print(k)

m, n = n, m
print(m)
print(n)

n, k = k, n
print(n)
print(k)

print(x, y, z, t, m, n, k)
