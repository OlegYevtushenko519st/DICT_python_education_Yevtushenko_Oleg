import numpy as np
import matplotlib.pyplot as plt

xi = np.array([1, 2, 3])
yi = np.array([2, 1, 3])

a = 5
b = 27/2
#Створюємо масив значень
x = np.linspace(0,2,10)
#Обчисляем ответы
y = a*x*b
#Побудова графика
plt.plot(x, y, label='Апроксимаційний поліном:')
plt.scatter(xi, yi, color='red', label='Ваші дані', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
# #Відображення графика
plt.show()