import numpy as np
import matplotlib.pyplot as plt


def f(x1, x2):
 inner1 = np.sin(((16/15) * x1) - 1) + (np.sin(((16/15) * x1) - 1))**2 + (1/50) * np.sin(4 * (((16/15) * x1) - 1))
 inner2 = np.sin(((16/15) * x2) - 1) + (np.sin(((16/15) * x2) - 1))**2 + (1/50) * np.sin(4 * (((16/15) * x2) - 1))
 return 0.6 + inner1 + inner2

#Считаем тестовую точку
x10 = 0.45834282
x20 = 0.45834282
y0 = f(x10, x20)

x1_min, x1_max = -1.0, 1.0
x2_min, x2_max = -1.0, 1.0
step = 0.01

#Создаём массивы координат и двумерные матрицы
x1_values = np.linspace(x1_min, x1_max, round((x1_max - x1_min) / step) + 1)
x2_values = np.linspace(x2_min, x2_max, round((x2_max - x2_min) / step) + 1)
X1, X2 = np.meshgrid(x1_values, x2_values)
Y = f(X1, X2)

#Создаём фигуру с графиками
fig = plt.figure(figsize=(12, 10))

#Тестовая точка
fig.suptitle(f'Тестовая точка: x1={x10}, x2={x20} | y=f(x10, x20) = {y0:.6f}', fontsize=13)

#Трехмерная поверхность
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Y, cmap='viridis')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y=f(x1, x2)')
ax1.set_title('3D поверхность (изометрия)')
fig.colorbar(surf1, ax=ax1, shrink=0.6, pad = 0.15)

#Трехмерная поверхность, вид сверху
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
surf2 = ax2.plot_surface(X1, X2, Y, cmap='viridis')
ax2.view_init(elev=90, azim=-90)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zticks([])
ax2.set_title('Вид сверху')
fig.colorbar(surf2, ax=ax2, shrink=0.6)

#График y = f(x1) при x2 = x20
y_line1 = f(x1_values, x20)
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x1_values, y_line1)
ax3.set_xlabel('x1')
ax3.set_ylabel('y=f(x1, x2)')
ax3.set_title(f'y = f(x1) при x2 = {x20}')
ax3.grid(True)

#График y = f(x2) при x1 = x10
y_line2 = f(x10, x2_values)
ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(x2_values, y_line2)
ax4.set_xlabel('x2')
ax4.set_ylabel('y=f(x1, x2)')
ax4.set_title(f'y = f(x2) при x1 = {x10}')
ax4.grid(True)

plt.show()