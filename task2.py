#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############################################################################
# Функция, возвращающая единицу
#
# Написать функцию, всегда возвращающую единицу
#
# one() -> 1
def one():
    result = 0.0
    truncation_error = 1.0
    precision = 10 ** -5
    n = 1
    # geometric sum of 1/2+1/4+1/8+1/16 + ...
    while truncation_error > precision:
        term = 2 ** -n
        result += term
        n += 1
        truncation_error = 2 * term

    result = int(round(result))
    return result


###############################################################################
# Единичная функция
#
# Написать функцию, возвращающую свой аргумент
#
# identity("a") -> "a"
def identity(x):
    return x


###############################################################################
# Инфляция
#
# Написать функцию, вычисляющую стоимость объекта через
# несколько лет. Каждый год стоимость растет на определенный процент.
#
# orig - начальная стоимость
# ir - значение роста стоимости в процентах
# n - количество лет
def inflation(orig, ir, n):
    cost = orig * ((ir / 100) + 1)
    for i in range(n - 1):
        cost = cost * ((ir / 100) + 1)
    return cost


###############################################################################
# Делимость
# Написать предикат (функцию, возвращающую логическое значение), проверяющий
# делиться ли одно число на другое
def is_divisor(dividend, divisor):
    return dividend % divisor == 0


###############################################################################
# Простое число
#
# Задание: написать предикат (функцию, возвращающую логическое значение),
# проверяющие является ли аргумент простым числом
def is_prime(n):
    x = 0
    for i in range(1, n):
        if n % i == 0:
            x += 1
    return x <= 1


# Печеньки
#
# Для заданного целого числа count, вернуть строку
# формы 'Number of cookies: <count>', но если count больше 10,
# тогда заменить число на слово 'many'
#
# Пример: cookies(5): 'Number of cookies: 5'
def cookies(count):
    if count > 10:
        count = "many"
    return "Number of cookies: {}".format(count)


# Перемешивание
#
# Задание: для заданных строк a и b, вернуть новую строку
# из <a> и <b>, разделённых пробелом, но при этом поменять в них
# первые два символа.
#
# Пример: 'mix', pod' -> 'pox mid'
#         'dog', 'dinner' -> 'dig donner'
#
#

def mix_up(a, b):
    answer = "{} {}".format(b[:2] + a[2::], a[:2] + b[2::])
    return answer


# Палиндром
#
# Задание: написать предикат (функцию, возвращающую логическое значение)
# возвращающая результат проверки, является ли аргумент строкой-палиндромом
def is_palindrome(string):
    return string == string[::-1]


# Вонни
#
# Задание: для заданной строки string, вернуть строку без гласных
# Пример: vonny('bezyskhodnost'): 'bzskhdnst'
def vonny(string):
    for _ in "aoyeui":
        string = string.replace(_, '')
    return string


# Тэгирование
#
# Написать функцию, которая оборачивает строку string в "тэг" tag
#
# add_tags("i", "Python") -> "<i>Python</i>"
def add_tags(tag, string):
    string_tag = "<{0}>{1}</{0}>".format(tag, string)
    return string_tag


# В верхний регистр
#
# Написать функцию, которая переводит всю строку в верхней регистр в случае, если
# строка начинается с двух букв в верхнем регистре. Иначе вернуть исходную
#
#
def to_uppercase(string):
    if string[:2].isupper():
       return string.upper()
    else:
        return string


# =====================================================
# testing stuff
class NotImplemented():
    pass


not_implemented = NotImplemented()

import copy, unittest


class Task2SolutionTest(unittest.TestCase):

    def test_one(self):
        cases = (
            (tuple(), 1),
        )
        self.__execute_equal_subcases(one, cases)

    def test_identity(self):
        cases = (
            ((1,), 1),
            (('abc',), 'abc')
        )
        self.__execute_equal_subcases(identity, cases)

    def test_inflation(self):
        cases = (
            ((100.0, 50, 1), 150.0),
            ((100.0, 50, 2,), 225.0)
        )
        self.__execute_equal_subcases(inflation, cases)

    def test_is_divisor(self):
        cases = (
            ((100, 5), True),
            ((111, 3), True),
            ((10, 3), False)
        )
        self.__execute_equal_subcases(is_divisor, cases)

    def test_is_prime(self):
        cases = (
            ((2,), True),
            ((3,), True),
            ((4,), False),
            ((1443,), False),
            ((2019,), False),
            ((39916801,), True),
        )
        self.__execute_equal_subcases(is_prime, cases)

    def test_cookies_dict(self):
        cases = (
            ((4,), 'Number of cookies: 4'),
            ((9,), 'Number of cookies: 9'),
            ((10,), 'Number of cookies: 10'),
            ((99,), 'Number of cookies: many'))

        self.__execute_equal_subcases(cookies, cases)

    def test_mix_up(self):
        cases = (
            (('mix', 'pod'), 'pox mid'),
            (('dog', 'dinner'), 'dig donner'),
            (('gnash', 'sport'), 'spash gnort'),
            (('pezzy', 'firm'), 'fizzy perm'),
            (('aaaaaa', 'bbbbbb'), 'bbaaaa aabbbb'))

        self.__execute_equal_subcases(mix_up, cases)

    def test_is_palindrome(self):
        cases = (
            (('a',), True),
            (('case esac',), True),
            (('palindrome',), False),
        )

        self.__execute_equal_subcases(is_palindrome, cases)

    def test_is_vonny(self):
        cases = (
            (('bezyskhodnost',), 'bzskhdnst'),
            (('Samaritan',), 'Smrtn'),
            (('L33T',), 'L33T'),
            (('eyuioa',), ''),
        )

        self.__execute_equal_subcases(vonny, cases)

    def test_add_tags(self):
        cases = (
            (('i', 'Python'), '<i>Python</i>'),
            (('script', 'console.log("Hello from javascript");'),
             '<script>console.log("Hello from javascript");</script>'),
        )

        self.__execute_equal_subcases(add_tags, cases)

    def test_to_uppercase(self):
        cases = (
            (("Alfred Hitchcock",), "Alfred Hitchcock"),
            (("INgmar Bergman",), "INGMAR BERGMAN"),
            (("ab",), "ab")
        )

        self.__execute_equal_subcases(to_uppercase, cases)

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
