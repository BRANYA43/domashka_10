"""Написати функцію яка зрушить отриманий список на N елементів вправо або вліво, аргументи, що приймаються -
список і натуральне число(якщо негативне зрушуємо вліво, позитивне - вправо)."""

from random import randint


def shift_numbers(numbers: list, n: int) -> list:
    """Зрушує список на зандану кількість n, вліво або вправо залежно від знаку n. Повертає зрушений список."""
    nums = numbers.copy()
    return nums[n:] + nums[:n]


def main():
    _numbers = list(range(10))
    print(_numbers)
    print(shift_numbers(_numbers, 1))
    print(shift_numbers(_numbers, -5))


if __name__ == '__main__':
    main()
