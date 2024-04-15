from typing import TypeAlias

Items: TypeAlias = list[int]


def unique_items(items: Items) -> Items:
    """
    1. Написать функцию, которая принимает на вход список целых чисел и
    возвращает новый список, содержащий только уникальные элементы из
    исходного списка.

    >>> unique_items([1, 1, 2, 2, 3, 3])
    [1, 2, 3]

    """
    return sorted(list(set(items)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
