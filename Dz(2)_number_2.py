import numpy as np
import matplotlib.pyplot as plt

a = np.array([[3, 0], [0, -2]])
u, s, w = np.linalg.svd(a)
S = np.zeros_like(a, dtype=float)
S[np.diag_indices(min(a.shape))] = s
print(u)
print(S)
print(w)
plt.arrow(0, 0, *(u[:, 0] * s[0]), color='gold')
plt.arrow(0, 0, *(u[:, 1] * s[1]), color='black')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
phi = np.arange(0, 2 * np.pi, 0.01)
plt.scatter(s[0] * np.cos(phi), s[1] * np.sin(phi), s=5)
plt.show()
plt.arrow(0, 0, *(w[:, 0]), color='gold')
plt.arrow(0, 0, *(w[:, 1]), color='black')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
phi = np.arange(0, 2 * np.pi, 0.001)
plt.scatter(s[1] * np.cos(phi), s[0] * np.sin(phi), s=5)
plt.show()
