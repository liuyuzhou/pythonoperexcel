import numpy as np

# 创建ndarray对象
ar_np = np.arange(10)
# 从索引 2 开始到索引 7 停止，间隔为2
s = slice(2, 7, 2)
print(ar_np[s])