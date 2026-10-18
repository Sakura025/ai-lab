import numpy as np

p1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
p2 = np.array([[1], [2], [3]])
print(p1 @ p2)
print((p1 @ p2).shape)

e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(e[1])
print(e[1, :])