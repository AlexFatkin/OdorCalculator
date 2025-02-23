import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Исходные данные
x_data = np.array(
    [0.500, 0.68, 0.9, 1.188, 1.568, 2.07, 2.732, 3.607, 4.761, 6.284, 8.295,
     10.95, 14.454, 19.079, 25.184, 33.243, 43.881, 57.923, 76.458, 100.925,
     133.221, 175.852, 232.125, 306.404, 404.454, 533.879, 704.72, 930.231, 10238]
)

flask_amount = 36.64
y = []
for i in range(len(x_data) - 1):
    y.append(round(1 / flask_amount * (i+1), 3))

y.append(1)
x_data = np.array(x_data)
y_data = np.array(y)

# Подгонка логарифмического сплайна
spline = UnivariateSpline(np.log(x_data), y_data, s=0.1)  # s - параметр сглаживания

# Создание точек для построения графика
x_fit = np.linspace(min(x_data), max(x_data), 1000)
y_fit = spline(np.log(x_fit))

# Расчет R-квадрат и MSE
y_pred = spline(np.log(x_data))
r_squared = 1 - np.sum((y_data - y_pred)**2) / np.sum((y_data - np.mean(y_data))**2)
mse = np.mean((y_data - y_pred)**2)

# Создание фигуры с двумя подграфиками
plt.style.use('default')
fig = plt.figure(figsize=(15, 8))
gs = GridSpec(1, 2, width_ratios=[1.5, 1])

# Первый график - данные и подгонка
ax1 = fig.add_subplot(gs[0])
ax1.scatter(x_data, y_data, label='Экспериментальные данные', alpha=0.6, color='#1f77b4')

# Разделение графика на две части
inside_range = (x_fit >= 0.5) & (x_fit <= 1000)
outside_range = ~inside_range

# Построение графика внутри диапазона
ax1.plot(x_fit[inside_range], y_fit[inside_range], 'r-', label='Логарифмический сплайн', linewidth=2)

# Построение графика вне диапазона
ax1.plot(x_fit[outside_range], y_fit[outside_range], 'r--', linewidth=2)

ax1.set_xlabel('C мкмоль/мл', fontsize=12)
ax1.set_ylabel('D интенсивность', fontsize=12)
ax1.set_title('Поиск параметров для логарифмического сплайна', fontsize=14, pad=20)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Второй график - информация
ax2 = fig.add_subplot(gs[1])
ax2.axis('off')

# Добавление текстовой информации
info_text = "ЛОГАРИФМИЧЕСКИЙ СПЛАЙН\n\n"
info_text += "Статистика:\n"
info_text += f"R² = {r_squared:.4f}\n"
info_text += f"MSE = {mse:.6f}\n\n"


# Добавление текстового блока
props = dict(boxstyle='round', facecolor='white', alpha=0.9)
ax2.text(0, 0.95, info_text, transform=ax2.transAxes,
         verticalalignment='top', bbox=props, fontsize=11)

plt.tight_layout()
plt.show()

# Вывод дополнительной информации в консоль
print("\nПодробный анализ логарифмического сплайна:")
print("-" * 50)
print(f"Качество подгонки:")
print(f"R-квадрат: {r_squared:.4f}")
print(f"Среднеквадратичная ошибка: {mse:.6f}")