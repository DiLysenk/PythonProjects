#!/usr/bin/env python3

# Физические единицы: длина
#
# Дополнить класс работы с объектами типа длина
# Уже реализованная функциональность: создание объектов методами
# from_micrometres и , доступны поля-свойства
# micrometres и nautical_miles
#
# Добавить следующие поля-свойства физических единиц длины:
# метры, милиметры, футы, ярды
#
# Добавить тесты в класс TaskOOP2Solution по аналогии с уже написанным
# test_micrometres
class Length:
    def __init__(self, *args, **kwargs):
        """Полностью скрытое внутреннее состояние: стандартный конструктор не работает"""
        raise ValueError("No default constructor available")

    __str__ = lambda s: "Length: {} metres".format(s._micrometres)

    @classmethod
    def from_micrometres(cls, micrometres):
        """Конструктор объектов из микрометров"""
        length_obj = cls.__new__(cls) # создание объекта класса cls
        length_obj.micrometres = micrometres
        return length_obj

    @property
    def micrometres(self):
        return self._micrometres

    @micrometres.setter
    def micrometres(self, value=0.0):
        if value < 0.0:
            raise ValueError("Length cannot be less than zero")
        self._micrometres = value

    @micrometres.deleter
    def micrometres(self):
        self._micrometres = 0.0

    @classmethod
    def from_nautical_miles(cls, nautical_miles):
        """Конструктор объектов из морских миль"""
        length_obj = cls.__new__(cls) # создание объекта класса cls
        length_obj.nautical_miles = nautical_miles
        return length_obj

    @property
    def nautical_mile(self):
        return self._micrometres / 1852 / 10 ** 6

    @nautical_mile.setter
    def nautical_mile(self, value=0.0):
        self.micrometres = value * 1852 * 10 ** 6

    @nautical_mile.deleter
    def nautical_mile(self, value=0.0):
        del self.micrometres

import unittest
class TaskOOP2SolutionTest(unittest.TestCase):

    def test_nautical_mile(self):
        micrometres = 1852.0 * 10 ** 6

        # создание объекта конструктором-методом класса
        obj = Length.from_micrometres(micrometres)

        # проверка двух объектов на равенство
        self.assertEqual(obj._micrometres,  micrometres)
        self.assertEqual(obj.micrometres, micrometres)

        # проверка даух чисел на "почти" равенство (для вещественных чисел)
        self.assertAlmostEqual(obj.nautical_mile, 1.0)

        obj.nautical_mile = 2.0
        self.assertAlmostEqual(obj.micrometres, 3704000000.0)

        del obj.nautical_mile
        self.assertAlmostEqual(obj.micrometres, 0.0)

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
