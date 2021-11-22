import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
nd_s = pd.Series(data)
print('ndarray创建不指定索引系列示例：\n{}'.format(nd_s))