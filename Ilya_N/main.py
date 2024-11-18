def calculate_dilution(target_concentration: float) -> dict | None:
    """
    Рассчитывает пошаговое разбавление раствора этилацетата до целевой концентрации.

    Args:
        target_concentration (float): Целевая концентрация раствора в моль/л.

    Returns:
        dict: Словарь с результатами расчета, содержащий:
            flask_count (int): количество необходимых флаконов.
            max_flask_volume (float): объем каждого флакона в мл.
            steps (list): список строк с пошаговыми инструкциями разбавления.
            current_concentration (float): итоговая концентрация раствора в моль/л.
            margin_of_error (float): погрешность разбавления в процентах.
        None: если целевая концентрация превышает исходную концентрацию раствора
    """
    mass_fraction = 99.8  # Массовая доля этилацетата (%)
    density = 0.902  # Исходная плотность (г/мл)
    max_flask_volume = 10  # Максимальный объем флакона (мл)
    ether_molar_mass = 88.1  # Молярная масса этилацетата (г/моль)
    tolerance = 0.25  # Погрешность разбавления (%)
    minimum_volume = 1  # Минимальный объем, который можно набрать (цена деления) (мл)

    initial_concentration = density * mass_fraction * 10 / ether_molar_mass  # Исходная концентрация этилацетата(моль/л)
    molarity_tolerance = (tolerance / 100) * target_concentration  # Допустимая погрешность разбавления (моль/л)

    current_concentration = initial_concentration
    steps = []
    flask_count = 0  # Количество флаконов

    if target_concentration > initial_concentration:
        return None

    while abs(current_concentration - target_concentration) > molarity_tolerance:
        # Цикл будет идти до тех пор, пока разница между текущей и требуемой концентрацией не станет пренебрежимо мала

        v_take = max_flask_volume * target_concentration / current_concentration  # Объем раствора, который нужно взять
        v_take = round(v_take, 10)

        if v_take < minimum_volume:  # Можно взять только минимально допустимый объем из-за ограничений
            v_take = minimum_volume

        # Приведение отбираемого объема к такому, который делится на минимальный объем (цену деления)
        if round(v_take % minimum_volume, 10) != 0 and round(v_take % minimum_volume, 10) != minimum_volume:
            v_take = round(round(v_take // minimum_volume, 10) * minimum_volume + minimum_volume, 10)

        if v_take >= max_flask_volume:
            break  # Значит текущая концентрация меньше требуемой

        flask_count += 1

        if flask_count == 1:
            steps.append(f'Возьмите {v_take} мл исходного раствора и поместите его в новый флакон')
        else:
            steps.append(f'Возьмите {v_take} мл раствора из предыдущего флакона и поместите его в новый флакон')

        steps.append(f'Добавьте {round((max_flask_volume - v_take), 10)} мл воды во флакон')
        current_concentration = v_take * current_concentration / max_flask_volume  # Расчет текущей концентрации

    margin_of_error = round(abs(1 - target_concentration / current_concentration) * 100, 3)
    # Получившаяся погрешность в %

    return {'flask_count': flask_count, 'max_flask_volume': max_flask_volume, 'steps': steps,
            'current_concentration': current_concentration,
            'margin_of_error': margin_of_error}


print('Введите требуемую концентрацию раствора в моль/л в формате вещественного числа со знаком точка')
while True:
    concentration = input()
    try:
        concentration = float(concentration)
    except ValueError:
        print(
            "Неверный формат. Введите требуемую концентрацию раствора в моль/л "
            "в формате вещественного числа со знаком точка")
    else:
        result = calculate_dilution(concentration)
        if result:
            print(f'Вам потребуется пузырьков: {result['flask_count']} объемом {result['max_flask_volume']} мл')
            for step in result['steps']:
                print(step)
            print(f'Концентрация составит: {result['current_concentration']} моль/л')
            print(f'Погрешность разбавления составила: {result['margin_of_error']} %')
            break
        else:
            print('Максимальная концентрация этилацетата составляет 1,0238 моль/л. Выберите меньшую концентрацию.')
            continue
