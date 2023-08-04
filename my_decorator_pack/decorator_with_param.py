"""
    ---Task 1_1---
    Задание No4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.
"""
from typing import Callable


def limited_runs_decorator(runs):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(runs):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator