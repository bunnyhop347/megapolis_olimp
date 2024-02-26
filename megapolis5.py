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
hash_table = {}  # Создание объекта хэш-таблицы, основываясь на классе словаря в python
added_tracks = []  # Создание списка, который предотвратит попадание уже использованных треков к другим артистам
streams, artist_name, track_name, date = read_csv_data(f)  # получаем данные из вышеописанной функции
for i in range(len(artist_name)):  # Проходимся по всем артистам в списке
    if artist_name[i] not in hash_table:  # Считаем кол-во треков в соответствии с условием
        if track_name[i] not in added_tracks:
            added_tracks.append(track_name[i])
            hash_table[artist_name[i]] = 1
    else:
        if track_name[i] not in added_tracks:
            added_tracks.append(track_name[i])
            hash_table[artist_name[i]] += 1


# Выводим первые 10 артистов из полученной таблицы
key = list(hash_table.keys())
value = list(hash_table.values())
for i in range(10):
    print(f"{key[i]} выпустил {str(value[i])} песен.")
