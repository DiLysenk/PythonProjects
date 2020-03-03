#!/usr/bin/env python3
from math import sqrt, cos, sin, pi

# Класс R^2:
#
# Написать класс описывающий двумерный вектор
class Vector2d():
    # У каждого объекта должно быть поле kind со значением-строка "vector2d"
    kind = None
    
    # Его поведение: конструктор по двум аргументам, координатам
    # Координаты должны быть доступны через экземпляр класса по именам x, y.
    def __init__(self, x, y):
        pass
    
    # Вектора должны уметь складываться друг с другом: результатом должен
    # быть новый вектор с координатами-суммами соответствующих полей
    def __add__(self, other):
        return

    # Можно получить обратный вектор, то есть новый вектор
    # с отрицательными относительно исходного координатами
    def __neg__(self):
        return

    # Вектора должы уметь вычитаться друг их друга
    def __sub__(self, other):
        return

    # Вектора можно проверять на равенство (равны ли их координаты)
    def __eq__(self, other):
        return
    
    # Строкове представление объекта str(Vector2d(1, 2)) - это "vector2d(x = 1, y = 2)"
    def __str__(self):
        return

    # У вектора есть длина: квадратный корень из квадратов координат
    def length(self):
        return

    # Можно создавать новый вектор при помощи поворота на заданный угол
    # https://ru.wikipedia.org/wiki/Поворот#Поворот_в_двумерном_пространстве
    def rotate(self, angle):
        return

import unittest
class TaskOOPSolutionTest(unittest.TestCase):

    def test_kind(self):
        v1 = Vector2d(0, 0)
        self.assertEqual(v1.kind, "vector2d", "Проверка поля kind")

    def test_coordinates(self):
        v1 = Vector2d(100, 200)
        self.assertEqual((v1.x, v1.y), (100, 200))

    def test_add(self):
        v1 = Vector2d(0, 0)
        v2 = Vector2d(1, 1)
        self.assertEqual(self.__to_tuple(v1 + v2), (1, 1))

    def test_neg(self):
        v1 = Vector2d(1, 2)
        self.assertEqual(self.__to_tuple(-v1), (-1, -2))

    def test_sub(self):
        v1 = Vector2d(0, 0)
        v2 = Vector2d(1, 1)
        self.assertEqual(self.__to_tuple(v1 - v2), (-1, -1))

    def test_eq(self):
        v1 = Vector2d(0, 0)
        v2 = Vector2d(0, 0)
        v3 = Vector2d(1, 1)
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)

    def test_str(self):
        v1 = Vector2d(0, 0)
        self.assertEqual(str(v1), "vector2d(x = 0, y = 0)")

    def test_length(self):
        v1 = Vector2d(1.0, 0.0)
        self.assertEqual(v1.length(), 1.0)

    def test_rotate(self):
        v1 = Vector2d(1.0, 0.0)
        self.assertTrue(self.__almost_equal(v1.rotate(pi/2), Vector2d(0.0, 1.0)))
        
    @staticmethod
    def __to_tuple(vector):
        return (vector.x, vector.y)

    @staticmethod
    def __almost_equal(v1, v2):
        return ((v2 - v1).length() / (v1 + v2).length()) < 0.0001
    
    def __gen_message(self, arg, got, expected, function):
        return """
Функция {name} для аргументов {arg} вернула неожидаемое значение:
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

    def __execute_equal_subcases(self, function, cases):
        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(*self.__build_equal_test_args(function, *case))
  
if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
