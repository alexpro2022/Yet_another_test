from typing import TypeAlias

Items: TypeAlias = list[int]
Strings: TypeAlias = list[str]


def unique_items(items: Items) -> Items:
    """
    1. Написать функцию, которая принимает на вход список целых чисел и
    возвращает новый список, содержащий только уникальные элементы из
    исходного списка.

    >>> unique_items([1, 1, 2, 2, 3, 3])
    [1, 2, 3]

    """
    return sorted(list(set(items)))


def eratosthenes_sieve(min: int = 0, max: int = 30) -> Items:
    """
    2. Написать функцию, которая принимает на вход два целых числа
    (минимум и максимум) и возвращает список всех простых чисел в
    заданном диапазоне.
    >>> eratosthenes_sieve()
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> eratosthenes_sieve(8)
    [11, 13, 17, 19, 23, 29]
    >>> eratosthenes_sieve(5, 50)
    [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    primes = [i for i in range(max + 1)]
    primes[1] = 0
    i = 2
    while i <= max:
        if primes[i] != 0:
            j = i + i
            while j <= max:
                primes[j] = 0
                j = j + i
        i += 1
    return [item for item in primes if item and item >= min]


def sorting_strings(strings: Strings, desc: bool = False) -> Strings:
    """
    4. Написать программу, которая сортирует список строк по длине,
    сначала по возрастанию, а затем по убыванию.

    >>> sorting_strings(['asdfgh', 'a', 'asdfghjkl', 'asd', 'as'])
    ['a', 'as', 'asd', 'asdfgh', 'asdfghjkl']

    >>> sorting_strings(['asdfgh', 'a', 'asdfghjkl', 'asd', 'as'], desc=True)
    ['asdfghjkl', 'asdfgh', 'asd', 'as', 'a']
    """
    return sorted(strings, key=lambda string: len(string), reverse=desc)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
