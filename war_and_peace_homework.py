# Импортируем библиотеку для выполнения HTTP-запросов в интернет
import requests

# Читаем текстовый файл по url-ссылке
data = requests.get("https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt").text

# Предобрабатываем текстовый файл
data = data.split('\n')
data.remove('')
data = data + ['[new chapter]']

# Выводим первые 100 слов из книги
print(data[:100])

# Превращаем список в множество, удаляя дублирующиеся слова
word_set = set(data)
# Удаляем из множества слово, символизирующее раздел между главами
word_set.discard('[new chapter]')
# Выводим результаты
print('Общее количество слов: {}'.format(len(data)))
print('Общее количество уникальных слов: {}'.format(len(word_set)))

# Инициализируем пустой словарь
word_counts = {}
# Инициализируем количество глав
count_chapter = 0
# Создаем цикл по всем словам из списка слов
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, то увеличиваем количество глав на 1
        count_chapter += 1
        # Переходим на новую итерацию цикла
        continue
    # Проверяем, что текущего слова еще нет в словаре слов
    if word not in word_counts:
        # Если условие выполняется, инициализируем новый ключ 1
        word_counts[word] = 1
    else:
        # В противном случае, увеличиваем количество слов на 1
        word_counts[word] += 1

# Выводим количество глав
print('Количество глав: {}'.format(count_chapter))

# Создаем цикл по ключам и их порядковым номерам полученного словаря
for i, key in enumerate(word_counts):
    # Выводим только первые 10 слов
    if i == 10:
        break
    print(key, word_counts[key])
    
    # Инициализируем общий список, в котором будем хранить списки слов в каждой главе
chapter_data = []
# Инициализируем список слов, в котором будет хранить слова одной главы
chapter_words = []

# Создаем цикл по всем словам из списка
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, добавляем список со словами из главы в общий список
        chapter_data.append(chapter_words)
        # Обновляем (перезаписываем) список со словами из текущей главы
        chapter_words = []
    else:
        # В противном случае, добавляем текущее слово в список со словами из главы
        chapter_words.append(word)

# Проверяем, что у нас получилось столько же списков, сколько глав в произведении
print('Вложенный список содержит {} внутренних списка'.format(len(chapter_data)))
# Выведем первые 100 слов 0-ой главы
print(chapter_data[0][:100])

chapter_data[15][100]

# Инициализируем список, в котором будем хранить словари
chapter_words_count = []

# Создаем цикл по элементам внешнего списка со словами
for chapter_words in chapter_data:
    # Инициализируем пустой словарь, куда будем добавлять результаты
    temp = {}
    # Создаем цикл по элементам внутреннего списка
    for word in chapter_words:
        # Проверяем, что текущего слова еще нет в словаре
        if word not in temp:
            # Если условие выполняется, добавляем ключ в словарь
            temp[word] = 1
        else:
            # В противном случае, увеличиваем количество влождений слова в главу
            temp[word] += 1
    # Добавляем получившийся словарь в список
    chapter_words_count.append(temp)

# Выводим результат
print(chapter_words_count)

# Создаем цикл по ключам словаря - спискам слов и их порядковым номерам
for chapter_number, chapter_dict in enumerate(chapter_words_count):
    # Выводим только первые 5 глав
    if chapter_number == 5:
        break
    # Выводим номер главы
    print('-' * 40)
    print('Chapter: {}'.format(chapter_number))
    print('-' * 40)
    # Создаем цикл по ключам - словам и их порядковым номерам
    for j, word in enumerate(chapter_dict):
        # Выводим первые 10 слов из главы
        if j == 10:
            break
        print(word, chapter_dict[word])
        
target_word = 'гостья'
target_chapter = 15

# Создаём список, где будут храниться словари по каждой главе и словам в этой главе с соответствующими значениями Term Frequency.
tf_data = []
for i, chapter_number in enumerate(chapter_data):
    chapter = i
    temp = {}
    for word in chapter_number:
        n_chapter = len(chapter_data[chapter])
        n_word_chapter = chapter_words_count[chapter][word]
        tf = n_word_chapter / n_chapter
        temp[word] = tf
    tf_data.append(temp)

# Определяем значение Term Frequency для наших target_word и target_chapter и выводим его в терминал.
# Округляем значение tf до 6 символов после точки.
target_tf_value = tf_data[target_chapter][target_word]
print('Частота употребления (Term Frequency) слова "{}" в {} главе = {:6f}'.format(target_word, target_chapter, target_tf_value))

# Крадём и адаптируем код из предыдущей ячейки с кодом для проверки, потому что можем :)
for chapter_number, tf_dict in enumerate(tf_data):
    # Выводим только первые 5 глав
    if chapter_number == 5:
        break
    # Выводим номер главы
    print('')
    print('-' * 40)
    print('Chapter: {}'.format(chapter_number))
    print('-' * 40)
    # Создаем цикл по ключам - словам и их порядковым номерам
    for j, word_tf in enumerate(tf_dict):
        # Выводим первые 10 слов из главы
        if j == 10:
            break
        print(word_tf, round(tf_dict[word_tf], 6))
        
target_word = 'человек'

# Создаём словарь, где будут храниться все слова в книге с соответствующими значениями Document Frequency.
df_data = {}

# Создаём цикл по каждой главе
# Из списка слов в каждой главе создаём множество слов.
for chapter_words in chapter_data:
    chapter_set = set(chapter_words)
    # Делаем цикл по каждому уникальному слову в главе
    # Если слова нет в словаре df_data - добавляем его
    # Если слово есть в словаре df_data - увеличиваем счётчик на один
    for word in chapter_set:
        if word not in df_data:
            df_data[word] = 1
        else:
            df_data[word] += 1

# С помощью цикла переписываем значение каждого ключа (каждого слова в книге)
# С количества глав со словом на его показатель Document Frequency
for book_word in word_set:
    df_data[book_word] /= count_chapter

# Обращаемся к словарю df_data по ключу target_word
# Получаем значение DF нашего target_word
target_df_value = df_data[target_word]

# Выводим значение Document Frequency в терминал
print('Document Frequency слова "{}" в книге = {:6f}'.format(target_word, target_df_value))

# Импортируем функцию log из модуля math:
from math import log
print(log(18))

target_word = 'анна'
target_chapter = 4

# Создаём список, где будут храниться словари по каждой главе и словам в этой главе с соответствующими значениями tf-idf
tf_idf_data = []
# Cоздаём цикл for по списку chapter_data
# Используем enumerate для получения индексов глав
# Создаём пустой словарь temp
for i, chapter_number in enumerate(chapter_data):
    chapter = i
    temp = {}
    # Задаём цикл for по каждому слову в главе chapter
    for word in chapter_number:
        # Обращаемся к словарю tf_data по индексу нашей главы и нашего слова.
        tf = tf_data[i][word]
        # Обращаемся к словарю df_data по нашему слову.
        df = df_data[word]
        # Вычисляем показатель idf для нашего слова по формуле
        idf = 1 / df
        # Вычисляем показатель tf_idf для нашего слова по формуле
        tf_idf = tf * log(idf)
        # Добавляем значение tf_idf к ключу word в наш словарь по главе.
        temp[word] = tf_idf
    # Добавляем ключ по слову и его значение в наш список словарей tf_idf_data
    tf_idf_data.append(temp)

# Определяем значение tf-idf для наших target_word и target_chapter
target_tf_idf = tf_idf_data[target_chapter][target_word]

# Выводим значение в терминал, округляя значение tf-idf до 6 символов после точки.
print('Показатель tf-idf слова "{}" в {} главе = {:6f}'.format(target_word, target_chapter, target_tf_idf))

target_chapter = 3

# Создаём цикл по каждому словарю tf_idf_data
for chapter_number, chapter_idf in enumerate(tf_idf_data):
    # Сортируем словарь по значениям от самого большого к самому маленькому
    sorted_chapter_idf = dict(sorted(chapter_idf.items(), key=lambda item: item[1], reverse=True))

    # Заменяем оригинальный словарь на отсортированный
    tf_idf_data[chapter_number] = sorted_chapter_idf

# Выводим три наиболее значимых слова в заданной главе в терминал.
print('3 наиболее значимые слова в главе {} это:'.format(target_chapter))
print(list(tf_idf_data[target_chapter].keys())[:3])

# Часть ниже вывел 3 значимых слова по каждой главе
# В задании такого условия не было - просто хотел посмотреть результат по всем главам :)
for i, tf_idf_dict in enumerate(tf_idf_data):
    if i == 50:
        break
    print('')
    print('-' * 40)
    print('Chapter: {}'.format(i))
    print('-' * 40)
    for j, word_tf_idf in enumerate(tf_idf_dict):
        if j == 3:
            break
        print(word_tf_idf, round(tf_idf_dict[word_tf_idf], 6))