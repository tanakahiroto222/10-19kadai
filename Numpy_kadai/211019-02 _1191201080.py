import numpy as np
#1
a = np.array([[3,5],[4,7]])
print("(1)")
print(a)
print("これの逆行列は")
print(np.linalg.inv(a))
print("これらの行列積は")
print(a @ np.linalg.inv(a))
print()
#2
b = np.array([[2,1,3],[4,5,4],[3,1,5]])
print("(2)")
print(b)
print("これの逆行列は")
print(np.linalg.inv(b))
print("これらの行列積は")
print(b @ np.linalg.inv(b))