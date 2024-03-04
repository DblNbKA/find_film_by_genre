import tmdbsimple as tmdb

# Установка ключа API
tmdb.API_KEY = '00a12344e199220710a3a77050374a14'

# Список жанров фильмов для поиска
g = input("Введите жанр (или несколько жанров через запятую): ")

genres = g.split(", ")
print(genres)

# Поиск фильмов
for i in range(1, 2):
    genre_ids = []
    for genre_name in genres:
        # Получаем идентификаторы жанров по их названиям
        genre_search = tmdb.Genres().movie_list()['genres']
        for genre in genre_search:
            if genre['name'].lower() == genre_name.strip().lower():
                genre_ids.append(str(genre['id']))
                break
    
    # Формируем строку с идентификаторами жанров для запроса
    genre_ids_str = ','.join(genre_ids)

    # Поиск фильмов с заданными жанрами
    response = tmdb.Discover().movie(page=i, include_adult=False, with_genres=genre_ids_str)
    results = response['results']
    for result in results:
        title = result['title']
        title = title.replace("'", "")
        overview = result['overview']
        trailer_url = 'https://www.youtube.com/results?search_query=' + '+'.join(title.split()) + '+trailer'
        print('Название:', title)
        print('Описание:', overview)
        print('Ссылка на трейлер:', trailer_url)
        print('Ссылка на просмотр на Netflix:', 'https://www.netflix.com/search?q=' + '+'.join(title.split()))
        print('Ссылка на просмотр на Amazon Prime Video:', 'https://www.amazon.com/s?k=' + '+'.join(title.split()) + '&ref=nb_sb_noss_2')
        print('Ссылка на просмотр на Hulu:', 'https://www.hulu.com/search?q=' + '+'.join(title.split()))
        print('-------------------------------------')
