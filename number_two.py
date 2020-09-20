import cmath
import math


def find_roots(b, c):
    if (-10 ** 4 <= b <= 10 ** 4) and (-10 ** 4 <= c <= 10 ** 4):
        D = b ** 2 - 4 * c
        if D >= 0:
            return -b / 2 + math.sqrt(D) / 2, -b / 2 - math.sqrt(D) / 2
        else:
            return -b / 2 + cmath.sqrt(D) / 2, -b / 2 - cmath.sqrt(D) / 2
    if c >= 0:
        if (((2 * math.sqrt(c)) / b) >= (-1)) and (
                ((2 * math.sqrt(c)) / b) <= (1)):
            d = math.sqrt(1 - ((2 * math.sqrt(c)) / b)) * math.sqrt(
                1 + ((2 * math.sqrt(c)) / b))
            return (-b / 2) * (1 + d), c / ((-b / 2) * (1 + d))
        else:
            d = cmath.sqrt(1 - ((2 * cmath.sqrt(c)) / b)) * cmath.sqrt(
                1 + ((2 * cmath.sqrt(c)) / b))
            return (-b / 2) * (1 + d), c / ((-b / 2) * (1 + d))
    else:
        d = cmath.sqrt(1 - ((2 * cmath.sqrt(c)) / b)) * cmath.sqrt(
            1 + ((2 * cmath.sqrt(c)) / b))
        return (-b / 2) * (1 + d), c / ((-b / 2) * (1 + d))


b, c = map(float, input().split())
print(find_roots(b, c))
