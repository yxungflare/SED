import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Данные для антивируса и межсетевого экрана (в часах)
data_antivirus = [100, 200, 150, 300, 250]
data_firewall = [120, 180, 220, 280, 200]

# Объединяем данные времени до отказа для обоих компонентов
data_system = data_antivirus + data_firewall

# Оцениваем параметры распределения Вейбулла для системы
shape_system, loc_system, scale_system = weibull_min.fit(data_system, loc=0)

# Генерируем данные для графика PDF для системы
x_system = np.linspace(0, max(data_system), 100)
pdf_system = weibull_min.pdf(x_system, shape_system, loc_system, scale_system)

# График PDF распределения Вейбулла для системы
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(x_system, pdf_system, 'r-', lw=2)
plt.xlabel('Время до отказа (часы)')
plt.ylabel('Плотность вероятности')
plt.title('PDF распределения Вейбулла для системы')

# График функции надежности для системы (Survival Function)
sf_system = 1 - weibull_min.cdf(x_system, shape_system, loc_system, scale_system)

plt.subplot(1, 2, 2)
plt.plot(x_system, sf_system, 'b-', lw=2)
plt.xlabel('Время до отказа (часы)')
plt.ylabel('Функция надежности')
plt.title('График функции надежности для системы')

plt.tight_layout()
plt.show()
