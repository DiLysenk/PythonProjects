#!/usr/bin/env python3

# Поймай исключение, если сможешь
#
# Функция asin определена на области [-1, 1] и возвращает
# угол для которого синус равне аргументу
#
# Задача: узнать, что происходит, когда аргумент не имеет
# математического смысла и при помощи обработки исключений
# сделать функцию "безопасной": возвращающей None в случае вне области
# определения
def safe_asin(*args, **kwargs):
    from math import asin
    return asin(*args, **kwargs)

# Задекорируй меня полностью
#
# Реализовать четыре декоратора:
#
# Декоратор: check_single_arg: проверяет, что на вход функции подали
# только один позиционный аргумент и ни одного опционального
#
# Декоратор: check_float_arg: проверяет, что позиционный аргумент - вещественное число
# (см isinstace(x, float))
#
# Декоратор: check_ge_minus_1: проверяет, что на вход функции подали
# аргумент, не меньший -1.0

# Декоратор: check_le_plus_1: проверяет, что на вход функции подали
# аргумент, не больший 1.0
#
# С их помощью задекорировать функцию safest_asin для работы с произвольными аргументами
# с аналогичным safe_asin поведению
#
# Пример декоратора:
# def check_positive(func):
#     def wrapper(x):
#         if x > 0:
#             return func(x)
#         else:
#             return None
#     return wrapper
#
# Пример использования:
# # @check_positive
# def safe_sqrt(x):
#     from math import sqrt
#     return sqrt(x)
def safest_asin(x):
    from math import asin
    return asin(x)

import unittest
class TaskDecoratorSolutionTest(unittest.TestCase):
    cases = (
        (0.0, (0.0,), {}),
        (__import__("math").asin(0.123), (0.123,), {}),
        (None, (-2,), {}),
        (None, ("abc",), {}),
        (None, (0.0, 1.0), {}),
        (None, tuple(), {"arg": 0.5}),
    )

    def test_safe_asin(self):
        self.__execute_equal_subcases(safe_asin, self.cases)

    def test_safest_asin(self):
        self.__execute_equal_subcases(safest_asin, self.cases)

    def __gen_message(self, got, expected, function, *args, **kwargs):
        return """
Функция {name} для аргументов {arg} вернула неожидаемое значение:
Значение: {got}
Ожидалось: {expected}""".format(
        name=function.__name__,
        arg=(args, kwargs),
        got=got,
        expected=expected)

    def __execute_equal_subcases(self, function, cases):
        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(*self.__build_equal_test_args(function, case[0], *case[1], **case[2]))

    def __build_equal_test_args(self, function, expected, *args, **kwargs):
        got = function(*args, **kwargs)
        return (
            got,
            expected,
            self.__gen_message(got, expected, function, *args, **kwargs)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
