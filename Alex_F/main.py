"""
@author: lataf 
@file: main.py 
@time: 16.11.2024 20:23
Модуль отвечает за 
UML схема модуля
Сценарий работы модуля:
Тест модуля находится в папке model/tests.
"""

import math


class Harrington:
    """Два односторонних критерия Харрингтона """

    def __init__(self):
        """Ахназарова С.Л., Кафаров В.В.; Методы оптимизации эксперимента в химической технологии;1985, с.209"""
        # self.health = _health  # Ссылка на родителя
        self.h_good = -math.log(math.log(1 / 0.80))  # Хороший результат по Харрингтону b_0 + b_1*y_good = h_good (1)
        self.y_good = 0  # Назначаем "хороший" параметр d = 0.8
        self.h_bad = -math.log(math.log(1 / 0.20))  # Плохой результат по Харрингтону b_0 + b_1 * y_bad = h_bad (2)
        self.y_bad = 0  # Назначаем "плохой" параметр d = 0.2
        self.b_0: float = 0  # Первый коэффициент в уравнении Харрингтона
        self.b_1: float = 0  # Второй коэффициент в уравнении Харрингтона
        self.d: float = 0  # Частная функция желательности Харрингтона для параметра y

    def calc(self, y_good: float, y_bad: float, y: float):
        """ Ахназарова с. 207   d = exp [—ехр(— у')]  у’ = bo + b1 * у' """
        self.b_1 = (self.h_good - self.h_bad) / (y_good - y_bad)  # Считаем b_1 из уравнений (1) и (2)
        self.b_0 = self.h_good - self.b_1 * y_good  # Считаем b_0 из уравнений (1) и (2)
        self.d = math.exp(-math.exp(-(self.b_0 + self.b_1 * y)))  # Считаем d по Ахназаровой с.207
        # print('h_good ', self.h_good)
        # print('h_bad ', self.h_bad)
        # print('b_1 ', self.b_1)
        # print('b_0', self.b_0)
        print('d', self.d)
        return self.d


if __name__ == '__main__':
    harrington = Harrington()
    print('lg(C)')
    harrington.calc(1.5,-0.5, 4)
    harrington.calc(1.5, -0.5, -2)
    ...
    #  Передаем логику внутрь функции
    # def apply(op, x, y):
    #     return (lambda a, b: a + b if op == "add" else a * b)(x, y)
    # print(apply("add", 2, 3))
