def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i]
    return total
def producto(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total
print(suma([1, 2, 3, 4]))
print(producto([1, 2, 3, 4]))


