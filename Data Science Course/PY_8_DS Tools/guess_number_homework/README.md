# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](#описание-проекта)  
[2. Какой кейс решаем?](#какой-кейс-решаем)  
[3. Краткая информация о данных](#краткая-информация-о-данных)  
[4. Этапы работы над проектом](#этапы-работы-над-проектом)  
[5. Результат](#результат)    
[6. Выводы](#выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

[к оглавлению](#оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений.

**Что практикуем**     
Учимся писать хороший код на Python, использовать Git и правильно оформлять проект на GitHub.


### Краткая информация о данных
....
  
[к оглавлению](#оглавление)


### Этапы работы над проектом  
1. V1: программа выбирала число случайным образом до тех пор, пока оно не было угадано. Данный способ не дал хорошего результата.
2. V2: программа устанавливала любое случайное число, а потом уменьшали или увеличивали его на 1. Данный способ дал улучшенный результат.
3. V3: программа использует метод половинного деления. Данный способ дал наилучшие результаты.

Более детально с эволюцией версий алгоритма можно ознакомиться с Jupyter ноутбуке [game.ipynb](https://github.com/podkovko/ds_course/blob/main/python_8/guess_number_homework/game.ipynb).

[к оглавлению](#оглавление)


### Результаты:  
Нам удалось написать алгоритм, который угадывает число от 1 до 100 в среднем за 4 попытки.

[к оглавлению](#оглавление)


### Выводы:  
....

[к оглавлению](#оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами