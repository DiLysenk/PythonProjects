def plus_one(n):
    """
    Написать функцию, возвращающую число на 1 больше своего аргумнта n

    >>> plus_one(5)
    6
    >>> plus_one(-1)
    0
    """
    return not_implemented


def max_of_three(a, b, c):
    """
    Написать функцию, возвращающую максимум из трёх элементов

    >>> max(1, 5, 3)
    5
    >>> max(10, 20, 30)
    30
    >>> max('z', 'b', 'a')
    'z'
    """
    return not_implemented


def sign(n):
    """
    Написать функцию возвращающую знак числа n:
    -1 для отрицательных, 0 для 0 и +1 для положительных

    >>> sign(-25.0)
    -1
    >>> sign(3.14)
    1
    >>> sign(0.0)
    0
    """
    return not_implemented


def fibonacci(n):
    """
    Написать функцию, возвращаюее n-е число Фибоначчи

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(20)
    6765
    """
    return not_implemented


def factors(n):
    """
    Написать функцию, возвращающую все делители числа n в виде
    упорядоченного возрастающего списка

    >>> factors(2)
    [1, 2]
    >>> factors(12)
    [1, 2, 3, 4, 6, 12]
    """
    return not_implemented


# =====================================================
# testing stuff
from funtests import CasesTestGen, not_implemented  # noqa: E402
import unittest  # noqa: E402

class PlusOneTest(CasesTestGen):
    def test_plus(self):
        cases = (
            ((5,), 6),
            ((-10,), -9),
        )
        self.execute_equal_subcases(plus_one, cases)


class MaxOfThreeTest(CasesTestGen):
    def test_max_of_three(self):
        cases = (
            ((1, 5, 3), 5),
            ((10, 20, 30), 30),
            (('z', 'b', 'a'), 'z'),
        )
        self.execute_equal_subcases(max_of_three, cases)


class SignTest(CasesTestGen):
    def test_sign(self):
        cases = (
            ((1.5, ), 1),
            ((-3, ), -1),
            ((0.0, ), 0),
            ((0, ), 0),
        )
        self.execute_equal_subcases(sign, cases)


class FactorsTest(CasesTestGen):
    def test_factors(self):
        cases = (
            ((2,), [1,2]),
            ((12,), [1, 2, 3, 4, 6, 12]),
        )
        self.execute_equal_subcases(factors, cases)


class FibonacciTest(CasesTestGen):
    def test_fibonacci(self):
        cases = (
            ((0, ), 0),
            ((1, ), 1),
            ((2, ), 1),
            ((3, ), 2),
            ((4, ), 3),
            ((5, ), 5),
            ((20, ), 6765),
        )
        self.execute_equal_subcases(fibonacci, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2)
