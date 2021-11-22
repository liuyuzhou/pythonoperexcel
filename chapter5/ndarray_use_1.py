import numpy as np

v_list = [1, 2, 3]
# 一维列表转一维数组
v_list_np = np.array(v_list)
print(f'列表对象 v_list：{v_list}')
print(f'v_list的数据类型为：{type(v_list)}')
print(f'数组对象 v_list_np：{v_list_np}')
print(f'v_list_np的数据类型为：{type(v_list_np)}')