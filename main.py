def calculate_dilution(target_concentration: float):
    """Функция для создания серии разбавлений, необходимых для достижения заданной концентрации раствора этилацетата.
    Выводит в консоль шаги серии разбавлений, конечную концентрацию и погрешность разбавления.
    :param target_concentration: Требуемая конечная концентрация раствора (моль/л)
    :return: Список шагов в серии разбавлений, погрешность разбавления в %

    """
    mass_fraction = 11  # Массовая доля этилацетата (%)
    density = 0.902  # Исходная плотность (г/мл)
    max_flask_volume = 20  # Максимальный объем флакона (мл)
    ether_molar_mass = 88.1  # Молярная масса этилацетата (г/моль)
    tolerance = 0.25  # Погрешность разбавления (%)
    minimum_volume = 0.02  # Минимальный объем, который можно набрать (цена деления) (мл)

    initial_concentration = density * mass_fraction * 10 / ether_molar_mass  # Исходная концентрация этилацетата (моль/л)
    molarity_tolerance = (tolerance / 100) * target_concentration  # Допустимая погрешность разбавления (моль/л)

    current_concentration = initial_concentration
    steps = []
    flask_count = 0  # Количество флаконов

    if target_concentration > initial_concentration:
        print('Максимальная концентрация этилацетата составляет 1,0238 моль/л. Выберите меньшую концентрацию.')
        return None

    while abs(current_concentration - target_concentration) > molarity_tolerance:
        # Цикл будет идти до тех пор, пока разница между текущей и требуемой концентрацией не станет пренебрежимо мала

        flask_count += 1
        v_take = max_flask_volume * target_concentration / current_concentration  # Объем раствора, который нужно взять
        v_take = round(v_take, 10)

        if v_take < minimum_volume:  # Можно взять только минимально допустимый объем из-за ограничений
            v_take = minimum_volume

        # Приведение отбираемого объема к такому, который делится на минимальный объем (цену деления)
        if round(v_take % minimum_volume, 10) != 0 and round(v_take % minimum_volume, 10) != minimum_volume:
            v_take = round(round(v_take // minimum_volume, 10) * minimum_volume + minimum_volume, 10)

        if v_take >= max_flask_volume:
            break  # Значит текущая концентрация меньше требуемой

        if flask_count == 1:
            steps.append(f'Возьмите {v_take} мл исходного раствора и поместите его в новый флакон')
        else:
            steps.append(f'Возьмите {v_take} мл раствора из предыдущего флакона и поместите его в новый флакон')

        steps.append(f'Добавьте {round((max_flask_volume - v_take), 10)} мл воды во флакон')
        current_concentration = v_take * current_concentration / max_flask_volume  # Расчет текущей концентрации

    margin_of_error = abs(1 - target_concentration / current_concentration) * 100  # Получившаяся погрешность в %

    print(f'Вам потребуется пузырьков: {flask_count} объемом {max_flask_volume} мл')
    for step in steps:
        print(step)
    print(f'Концентрация составит: {current_concentration} моль/л')
    print(f'Погрешность разбавления составила: {round(margin_of_error, 3)} %')

    return steps, margin_of_error
