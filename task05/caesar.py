#!/usr/bin/evn python3
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def cipher_caesar(n, text):
    """
    Шифр цезаря. Зашифровать

    написать функцию шифрования сдвигом: когда каждая кириллическая
    буква в тексте заменяется на букву, следующую через n-позиций
    в алфавите, то есть для n = 2:
    а -> в, б -> г, е -> ж, н -> п и т.д. Последние буквы алфавита
    заменяются циклически, то есть для n = 2: ю -> а, я -> б. Это
    применяется как к строчным, так и к заглавным буквам Все прочие
    символы остаются без изменений.

    Полученную новую строку вернуть как результат
    """
    return not_implemented


def decipher_caesar(n, text):
    """
    Шифр цезаря. Расшифровать

    написать функцию расшифрования, которая по значению сдвига и зашифрованному сообщению
    возвращает расшифрованное значение
    """
    return not_implemented


def hack_caesar(text):
    """
    Шифр цезаря. Взломать

    Написать функцию расшифровки, не зная, конкретного значения сдвига.

    Можно воспользоваться уже реализованными функциями из предыдущих заданий
    Воспользоваться статистическим фактом: для текста не слишком маленького объёма
    частотность букв алфавита (как часто встречается буквы) близка к постоянным
    значениям (вне зависимости от текста)
    """
    return not_implemented


#  ####################################################################################################################
#  # testing stuff
#  ####################################################################################################################
from funtests import CasesTestGen, not_implemented  # noqa: E402
import unittest  # noqa: E402


class CaesarTest(CasesTestGen):
    def test_hack_caesar(self):
        ciphered = "М хынл, еаь хстяй црюнла ытецяаь. Ыь сюбрьч црюи п каьъ рьюьст ыта"
        unciphered = "Я знаю, что здесь играют нечисто. Но другой игры в этом городе нет"
        cases = list(
            ((cipher_caesar(n, ciphered), ), unciphered)
                for n in range(-5, 5))

        self.execute_equal_subcases(hack_caesar, cases)

    def test_cipher_caesar(self):
        cases = (
            ((0, "Текст, который не должен меняться"), "Текст, который не должен меняться"),
            ((3, "Гай Юлий Цезарь"), "Ёгм Болм Щзкгуя"),
            ((1, "абвгд"), "бвгде"),
            ((3, "!@#$"), "!@#$"),
            ((-10, ""), ""),
            ((2, "ОченьВажнаяИнформацияОсобоСекретная"), "РщжпюДвипвбКпцртовшкбРургрУжмтжфпвб"),
        )

        self.execute_equal_subcases(cipher_caesar, cases)

    def test_decipher_caesar(self):
        cases = (
            ((0, "Текст, который не должен меняться"), "Текст, который не должен меняться"),
            ((3, "Ёгм Болм Щзкгуя"), "Гай Юлий Цезарь"),
            ((1, "бвгде"), "абвгд"),
            ((3, "!@#$"), "!@#$"),
            ((-10, ""), ""),
            ((2, "РщжпюДвипвбКпцртовшкбРургрУжмтжфпвб"), "ОченьВажнаяИнформацияОсобоСекретная"),
        )

        self.execute_equal_subcases(decipher_caesar, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2)
