"""
# pervaya versia
import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Users\\Charcharadon Astra\\Documents\\123"']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Users\\Charcharadon Astra\\Desktop\\бэкап'
# Подставьте тот путь, который вы будете использовать.
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
tojoin = '"'target+'"'
# ЭТИ КАВЫЧКИ ТОЖЕ ВСТАВИЛ ОНИ НУЖНЫ В ФИНАЛЬНОЙ КОМАНДЕ КАК И ПЕРВЫЕ
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(tojoin, ' '.join(source))
print(zip_command)
print("Yo")

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
"""

"""
# versia s bollee uporodachennimi archivami
import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Users\\Charcharadon Astra\\Documents\\123"']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Users\\Charcharadon Astra\\Desktop\\бэкап'
# Подставьте тот путь, который вы будете использовать.
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')
# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)
# Имя zip-файла
target = today + os.sep + now + '.zip'
tojoin = '"'+target+'"'
#ЭТИ КАВЫЧКИ НУЖНЫ, Я ВСТАВИЛ
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(tojoin, ' '.join(source))
print(zip_command)
print("Yo")

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
"""

# versia s bollee uporodachennimi archivami
import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Users\\Charcharadon Astra\\Documents\\123"']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Users\\Charcharadon Astra\\Desktop\\бэкап'
# Подставьте тот путь, который вы будете использовать.
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
             comment.replace(' ', '_') + '.zip'
# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)
# Имя zip-файла
tojoin = '"'+target+'"'
#ЭТИ КАВЫЧКИ НУЖНЫ, Я ВСТАВИЛ
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(tojoin, ' '.join(source))
print(zip_command)
print("Yo")

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')



