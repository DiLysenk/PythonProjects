def filter_by_key(d, filtering):
    """
    Фильтрация по предикату ключа

    Написать функцию, которая на вход получает словарь и функцию-предикат от одного
    аргументь. Функция должна возвращать новый словарь с парами ключ-значения
    из входного словаря, но только в том случае, если ключ у этой пары удовлетворяет
    функции-предикату (то есть, когда filtering(key) == True)

    Пример: если filtering=lambda x: isinstance(x, int) and x % 2 == 0,
    тогда в словаре должны остаться только пары с ключами-чётными числами

    >>> filtering = lambda x: isinstance(x, int) and x % 2 0
    >>> filter_by_key({'a': 2, 5: 3, 't': 5, 10: 'Yes', 20: True}, filtering)
    {10: 'Yes', 20: 'True'}
    """
    if filtering == True:
        d1 = {}
        for key, value in d.items():
            if isinstance(key, int) and key % 2 == 0:
                d1[key] = value
        return d1
    else:
        return d