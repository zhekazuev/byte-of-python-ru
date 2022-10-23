def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

# прямая передача значений
print_max(3, 4)

x = 5
y = 7

# передача переменных в качестве аргументов
print_max(x, y)
