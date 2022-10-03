import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, 
# собираются в список.
# Пример на Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Пример на Mac OS X и Linux:
source = ['/Users/swa/notes']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться 
# в основном каталоге резерва.
# Пример на Windows:
# target_dir = 'E:\\Backup'
# Пример на Mac OS X и Linux:
target_dir = '/Users/swa/backup'
# Подставьте тот путь, который вы будете использовать.

# Создайте целевой каталог, если он отсутствует
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # создать каталог

# 3. Файлы помещаются в zip-архив.
# 4. Текущий день - это имя подкаталога
# в главном каталоге.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время - это имя zip-архива.
now = time.strftime('%H%M%S')

# Принять комментарий от пользователя, чтобы
# создать имя zip-файла
comment = input('Введите комментарий --> ')
# Проверьте, был ли введен комментарий
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + 
        comment.replace(' ', '_') + '.zip'

# Создайте целевой каталог, если он отсутствует
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -r {0} {1}".format(target,
                                      ' '.join(source))

# Запускаем создание резервной копии
print('Zip команда:')
print(zip_command)
print('Выполняется:')
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
