import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, 
# собираются в список.
# Пример на Windows:
# source = ['"C:\\My Documents"']
# Пример на Mac OS X и Linux:
source = ['/Users/swa/notes']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки. Мы могли бы также использовать
# необработанную строку, записав [r'C:\My Documents'].

# 2. Резервные копии должны храниться 
# в основном каталоге резерва.
# Пример на Windows:
# target_dir = 'E:\\Backup'
# Пример на Mac OS X и Linux:
target_dir = '/Users/swa/backup'
# Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# Создайте целевой каталог, если он отсутствует
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # создать каталог

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Запускаем создание резервной копии
print('Zip команда:')
print(zip_command)
print('Выполняется:')
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
