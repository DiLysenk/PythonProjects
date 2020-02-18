def reverse_dict(d):
    """
    Разворот словаря

    Преобразовать заданный словарь таким образом, чтобы значения стали ключами,
    а ключи значениями. Можно считать, что все значения уникальны и хэширеумы

    Note: функция не обязана возвращать этот словарь, но обязана изменить
    словарь, подваваемый на вход

    >>> d = {'a': 1, 'b': 2}
    >>> reverse_dict(d)
    >>> d
    {1: 'a', 2: 'b'}
    """
    return not_implemented


def swap_in_list(lst, index1, index2):
    """
    Обменять элементы списка

    Преобразовать заданный список таким образом, чтобы
    элементы по заданным индексам обменялись местами

    >>> lst = [0, 1, 2, 3]
    >>> swap_in_list(lst, 0, 3)
    >>> lst
    [3, 1, 2, 0]
    """
    return not_implemented


def filter_in_place(filter_fun, lst):
    """
    Фильтр "на месте"

    Согласно фильтрующей функции filter_fun убрать из списка
    все элементы, для которых filter_fun вернёт не истинное значение

    >>> lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> filter_in_place(lambda x: x % 3 == 0, lst)
    >>> lst
    [0, 3, 6, 9]
    """
    return not_implemented


# =====================================================
# testing stuff
from  PythonProjects.task05.funtests import CasesTestGen, not_implemented  # noqa: E402
import unittest  # noqa: E402


class ReverseTest(CasesTestGen):
    def test_reverse_dict(self):
        cases = (
            (({1: 2, 2: 3, 3: 4},), ({2: 1, 3: 2, 4: 3},)),
        )

        self.execute_mutation_subcases(reverse_dict, cases)


class SwapInListTest(CasesTestGen):
    def test_swap_in_list(self):
        cases = (
            (([0, 1, 2, 3], 0, 3), ([3, 1, 2, 0], 0, 3)),
        )

        self.execute_mutation_subcases(swap_in_list, cases)


class FilterInPlaceTest(CasesTestGen):
    def test_filter_in_place(self):
        def div_by_3(x): return x % 3 == 0
        def endswith_digit(string): return string[-1].isdigit()

        cases = (
            ((div_by_3, [0, 1, 2, 3, 4, 5, 6]), (div_by_3, [0, 3, 6])),
            ((endswith_digit, ['a', 'b', 'c1', 'd2', 'e', 'f3', 'rr']), (endswith_digit, ['c1', 'd2', 'f3'])),
        )

        self.execute_mutation_subcases(filter_in_place, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2)
