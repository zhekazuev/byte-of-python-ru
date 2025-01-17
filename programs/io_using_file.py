poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python!
'''

# открываем для записи (writing)
f = open('poem.txt', 'w')
# записываем текст в файл
f.write(poem)
# закрываем файл
f.close()

# если не указан режим, по умолчанию подразумевается
# режим чтения ('r'eading)
f = open('poem.txt')

while True:
    line = f.readline()
    # Нулевая длина обозначает конец файла (EOF)
    if len(line) == 0:
        break
    # Строка `line` уже имеет новую строку
    # в конце каждой строки
    # так как он читает из файла.
    print(line, end='')
# закрываем файл
f.close()
