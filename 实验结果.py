import numpy as np
# 输入实验时间
t1 = 26.73
t2 = 70
t3 = 60

# 计算速率z
z1 = (0.0016/2)/t1
z2 = (0.002/2)/t2
z3 = (0.0016/2)/t3


# 给定的数据点
x = np.array([0.08, 0.05, 0.08])
y = np.array([0.08, 0.10, 0.04])
z = np.array([z1, z2, z3])

# 取对数
ln_x = np.log(x)
ln_y = np.log(y)
ln_z = np.log(z)

# 构建矩阵 M 和向量 B
M = np.column_stack((np.ones_like(ln_x), ln_x, ln_y))
B = ln_z

# 求解线性方程组 M * [A, m, n]^T = B
A_m_n = np.linalg.solve(M, B)

# 提取 A, m, n
A, m, n = A_m_n

# 计算 k
k = np.exp(A)

print(f"k = {k}")
print(f"m = {m}")
print(f"n = {n}")
