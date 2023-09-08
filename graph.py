import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
from SZI_INFO import data_szi

data_system = []


def data(data_array):
    global data_system
    print('============================================')
    for szi in data_szi:
        if szi in data_array:
            print(data_szi[szi])
            data_system += data_szi[szi]
    print('#####################################')
    print(data_system)
    # Объединяем данные времени до отказа для обоих компонентов


    # Оцениваем параметры распределения Вейбулла для системы
    shape_system, loc_system, scale_system = weibull_min.fit(data_system, loc=0)

    # Генерируем данные для графика PDF для системы
    x_system = np.linspace(0, max(data_system), 100)
    pdf_system = weibull_min.pdf(x_system, shape_system, loc_system, scale_system)

    # Сохраняем график PDF распределения Вейбулла для системы
    plt.figure(figsize=(12, 4))
    plt.plot(x_system, pdf_system, 'r-', lw=2)
    plt.xlabel('Время до отказа (часы)')
    plt.ylabel('Плотность вероятности')
    plt.title('PDF распределения Вейбулла для системы')
    plt.savefig('static/etc/img/graph1.png')  # Сохраняем график как '/static/img/graph1.png'
    plt.close()  # Закрываем текущий график, чтобы создать следующий


    # График функции надежности для системы (Survival Function)
    sf_system = 1 - weibull_min.cdf(x_system, shape_system, loc_system, scale_system)


    # Сохраняем график функции надежности для системы
    plt.figure(figsize=(12, 4))
    plt.plot(x_system, sf_system, 'b-', lw=2)
    plt.xlabel('Время до отказа (часы)')
    plt.ylabel('Функция надежности')
    plt.title('График функции надежности для системы')
    plt.savefig('static/etc/img/graph2.png')  # Сохраняем график как '/static/img/graph2.png'
    plt.close()  # Закрываем текущий график