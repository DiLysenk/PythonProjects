#!/usr/bin/env python
from math import ceil

"""
Отприлагать

Для заданной строки, если её длина больше 2-х, w добавить "ий" на конец.
Однако если она уже оканчивается на ий, добавить перед "ий" "ейш"
Вернуть получившуюся строку
Для строки меньшей длины вернуть её самму
Пример: "син" -> "синий"
        "синий" -> "синейший"
        "ад" -> "ад"
"""


def adjective(string):
    if len(string) > 2 and string[-2:] != "ий":
        return (string + "{}").format("ий")
    elif string[-2:] == "ий" and len(string) > 2:
        return (string[:-2] + "{}" + string[-2:]).format("ейш")
    else:
        return string


"""
Не плохо

Для заданной строки, найти первые появление подстрок "не" и "плохо"
Если "не" идёт до "плохо", до заменить всю подстроку с "не" ... "плохо"
на "хорошо", для всех других случаев ничего со строкой не делать
Вернуть получившуюся строку

Пример: "Решать задания не так уж и плохо." -> "Решать задания хорошо."
"""


def not_bad(string):
    if string.find("не") >= 0: # проверка на вхлждение "не"
        if string.find("плохо") >= 0:       # проверка на вхождение "плохо"
            if string.find("не") < string.find("плохо"): # проверка на случай если "плохо" раньше чем "не"
                return (string[:string.index("не")] + "{}" + string[string.index("плохо") + len("плохо"):]).format("хорошо")
            else:
                return string
        else:
            return string
    else:
        return string


"""
Конец начала

Для заданных двух строк a и b, разбить их на две половины:
если длина нецелая, то средний символ идёт в первую половину
Вернуть строку, вида
начало_а + начало_b + конец_a + конец_b
"""


def front_back(a, b):
    half_a = ceil(len(a)/2)
    half_b = ceil(len(b)/2)
    string = a[:half_a] + b[:half_b] + a[half_a:] + b[half_b:]
    return string




"""
Валиден ли ip адресс

Написать предикат, то есть функцию, вовзращающую логическое значение,
Является ли аргумент строкой с описанием ipv4 адреса в
форме десятичной с точками (dotted decimal notation)

https://en.wikipedia.org/wiki/IPv4
"""


def is_ddn_ipv4(string):
    x = 0
    if type(string) == str:                                          # проверка типа
        if string.count(".") == 3:                                   # проверка количества точек
            for _ in range(len(string.split('.'))):                  # проверка октетов, что бы они были меньше чем 256
                if 0 <= (int(string.split('.')[_])) < 256:
                    x += 1                                            # x = количество октетов, больше
    return x == 4


# =====================================================
# testing stuff
class NotImplemented():
    pass


not_implemented = NotImplemented()

import copy, unittest


class Task2SolutionTest(unittest.TestCase):

    def test_adjective(self):
        cases = (
            (("син",), "синий"),
            (("синий",), "синейший"),
            (("ад",), "ад"),
        )

        self.__execute_equal_subcases(adjective, cases)

    def test_not_bad(self):
        cases = (
            (("Решать задания не так уж и плохо.",), "Решать задания хорошо."),
            (("",), ""),
            (("Мы действительно живём в глобальную информационную эпоху.",),
             "Мы действительно живём в глобальную информационную эпоху."),
        )

        self.__execute_equal_subcases(not_bad, cases)

    def test_front_back(self):
        cases = (
            (("1234", "bdef"), "12bd34ef"),
            (("12345", "bdefg"), "123bde45fg")
        )

        self.__execute_equal_subcases(front_back, cases)

    def test_is_ddn_ipv4(self):
        cases = (
            (('192.0.168.0',), True),
            (('192.0.168',), False),
            (('192.0.168.0.1',), False),
            (('8.8.8.8',), True),
            (('0.0.0.0',), True),
            (('257.0.0.1',), False),
            (('3221226219',), False),
            ((19201680,), False),
        )
        self.__execute_equal_subcases(is_ddn_ipv4, cases)

    def __gen_message(self, arg, got, expected, function):
        return """
Функция {name} для аргумента {arg} вернула неожидаемое значение:
Значение: {got}
Ожидалось: {expected}""".format(
            name=function.__name__,
            arg=arg,
            got=got,
            expected=expected)

    def __build_equal_test_args(self, function, arg, expected):
        got = function(*arg)
        return (
            got,
            expected,
            self.__gen_message(arg, got, expected, function)
        )

    def __build_mutation_test_args(self, function, obj, expected):
        arg = copy.deepcopy(obj)
        function(*obj)
        return (
            obj,
            expected,
            self.__gen_message(arg, obj, expected, function)
        )

    def __build_funcgen_test_args(self, function, gen_arg, fun_arg, expected):
        f = function(*gen_arg)
        got = f(*fun_arg)
        return (
            got,
            expected,
            self.__gen_message((gen_arg, fun_arg), got, expected, function)
        )

    def __execute_equal_subcases(self, function, cases):
        if function(*cases[0][0]) == not_implemented:
            self.skipTest('Не реализован')

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(*self.__build_equal_test_args(function, *case))

    def __execute_mutation_subcases(self, function, cases):
        if function(*copy.deepcopy(cases[0][0])) == not_implemented:
            self.skipTest('Не реализован')

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(*self.__build_mutation_test_args(function, *case))

    def __execute_genfunction_subcases(self, function, cases):
        if function(*copy.deepcopy(cases[0][0])) == not_implemented:
            self.skipTest('Не реализован')

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(*self.__build_funcgen_test_args(function, *case))


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)