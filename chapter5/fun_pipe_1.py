import pandas as pd
import numpy as np


def add_num(ele1, ele2):
    return ele1 + ele2


df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print('初始数组：\n{}'.format(df))
print('调用函数后的数组：\n{}'.format(df.pipe(add_num, 2)))