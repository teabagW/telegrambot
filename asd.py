a = 12345
b = 1
while num != 0:
    c = a % 10
    b = b * c
    a = a //10
print(b)