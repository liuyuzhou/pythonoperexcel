import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df.append(df2)
print('初始数据帧：\n{}'.format(df))

df = df.drop(0)
print('删除包含标签0后的数据帧：\n{}'.format(df))