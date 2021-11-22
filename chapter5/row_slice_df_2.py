import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
print('初始数据帧：\n{}'.format(df))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df.append(df2)
print('添加新行后的数据帧：\n{}'.format(df))