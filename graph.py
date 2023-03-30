from matplotlib import pyplot as plt

# Задаем данные для графиков
szi = ['"ПАК" Соболь', 'SecretDisk']
reliability = [0.8, 0.9]
price = [62000, 50000]

# Строим график зависимости надежности от цены
plt.bar(szi, price)
plt.title('Зависимость надежности от цены')
plt.xlabel('СЗИ')
plt.ylabel('Цена, руб.')
plt.savefig('graph1.png')

# Строим столбчатую диаграмму
plt.bar(szi, reliability)
plt.title('Надежность СЗИ')
plt.xlabel('СЗИ')
plt.ylabel('Надежность')
plt.ylim(0, 1) # Установка ограничений по оси y
plt.savefig('graph2.png')