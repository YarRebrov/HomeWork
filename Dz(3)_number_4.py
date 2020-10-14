import numpy as np
import matplotlib.pyplot as plt
import math


def coefficients(x, y, m):
    m = m + 1
    if len(x) != len(y):
        print('error')
        return
    A = np.zeros((m, m))
    for k in range(m):
        for j in range(m):
            for i in range(len(x)):
                A[k, j] += x[i] ** (k + j)

    B = np.zeros(m)
    for k in range(m):
        for i in range(len(x)):
            B[k] += y[i] * (x[i] ** k)
    a = np.linalg.solve(A, B)
    return a


def optimal_degree(x, y):
    if len(x) != len(y):
        print('error')
        return
    E1 = np.zeros(1)
    E = np.zeros(len(x))
    for k in range(len(x)):
        d1 = coefficients(x, y, k)
        d1 = d1[::-1]
        f1 = np.poly1d(d1)
        for i in range(len(x)):
            E1[0] += (y[i] - f1(x[i])) ** 2
        E[k] = E1[0]
        E1[0] = 0
    best_m = np.argmin(E)
    return best_m


x = np.linspace(-30, 30, 60)
y = np.sin(x)
m = optimal_degree(x, y)
print("Оптимальная степень полинома = ", optimal_degree(x, y))
d = coefficients(x, y, m)
d = d[::-1]
f = np.poly1d(d)
print("Аппроксимирующая функция выглядит следующим образом:")
print(f)
u = np.polyfit(x, y, len(x) - 1)
F = np.poly1d(u)
plt.grid(True)
plt.plot(x, y, 'o', x, f(x), 'b', x, F(x), 'r')
plt.show()
