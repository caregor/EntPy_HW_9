"""
    ---Task 2---
Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import csv
import math
import random
import json


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None


def quadratic_decorator(func):
    def wrapper(*args, **kwargs):
        filename = kwargs.get('filename')
        results = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    a, b, c = map(int, row)
                    roots = func(a, b, c)
                    results.append({
                        "input": row,
                        "output": roots
                    })
                    print(f"Корни для {row}: {roots}")
        except FileNotFoundError:
            print("Файл не найден.")

        # Сохраняем результаты в JSON файл
        with open("results.json", "w") as json_file:
            json.dump(results, json_file, indent=4)

    return wrapper


@quadratic_decorator
def solve_quadratic_equation_with_csv(a, b, c):
    return quadratic_equation(a, b, c)


def generate_csv_file(file_path, num_rows):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["a", "b", "c"])

        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


if __name__ == "__main__":
    file_path = "random_numbers.csv"
    num_rows = random.randint(100, 1000)

    generate_csv_file(file_path, num_rows)
    print(f"Сгенерирован CSV файл '{file_path}' с {num_rows} строками.")

    solve_quadratic_equation_with_csv(filename=file_path)
