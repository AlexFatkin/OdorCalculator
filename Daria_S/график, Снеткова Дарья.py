import math

import matplotlib.pyplot as plt


class Harrington:

    def __init__(self):
        # self.health = _health  # Ссылка на родителя
        self.h_good = -math.log(math.log(1 / 0.80))  # Хороший результат по Харрингтону b_0 + b_1*y_good = h_good (1)
        self.y_good = 0  # Назначаем "хороший" параметр d = 0.8
        self.h_bad = -math.log(math.log(1 / 0.20))  # Плохой результат по Харрингтону b_0 + b_1 * y_bad = h_bad (2)
        self.y_bad = 0  # Назначаем "плохой" параметр d = 0.2
        self.b_0: float = 0  # Первый коэффициент в уравнении Харрингтона
        self.b_1: float = 0  # Второй коэффициент в уравнении Харрингтона
        self.d: float = 0  # Частная функция желательности Харрингтона для параметра y

    def calc(self, y_good: float, y_bad: float, y: float):
        self.b_1 = (self.h_good - self.h_bad) / (y_good - y_bad)  # Считаем b_1 из уравнений (1) и (2)
        self.b_0 = self.h_good - self.b_1 * y_good  # Считаем b_0 из уравнений (1) и (2)
        self.d = math.exp(-math.exp(-(self.b_0 + self.b_1 * y)))  # Считаем d по Ахназаровой с.207
        return self.d


if __name__ == '__main__':
    harrington = Harrington()


    def float_range(start, stop, step):
        current = start
        while current < stop:
            yield current
            current += step


    start = -1.0
    stop = 4.0
    step = 0.001
    x_list = []
    y_list = []

    for value in float_range(start, stop, step):
        x_list.append(value)

    for y1 in x_list:
        y = harrington.calc(1.5, -0.5, y1)
        y_list.append(y)

    plt.plot(x_list, y_list)
    plt.grid(True)
    plt.xlabel("lg('C); C, мкмоль/мл")
    plt.ylabel('d')
    plt.title('Функция Харрингтона')

    plt.show()
