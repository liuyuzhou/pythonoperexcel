import numpy as np

ar_np = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('初始数组：\n{}'.format(ar_np))

# 从某个索引处开始切割
print('从数组索引ar_np[1:]处开始切割:\n{}'.format(ar_np[1:]))

print('从数组索引ar_np[1:]处开始切割,到ar_np[2]出结束:\n{}'.format(ar_np[1:2]))

print('从数组索引ar_np[0:]处开始切割,到ar_np[2]出结束，步长为2:\n{}'.format(ar_np[0:3:2]))