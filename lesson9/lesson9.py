"""
Ex1
Продолжаем задачу из предыдущего урока
Используя дескрипторы, проверьте правильность введённых данных (a, b, c, d, r > 0).
square и perimeter -  теперь свойства. Обратите внимание, что при каждом обращении к square/perimeter
значения будут вычисляться заново. Подумайте, как это можно обойти,
т.е. значение должно вычисляться только при первом обращении к свойству.
"""


"""
Ex2
Напишите менеджер контекста MultiFileOpen, который позволяет работать с несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""

from contextlib import contextmanager

@contextmanager
def mfo(*args):
    f = map(lambda x: open(x, 'w'), args)
    yield f
    for i in f:
        i.close()


"""
Ex3
Напишите генератор fibonacci(n), который генерирует числа Фибоначчи до n включительно.
"""

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


"""
Ex4
Напишите генератор factorials(n), генерирующий последовательность факториалов натуральных чисел.
"""

def factorials(n):
    f = 1
    for i in range(1,n+1):
       f *= i
       yield f


"""
Ex5*
Напишите генератор binomial_coefficients(n), генерирующий последовательность биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


"""
Ex6
Напишите класс, объектом которого будет итератор производящий только чётные числа до n включительно.
"""

class EvenNumb:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.e = 0
        return self

    def __next__(self):
        if self.e <= self.n:
            r = 0 + self.e
            self.e += 2
            return r
        else:
            raise StopIteration
"""
Ex7
Напишите метакласс, который возводит имена всех аттрибутов класса в верхний регистр.
"""
