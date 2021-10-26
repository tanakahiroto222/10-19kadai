import numpy as np
from scipy import linalg
#1
a1 = np.array([[2,1,3],[4,5,4],[3,1,5]])
b1 = np.array([0,-2,1])
print("(1)")
print(a1)
print(b1)
lu1, p1 = linalg.lu_factor(a1)
print("LU分解で解くと")
print(linalg.lu_solve((lu1,p1), b1))
print("逆行列を用いると")
print(np.linalg.inv(a1) @ b1)
print()
#2
a2 = np.array([[8,16,24,32],[2,7,12,17],[6,17,32,59],[7,22,46,105]])
b2 = np.array([160,70,198,291])
print("(2)")
print(a2)
print(b2)
lu2, p2 = linalg.lu_factor(a2)
print("LU分解で解くと")
print(linalg.lu_solve((lu2,p2), b2))
print("逆行列を用いると")
print(np.linalg.inv(a2) @ b2)
