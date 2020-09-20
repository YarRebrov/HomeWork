import math
import numpy as np

print("Введите аргумент интеграла:")
a = float(input())
I_0 = 0
print("Введите рекуррентный номер интеграла")
k = int(input())
I = I_0
i = k + 20
while i > k:
    I = 1 / (a * i) - I / a
    print("I_", i, " = ", I, sep="", end="; ")
    i = i - 1
print()
print("Результат = ", I)
