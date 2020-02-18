def front_x(words):
    """
    Я в начало

    Для заданного списка строк вернуть отсортированный обычным образом список,
    но с условием, что слова, начинающиеся на последнюю букву
    кириллического алфавита идут в начале

    >>> front_x(['яд', 'ад', 'ода', 'яз'])
    ['яд', 'яз', 'ад', 'ода']
    """



    words




    return not_implemented


def sort_last(tuples):
    """
    Последний решает

    Для заданного списка непустых кортежей из чисел, вернуть список,
    отсортированный по значению последнего элемента в кортежах

    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    return not_implemented


def symbol_count(string):
    """
    Количество символов

    Для заданной строки вернуть словарь, содержащий ключами символы из строки,
    а значениями: количество раз, сколько этот символ встретился в строке

    >>> import pprint
    >>> pprint.pprint(symbol_count("aaab"))
    {'a': 3, 'b': 1}
    """
    return not_implemented


def word_count(string):
    """
    Количество слов

    Для заданного текста вернуть словарь, содержащий ключами слова из строки,
    а значениями: количество раз, сколько эта строка встретилась в строке

    Пример:
    >>> wd = word_count('''Beautiful is better than ugly.
    ... Explicit is better than implicit.
    ... Simple is better than complex.
    ... Complex is better than complicated.''')
    >>> import pprint
    >>> pprint.pprint(wd, indent=4)
    {   'beautiful': 1,
        'better': 4,
        'complex': 2,
        'complicated': 1,
        'explicit': 1,
        'implicit': 1,
        'is': 4,
        'simple': 1,
        'than': 4,
        'ugly': 1}
    """
    return not_implemented


# =====================================================
# testing stuff
from  PythonProjects.task05.funtests import CasesTestGen, not_implemented  # noqa: E402
import unittest  # noqa: E402


class FrontXTest(CasesTestGen):

    def test_front_x(self):
        cases = (
            ((['Овечкин', 'Яшин', 'Малкин', 'Дацюк', 'Якушев'],),
             ['Якушев', 'Яшин', 'Дацюк', 'Малкин', 'Овечкин']),
            ((['яблоко', 'апельсин', 'банан', 'киви', '123'],),
             ['яблоко', '123', 'апельсин', 'банан', 'киви']),
            ((['гамильтониан', 'лапласиан', 'вронскиан', 'гессиан',  'грамиан', 'якобиан'],),
             ['якобиан', 'вронскиан', 'гамильтониан', 'гессиан', 'грамиан', 'лапласиан'])
        )
        self.execute_equal_subcases(front_x, cases)


class SortLastTest(CasesTestGen):
    def test_sort_last(self):
        cases = (
            (([(1, 3), (3, 2), (2, 1)],),
             [(2, 1), (3, 2), (1, 3)]),
            (([(2, 3), (1, 2), (3, 1)],),
             [(3, 1), (1, 2), (2, 3)]),
            (([(1, 7), (1, 3), (3, 4, 5), (2, 2)],),
             [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
        )
        self.execute_equal_subcases(sort_last, cases)


class SymbolCountTest(CasesTestGen):
    def test_symbol_count(self):
        cases = (
            (("aaa", ), {"a": 3}),
            (("aaabccdaa_,.a", ), {"a": 6, "b": 1, "c": 2, "d": 1, "_": 1, ",": 1, ".": 1}),
        )
        self.execute_equal_subcases(symbol_count, cases)


class WordCountTest(CasesTestGen):
    def test_word_count(self):
        cases = (
            ((
"""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.""",),
             {'beautiful': 1,
              'better': 4,
              'complex': 2,
              'complicated': 1,
              'explicit': 1,
              'implicit': 1,
              'is': 4,
              'simple': 1,
              'than': 4,
              'ugly': 1}),)

        self.execute_equal_subcases(word_count, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2)
