DENSITY_OF_ETHYL_ACETATE = 0.902  # плотность этилацетата (г/см^3)
MOLECULAR_WEIGHT_OF_ETHYL_ACETATE = 88.1  # молекулярный вес этилацетата (г/моль)
MIN_PERCENTAGE_CONCENTRATION_OF_ETHYL_ACETATE = 10
# минимальная процентная концентрация этилацетата (%)
MAX_PERCENTAGE_CONCENTRATION_OF_ETHYL_ACETATE = 12


# максимальная процентная концентрация этилацетата (%)

# Нахождние минимальной молярной концентрации,
# при которой  этилацетат будет полностью растворятся
# C = 10 * w(%) * p / M, где C — молярная концентрация,
#  w(%) — массовая доля (процентная концентрация), p — плотность раствора,
# M — молярная масса растворённого вещества.
def min_concentration_ethyl_acetate():
    min_concentration = 10 * MIN_PERCENTAGE_CONCENTRATION_OF_ETHYL_ACETATE * DENSITY_OF_ETHYL_ACETATE / MOLECULAR_WEIGHT_OF_ETHYL_ACETATE
    return min_concentration


def max_concentration_ethyl_acetate():
    max_concentration = 10 * MAX_PERCENTAGE_CONCENTRATION_OF_ETHYL_ACETATE * DENSITY_OF_ETHYL_ACETATE / MOLECULAR_WEIGHT_OF_ETHYL_ACETATE
    return max_concentration


def error_rate(volume, volume_average):
    absolute_error = volume - volume_average  # Абсолютная погрешность
    relative_error = absolute_error / volume_average * 100  # Относительная погрешность
    return absolute_error, relative_error


def main():
    # Ввод с клавиатуры начального объема этилацетата
    initial_volume_of_ethyl_acetate = float(input('Введите начальный объем этилацетата: '))
    # Ввод с клавиатуры желаемой молярной концентрации
    desired_molar_concentration_of_ethyl_acetate = float(input('Введите желаемую молярную концентрацию этилацетата в г/моль\
(молярная концентрация не должна превышать 1,02 г/моль) '))
    while desired_molar_concentration_of_ethyl_acetate > min_concentration_ethyl_acetate():
        desired_molar_concentration_of_ethyl_acetate = float(input('Введите новую желаемую молярную концентрацию этилацетата в г/моль\
(молярная концентрация НЕ ДОЛЖНА превышать 1,02 г/моль)'))
    # формула для нахождения необходимого объема растворителя ( объем растворителя = масса этилацетата (плотность*объем)/желаемую молярную концентрацию*
    # *молекулярный вес - объем этилацетата)
    solvent_volume = (
                                 DENSITY_OF_ETHYL_ACETATE * initial_volume_of_ethyl_acetate / desired_molar_concentration_of_ethyl_acetate \
                                 * MOLECULAR_WEIGHT_OF_ETHYL_ACETATE) - initial_volume_of_ethyl_acetate
    # Нахождение объема для минимальной процентной концентрации этилацетата
    solvent_volume_min_concentration = (
                                                   DENSITY_OF_ETHYL_ACETATE * initial_volume_of_ethyl_acetate / min_concentration_ethyl_acetate() \
                                                   * MOLECULAR_WEIGHT_OF_ETHYL_ACETATE) - initial_volume_of_ethyl_acetate
    # Нахождение объема для максимальной процентной концентрации этилацетата
    solvent_volume_max_concentration = (
                                                   DENSITY_OF_ETHYL_ACETATE * initial_volume_of_ethyl_acetate / max_concentration_ethyl_acetate() \
                                                   * MOLECULAR_WEIGHT_OF_ETHYL_ACETATE) - initial_volume_of_ethyl_acetate
    # Нахождение среднего объема
    average_volume = (solvent_volume_min_concentration + solvent_volume_max_concentration) / 2
    a_error, r_error = error_rate(solvent_volume_min_concentration, average_volume)
    print(
        f' Для получения раствора с желаемой молярной концентрацией необходимо добавить:{solvent_volume / 1000:.3f} л. +- {a_error / 1000:.3f} л, ',
        f'относительная погрешность составит {r_error:.0f}%')


if __name__ == '__main__':
    main()




