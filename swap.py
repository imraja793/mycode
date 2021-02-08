a = 100
b = 50
c = a
a = b
b = c
print(a, b)

a = 50
b = 60
a = a + b
b = a - b
a = a - b
print(a, b)

a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

a = a*b
b = a/b
a = a/b
print(a, b)