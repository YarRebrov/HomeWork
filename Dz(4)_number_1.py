import math
import matplotlib.pyplot as plt
import numpy as np

n = 1000
a = np.random.normal(0, 1, (n, n))
A = a + a.T
eigenvalue = np.linalg.eigvalsh(A)
S = np.zeros_like(A, dtype=float)
S[np.diag_indices(min(A.shape))] = eigenvalue
print(eigenvalue)
print(S)
plt.hist(eigenvalue, bins=30)
plt.show()
