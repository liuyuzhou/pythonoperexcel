import numpy as np

# 默认为浮点数
one_df = np.ones(5)
print('默认为float类型：\n{}'.format(one_df))

# 自定义为int类型
one_int = np.ones((5,), dtype=np.int)
print('自定义为int类型：\n{}'.format(one_int))
