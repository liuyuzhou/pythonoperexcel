import numpy as np

# 创建ndarray对象
ar_np = np.arange(10)
print('数组ar_np为：{}'.format(ar_np))

s_rs = ar_np[2]
print('数组ar_np索引2：{}'.format(s_rs))

# 从索引2开始
s_rs = ar_np[2:]
print('数组ar_np从索引2开始：{}'.format(s_rs))

# 从索引2开始，到索引7停止
s_rs = ar_np[2:7]
print('数组ar_np从索引2开始，到索引7停止：\n{}'.format(s_rs))

# 从索引2开始，到索引7停止，间隔为2
s_rs = ar_np[2: 7: 2]
print('数组ar_np从索引2开始，到索引7停止，间隔为2：\n{}'.format(s_rs))