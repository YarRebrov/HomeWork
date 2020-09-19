import math
import numpy as np

a=float(input())
I_0=np.log(abs(a+1))-np.log(abs(a))
k=int(input())
I=I_0
for i in range(0,k):
    I=1/(i+1)-a*I
print(I)

