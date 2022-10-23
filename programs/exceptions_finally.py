import sys
import time

f = None
try:
    f = open("poem.txt")
    # Наш обычный способ читать файлы
    while True: 
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Нажмите ctrl+c сейчас")
        # Пусть подождёт некоторое время
        time.sleep(2)
except IOError:
    print("Не удалось найти файл poem.txt")
except KeyboardInterrupt:
    print("!! Вы отменили чтение файла.")
finally:
    if f:
        f.close()
    print("(Очистка: Закрытие файла)")
