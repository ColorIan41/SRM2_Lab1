import numpy as np
import matplotlib.pyplot as plt


# ln(x+2)-x^4+0,5=0

# Локалізуємо корені рівняння
def func1(x):
    return x ** 4


def func2(x):
    return np.log(x + 2) + 0.5


# Задамо діапазон значень x
x_values = np.linspace(-1, 3, 400)

# Обчислимо значення функцій на заданих значеннях x
left_values = func2(x_values)
right_values = func1(x_values)

# Побудуємо графік
plt.figure(figsize=(10, 6))
plt.plot(x_values, left_values, label='ln(x + 2) + 0.5', color='blue')
plt.plot(x_values, right_values, label='x⁴', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title("")
plt.legend()
plt.grid(True)
plt.show()
