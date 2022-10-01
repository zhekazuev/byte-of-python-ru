import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
