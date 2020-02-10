import copy
import unittest

from . import not_implemented

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
