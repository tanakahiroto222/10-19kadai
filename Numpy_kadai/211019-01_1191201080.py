import numpy as np

a = np.random.randint(0, 10, 10)
b = np.random.randint(0, 10, 10)
print(a)
print(b)
same = a==b
print("上２つの配列で同じ番号で値も等しいのは", a[same])
print("その個数は、", same.sum())