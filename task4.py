#!/usr/bin/env python3

import unittest
import copy

#######################################################################################################################
# Совпадающие концы
# Для заданного списка строк вернуть количество строк,
# таких, что их длина неменьше 2, при этом первый и последний
# символ совпадают
#
# То есть: 'aba' - удовлетворяющая условию строка, 'a' и 'abab' - нет
def match_ends(words):
    p = 0
    for string in words:   # для каждой строки в списке _ - идет как строка
        if len(string) >= 2:
            if string[0] == string[-1]:
                p += 1
    return p



#######################################################################################################################
# Частичная сумма
#
# Для последовательности, заданной аргументом - списком целых чисел вернуть
# новый список из частичных сумм последовательности
def partial_sum(ints):
    par_sum = []
    for integer in ints:
        n = 0
        for i in range(integer + 1):
            n = i + n
        par_sum.append(n)
    return par_sum


#######################################################################################################################
# Велосипед enumerate:
#
# Реализовать стандартную функцию enumerate для списков:
# Для произвольного списка, вернуть новый список, в котором
# содержатся пары (кортеж из двух элементов): индекс значения и само значение
# Пример: [3, 14, 15] -> [(0, 3), (1, 14), (2, 15)]
def list_enumerate(lst):
    enumerate_lst = []
    i = -1

    for integer in lst:

        i += 1
        lst1 = [i, integer]
        enumerate_lst.append(tuple(lst1))
    return enumerate_lst


#######################################################################################################################
# Пересечение
#
# Написать предикат (логическую функцию, возвращающую True или False)
# проверяющий, есть ли в двух списках хотя бы один одинаковый элемент
# Пример: ([0, 1, 2], [3, 4]) -> False
#         ([0, 1, 2], [2, 3]) -> True
def have_same_element(lst1, lst2):
    return len(set(lst1+lst2)) != len(lst1) + len(lst2) # сравним длину  множества суммы  двух списков и сумму элементов двух списков




#######################################################################################################################
# Единичная матрица из списков
#
# Написать функцию, создающую спискок из n-списков, таких что
# Для этого списка lst: lst[i][j] == 0 для всех i != j и
# lst[i][j] == 1 для всех i == j.
# Пример: n = 3 -> [ [1, 0, 0],
#                    [0, 1, 0],
#                    [0, 0, 1] ]
#        
def identity_2d_lists(n):
    a = [] # пустой список для основного результата
    for i in range(n):
        b = []
        for j in range(n):
            if i == j:
                b.append(1)
            else:
                b.append(0)
        a.append(b)
    return a



# =====================================================
# testing stuff
# =====================================================
class NotImplemented():
    """
    Stub class for not_implemented instance. Used in automatic
    skipping of tests.
    """
    pass


not_implemented = NotImplemented()


class CasesTestGen(unittest.TestCase):
    """
    Class for automatic test running, according to simple tuple
    of arguments and expected values
    """

    def __gen_message(self, arg, got, expected, function):
        return """
Функция {name} для аргумента {arg} вернула неожидаемое значение:
Значение: {got}
Ожидалось: {expected}""".format(
            name=function.__name__,
            arg=arg,
            got=got,
            expected=expected)

    def __build_equal_test_args(self, function, args, expected):
        new_args = copy.deepcopy(args)
        got = function(*new_args)
        return (
            got,
            expected,
            self.__gen_message(args, got, expected, function)
        )

    def __build_mutation_test_args(self, function, obj, expected):
        arg = copy.deepcopy(obj)
        function(*arg)
        return (
            arg,
            expected,
            self.__gen_message(obj, arg, expected, function)
        )

    def __build_funcgen_test_args(self, function, gen_arg, fun_arg, expected):
        f = function(*gen_arg)
        got = f(*fun_arg)
        return (
            got,
            expected,
            self.__gen_message((gen_arg, fun_arg), got, expected, function)
        )

    def execute_equal_subcases(self, function, cases):
        """
        Run <cases> as subtests to test <function>

        Example: fun = lambda x: x + x, cases = ()
        """
        first_case_copy = copy.deepcopy(cases[0][0])
        if function(*first_case_copy) == not_implemented:
            self.skipTest('Не реализован')

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(
                    *self.__build_equal_test_args(function, *case))

    def execute_mutation_subcases(self, function, cases):
        first_case_copy = copy.deepcopy(cases[0][0])
        if function(*first_case_copy) == not_implemented:
            self.skipTest('Не реализован')

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(
                    *self.__build_mutation_test_args(function, *case))

    def execute_genfunction_subcases(self, function, cases):
        first_case_copy = copy.deepcopy(cases[0][0])
        if function(*first_case_copy) == not_implemented:
            self.skipTest('Не реализован')

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(
                    *self.__build_funcgen_test_args(function, *case))


class Task3Test(CasesTestGen):

    def test_match_ends(self):
        cases = (
            ((['aba', 'xyz', 'aa', 'x', 'bbb'],), 3),
            ((['', 'x', 'xy', 'xyx', 'xx'],), 2),
            ((['aaa', 'be', 'abc', 'hello'],), 1)
        )
        self.execute_equal_subcases(match_ends, cases)

    def test_partial_sum(self):
        cases = (
            (([0, 0, 0, 0],), [0, 0, 0, 0]),
            (([0, 1, 2, 3],), [0, 1, 3, 6])
        )
        self.execute_equal_subcases(partial_sum, cases)

    def test_list_enumerate(self):
        cases = (
            (([3, 14, 15],),
             [(0, 3), (1, 14), (2, 15)]),
            (([int, str, float],),
                list(enumerate([int, str, float]))
             )
        )
        self.execute_equal_subcases(list_enumerate, cases)

    def test_have_same_element(self):
        cases = (
            ( ([0, 1, 2], [3, 4]), False),
            ( ([0, 1, 2], [2, 3]), True),
            ( ([], []), False),
            ( ([0], [1]), False),
            ( ([0], [0]), True)
        )
        self.execute_equal_subcases(have_same_element, cases)
        
    def test_identity_2d_lists(self):
        cases = (
            ( (1,), [[1]] ),
            ( (2,), [[1, 0], [0, 1]]),
            ( (3,), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        )
        self.execute_equal_subcases(identity_2d_lists, cases)
              
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
