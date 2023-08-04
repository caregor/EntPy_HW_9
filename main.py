from my_decorator_pack import limited_runs_decorator
from random import randint


@limited_runs_decorator(4)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10


# Декоратор для сохранения параметров
def log_parameters(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper


# Декоратор для контроля значений
def validate_input(func):
    def wrapper(*args, **kwargs):
        guess = int(input(f"Попытка {kwargs['attempt']}: Введите вашу догадку: "))
        if LOWER_LIMIT <= guess <= UPPER_LIMIT:
            kwargs['guess'] = guess
            result = func(*args, **kwargs)
        else:
            print("Неверное значение! Попробуйте ещё раз.")
            result = wrapper(*args, **kwargs)
        return result

    return wrapper


@log_parameters
@validate_input
@limited_runs_decorator(3)
def guess_number_game(attempt, guess):
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print("Угадайте число от 0 до 1000. У вас 10 попыток.")

    for _ in range(1, MAX_ATTEMPTS + 1):
        if guess == num:
            print("Поздравляю! Вы угадали число!")
            break
        elif guess < num:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

        if attempt == MAX_ATTEMPTS:
            print("У вас закончились попытки. Загаданное число:", num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #task1_1
    print_hi('PyCharm')

    guess_number_game(3)
