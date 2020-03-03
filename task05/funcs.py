#!/usr/bin/evn python3

def constant_f(arg):
    """
    Функции-константа:

    Написать функцию, принимающую аргумент, возвращающая
    новую функцию без аргументов, которая возрващает этот аргумент

    >>> f = constant_f(1)
    >>> val = f()
    >>> val
    1
    """

    def n():
        return arg

    return n

def argdict(*args, **kwargs):
    """
    Словарь аргументов:

    Написать функцию, которая возвращает словарь из аргументов
    для позиционных аргументов ключ-индекс позиции, а значения -
    сами аргументы, а для именнованных - имя аргумента и его значение

    >>> argdict(0, 1, 2, name = "Name")
    {0: 0, 1: 1, 2: 2, name: "Name"}
    """
    dict1 = {}
    i = 0
    for n in args:
        dict1[i] = n
        i += 1

    for k, v in kwargs.items():
        dict1[k] = v
    return dict1



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
    return not_implemented


def argmax_dict(d):
    """
    Ключ наибольшего значения

    Написать функцию, которая на вход получает словарь, а на выход возврашает
    ключ, для которого в словаре наибольшее значение:

    Пример:
    >>> argmax_dict({0: 2, 1: 5, 2: 10})
    2
    >>> argmax_dict9({0: 2, 1: 20, 3: 10})
    1
    """


    return not_implemented


def compose(*funcs):
    """
    Композиция функций

    Написать функцию, которая принимает набор других фунций от одного аргумента
    и возвращающую новыю функцию, которая является компоизицией этих
    функций. То есть для двух функций f(y) и g(x) их комопзиция
    f(g(x)): результат выполнения f для аргумента, которым является g(x)

    Пример:
    >>> plus_1 = lambda x: x + 1
    >>> mult_2 = lambda x: x * 2
    >>> f = compose(plus_1, mult_2)
    >>> f(1)
    3
    """
    return not_implemented


# =====================================================
# testing stuff
from funtests import CasesTestGen, not_implemented  # noqa: E402
import unittest  # noqa: E402


class FilterByKeyTest(CasesTestGen):
    def test_filter_by_key(self):
        cases = (
            (({i: i for i in range(10)}, lambda x: x % 2 == 0), {i: i for i in range(0, 10, 2)}),
            ((dict(zip("OnlyUpperShouldStay", range(50))), str.isupper), {'O': 0, 'U': 4, 'S': 15}),
        )
        self.execute_equal_subcases(filter_by_key, cases)


class ArgmaxTest(CasesTestGen):
    def test_argmax_dict(self):
        cases = (
            (({0: 2, 1: 5, 2: 10},), 2),
            (({0: 2, 1: 20, 3: 10},), 1))

        self.execute_equal_subcases(argmax_dict, cases)


class ArgDictTest(CasesTestGen):
    def test_argdict(self):
        cases = (
            ((0, 1, 2), {"name": "Name", "value": "Value"}, {0: 0, 1: 1, 2: 2, "name": "Name", "value": "Value"}),
            ((0, 1, 2), {}, {0: 0, 1: 1, 2: 2}),
            ((10, 0), {}, {0: 10, 1: 0}),
        )
        for case in cases:
            with self.subTest(case=case):
                args = case[0]
                kwargs = case[1]
                expected = case[2]
                val = argdict(*args, **kwargs)
                if val == not_implemented:
                    self.skipTest('не реализован')
                self.assertEqual(argdict(*args, **kwargs), expected)


class ComposeTest(CasesTestGen):
    def test_compose(self):
        cases = (
            ((lambda x: x + 1, lambda x: x * 2), (1,), 3),
            ((lambda x: x + 1, lambda x: x + 2, lambda x: x + 3), (1,), 7),
        )
        self.execute_genfunction_subcases(compose, cases)


class ConstantFTest(CasesTestGen):
    def test_constant_f(self):
        cases = (
            ((0,), tuple(), 0),
            (("abc",), tuple(), "abc"),
            (([1, 2, 3],), tuple(), [1, 2, 3]),
        )
        self.execute_genfunction_subcases(constant_f, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2)