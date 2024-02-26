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
user_input = input()  # Переменная, хранящая ввод пользователя
while user_input != '0':
    flag = True  # Флаг проверки, чтобы найденный трек выводился 1 раз, а если не нашелся - вывелась "ошибка"
    streams, artist_name, track_name, date = read_csv_data(f)  # получаем данные из вышеописанной функции
    for i in range(len(artist_name)):  # Ищем артиста
        if user_input == artist_name[i] and flag:  # Единожды выводим его песню или выводим "ошибку"
            flag = False
            print(f"У {artist_name[i]} найдена песня: {track_name[i]}")
    if flag:
        print("К сожалению, ничего не удалось найти")
    user_input = input()
