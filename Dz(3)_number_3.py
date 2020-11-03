import numpy as np
import matplotlib.pyplot as plt

a = np.zeros((15, 28))
a[2: -2, 1] = 1;
a[2, 2:6] = 1
a[2: 7, 6] = 1;
a[7: -2, 7] = 1
a[7, 2:7] = 1;
a[-3, 2:7] = 1
a[2: -2, 10] = 1;
a[2: -2, 14] = 1
a[2: -2, 18] = 1;
a[-3, 10:19] = 1
a[-3, 21:27] = 1;
a[-8, 21:27] = 1
a[-13, 21:27] = 1;
a[2: -2, 26] = 1
plt.imshow(a)
plt.show()
print(np.linalg.matrix_rank(a))
u, s, w = np.linalg.svd(a)
S = np.zeros_like(a, dtype=float)
S[np.diag_indices(min(a.shape))] = s
S_4 = S[:, :4]
w_4 = w[:4, :]
plt.imshow(u @ S_4 @ w_4)
plt.show()
S_3 = S[:, :3]
w_3 = w[:3, :]
plt.imshow(u @ S_3 @ w_3)
plt.show()
S_2 = S[:, :2]
w_2 = w[:2, :]
plt.imshow(u @ S_2 @ w_2)
plt.show()
S_1 = S[:, :1]
w_1 = w[:1, :]
plt.imshow(u @ S_1 @ w_1)
plt.show()
