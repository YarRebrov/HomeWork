import math
import numpy as np


def integral(a, n):
    res = 0
    if n > 0:
        res = 1.0 / n - a * integral(a, n - 1)
    else:
        res = np.log(abs(a + 1)) - np.log(abs(a))
    print("I_", n,  " = ", res, sep="", end="; ")
    return res


print("Введите аргумент интеграла:")
alpha = float(input())
print("Введите рекуррентный номер интеграла")
k = int(input())
print("\nРезультат:", integral(alpha, k))
