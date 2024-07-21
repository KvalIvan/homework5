immutable_var = (17, 'Текст', True)
print(immutable_var)
# Если мы захотим изменить элемент кортежа то у нас появится ошибка:
# Что кортеж не поддерживает обращение по элементам

mutable_list = [1, 2, 'a', 'b']
mutable_list.remove(1)
mutable_list.append('fish')
mutable_list[1] = 3
print(mutable_list)