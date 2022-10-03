import pickle

# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
# помещаем объект в файл
pickle.dump(shoplist, f)
f.close()

# уничтожаем переменную shoplist
del shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
# загружаем объект из файла
storedlist = pickle.load(f)
print(storedlist)
f.close()
