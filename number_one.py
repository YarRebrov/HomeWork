import math
import numpy as np

print("Введите аргумент интеграла:")
a = float(input())
I_0 = np.log(abs(a + 1)) - np.log(abs(a))
print(I_0)
print("Введите рекуррентный номер интеграла")
k = int(input())
I = I_0
for i in range(0, k):
    I = 1 / (i + 1) - a * I
    print("I_", i+1, " = ", I, sep="", end="; ")
print()
print("Результат = ", I)
