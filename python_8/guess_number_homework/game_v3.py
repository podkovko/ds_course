"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Угадываем число методом половинного деления.
    В зависимости от знака (> или <) каждого цикла while - повышаем или 
    понижаем нижний или высший предел и целочисленно делим его на 2.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    np.random.seed(5)
    
    count = 0
    low = 1
    high = 101
    predict = (low + high) // 2

    while number != predict:
        count += 1
        if number > predict:
            low = predict + 1
        elif number < predict:
            high = predict - 1
        predict = (low + high) // 2
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает 
       наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
