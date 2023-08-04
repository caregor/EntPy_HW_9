"""
    ---Task1_3---
    Задание No6
Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.
"""

import random
import csv
from functools import wraps


def save_to_csv(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        with open("results.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                header = ["limit", "attempts"]
                writer.writerow(header)
            writer.writerow([*args, *kwargs.values(), result])

        return result

    return wrapper


def validate_parameters(func):
    @wraps(func)
    def wrapper(upper_bound, max_attempts):
        if not (1 <= upper_bound <= 100):
            upper_bound = random.randint(1, 100)
            print("Некорректное значение верхней границы. Генерируется случайное число от 1 до 100.")

        if not (1 <= max_attempts <= 10):
            max_attempts = random.randint(1, 10)
            print("Некорректное значение числа попыток. Генерируется случайное число от 1 до 10.")

        func(upper_bound, max_attempts)

    return wrapper


def multiple_runs(num_runs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for run in range(num_runs):
                print(f"Игра #{run + 1}")
                result = func(*args, **kwargs)
                print(f"Результат игры: {result}")
                if run + 1 != num_runs:
                    choice = input("Продолжить игру? (да/нет): ")
                    if choice.lower() != "да":
                        break

        return wrapper

    return decorator


@save_to_csv
@validate_parameters
@multiple_runs(num_runs=3)
def main(upper_bound, max_attempts):
    secret_number = random.randint(1, upper_bound)
    print(f"Компьютер загадал число от 1 до {upper_bound}. Попробуйте угадать.")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Попытка {attempt}. Введите вашу догадку: "))

        if guess < secret_number:
            print("Загаданное число больше вашей догадки.")
        elif guess > secret_number:
            print("Загаданное число меньше вашей догадки.")
        else:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
            return "Выиграл"

    return "Проиграл"


if __name__ == "__main__":
    upper_bound = int(input("Введите верхнюю границу для загадываемого числа: "))
    max_attempts = int(input("Введите число попыток: "))
    main(upper_bound, max_attempts)
