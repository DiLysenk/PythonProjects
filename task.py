import math
def front_x(words):
    words.sort()
    return words








print(front_x(['яд', 'ад', 'ода', 'яз']))

exit()








def constant_f(arg):
    def f():
        return arg
    return f()






def factors(n):
    m = []
    for i in range(1, n + 1):
        if n % i == 0:
            m.append(i)
    return m


print(factors(12))

exit()


def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


exit()

""" код цезаря """
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

n = 1
text = "абвг жз"
text2 = []
text_cesar = 1

if len(text.split()) == 1:
    for i in range(len(text)):
        text2.append(alphabet[alphabet.find(text[i]) - len(alphabet) + n])
        text_cesar = "".join(text2)

elif len(text.split()) > 1:
    lst_text = text.split()
    for string in lst_text:
        print(string)
        for i in range(len(string)):
            print(string)
            print(text2)
            text2.append(alphabet[alphabet.find(text[i]) - len(alphabet) + n])
            text_cesar = "".join(text2)
        print(text_cesar)
    lst_text_cesar = " ".join(text_cesar)
    print(lst_text_cesar)


def front_back(a, b):
    half_a = ceil(len(a) / 2)
    half_b = ceil(len(b) / 2)
    string = a[:half_a] + b[:half_b] + a[half_a:] + b[half_b:]
    return string


def is_ddn_ipv4(string):
    x = 0
    if type(string) == str:
        print(x, 1)
        if string.count(".") == 3:
            print(x, 2)
            for x in range(len(string.split('.'))):
                print(x, 3)
                if int(string.split('.')[x]) < 256:
                    print(string.split('.')[x])
                    print(x)

    return x == 4


def not_bad(string):
    if string.find("не") >= 0:
        if string.find("плохо") >= 0:
            if string.find("не") < string.find("плохо"):
                return (string[:string.index("не")] + "{}" + string[string.index("плохо") + len("плохо"):]).format(
                    "хорошо")
            else:
                return string
        else:
            return string
    else:
        return string


def is_divisor(dividend, divisor):
    return dividend % divisor == 0


def is_prime(n):
    x = 0
    for i in range(1, n):
        if n % i == 0:
            x += 1
    return x <= 1


def is_palindrome(string):
    return string == string[::-1]


def vonny(string):
    for _ in 'aoyeui':
        string = string.replace(_, '')
    return string


def match_ends(words):
    p = 0
    i = -1
    for _ in words:
        i += 1
        if len(words[i]) > 2:
            if words[i][0] == words[i][-1]:
                p += 1
    return i


def partial_sum(ints):
    par_sum = []
    for integer in ints:
        n = 0
        for i in range(integer + 1):
            n = i + n
        par_sum.append(n)
    return par_sum


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


def have_same_element(lst1, lst2):
    return len(set(lst1 + lst2)) == len(lst1) + len(
        lst2)  # сравним длину  множества суммы  двух списков и сумму элементов двух списков


print(have_same_element([0, 1, 2], [3, 4]))

exit()
