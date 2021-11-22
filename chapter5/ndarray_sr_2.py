import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
nd_s = pd.Series(data, index=[1001, 1002, 1003, 1004])
print('ndarray创建指定索引系列示例：\n{}'.format(nd_s))