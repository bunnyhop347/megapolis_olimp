def read_csv_data(file):
    """Read_csv_data - функция, которая позволяет извлечь все нужные данные
    из таблицы и вернуть их в виде четырех списков"""
    streams = []  # список значений первого столбца
    artist_name = []  # список значений второго столбца
    track_name = []  # список значений третьего столбца
    date = []  # список значений четвертого столбца
    for line in file.readlines():
        temp = line.split(';')
        streams.append(temp[0])
        artist_name.append(temp[1])
        track_name.append(temp[2])
        date.append(temp[3].rstrip())
    return streams[1:], artist_name[1:], track_name[1:], date[1:]


f = open('songs.csv', encoding='utf-8')
russian_artists = []
foreign_artists = []
streams, artist_name, track_name, date = read_csv_data(f)  # получаем данные из вышеописанной функции
for i in range(len(artist_name)):  # Проходимся по всем артистам в списке
    flag = True
    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # Переменная со всеми буквами русского алфавита для проверки
    for ch in artist_name[i]:  # Осуществляем поиск русских символов в названии артистов
        if ch.lower() in rus_alph and flag:
            flag = False
            if artist_name[i] not in russian_artists:
                russian_artists.append(artist_name[i])
    if flag:
        if artist_name[i] not in foreign_artists:
            foreign_artists.append(artist_name[i])

print(f"Количество российских исполнителей: {len(russian_artists)}")
print(f"Количество иностранных исполнителей: {len(foreign_artists)}")

f_rus = open('russian_artists.txt', mode='w', encoding='utf-8')
f_for = open('foreign_artists.txt', mode='w', encoding='utf-8')
# Запись содержимого обоих списков в файлы
for el in russian_artists:
    f_rus.write(f'{el}\n')
for el in foreign_artists:
    f_for.write(f'{el}\n')
