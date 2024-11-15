# Этилацетат (Марка А, высший сорт, ГОСТ) (200мл - объём в одной банке):
# плотность этилацетата: p = 0,902 г/куб.см = 0,902 г/мл
# плотность воды: p = 1г/мл
# молекулярный вес этилацетата: M = 88,1 г/моль
# растворимость этилацетата по массе при стандартных условиях (20-25С) = 10-12%

"""Создать функцию, рассчитывающую сколько надо добавить растворителя к определённому объему этилацетата,
чтобы понизить молярную концентрацию до заданной величины"""

"""желаемая молярная концентрация = (кол-во в-ва раствор этилацетата)/(объем этилацетата(л) + объем растворителя(л))
 поэтому =>

объем растворителя = ((кол-во в-ва раствор этилацетата)/(жел.моляр.конц))*1000 - объем этилацетата"""
# Умножение на 1000 - перевод в литры

"""Массовая доля этилацетата, соответствующая его верхней границе растворимости = 0.1 (берём по нижней границе,
так как нужно разбавлять, и пользователь не должен получать объём разбавителя, при котором % этилацетата
будет превышать его растворимость)
связь массовой доли(w) и мольной доли(C): 
С = (10*w*p)/M"""

C_max_ethyl_acetate = (10 * 10 * 0.902) / 88.1

V_ethyl_acetate = int(input("Начальный объем этилацетата, мл: "))
C_ethyl_acetate_desired = float(input("Желаемая молярная концентрация этилацетата, моль/л: "))

while C_ethyl_acetate_desired > C_max_ethyl_acetate:
    print(f'Желаемая молярная концентрация этилацетата превышает его максимальную растворимость.\n' +
          'Задайте другую молярную концентрацию, не превышающую ' + f'{C_max_ethyl_acetate:3f} моль/л\n')
    C_ethyl_acetate_desired = float(input('Новая желаемая молярная концентрация этилацетата, моль/л: '))

m_ethyl_acetate = V_ethyl_acetate * 0.902  # исходная масса этилацетата
m_ethyl_acetate_soluted = m_ethyl_acetate * 0.11  # ниже укажем погрешность в +-1% растворимости
n_ethyl_acetate_soluted = m_ethyl_acetate_soluted / 88.1  # кол-во в-ва растворённого этилацетата
the_account_of_solution_error = (m_ethyl_acetate * 0.01) / 88.1  # учет погрешности растворимости этилацетата (10-12%)


def diluent_func():
    V_diluent = (n_ethyl_acetate_soluted / C_ethyl_acetate_desired) * 1000 - V_ethyl_acetate  # масса растворителя
    print("Потребуется " + f'{V_diluent:,.3f}' +
          " мл растворителя (воды), чтобы достичь желаемой молярной концентрации этилацетата.")


def error_diluent_func():
    V_diluent_solution_error = (the_account_of_solution_error / C_ethyl_acetate_desired) * 1000 - V_ethyl_acetate
    print("Вероятно потребуется добавить или убавить " + f'{V_diluent_solution_error:,.3f}'
          + " мл растворителя (воды) с учётом погрешности растворимости этилацетата.")


diluent_func()
error_diluent_func()