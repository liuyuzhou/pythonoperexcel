import pandas as pd

dict_v = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
          'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(dict_v)

df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("根据传递的系列添加新列:\n{}".format(df))

df['four'] = df['one'] + df['three']
print("使用存在的数据帧添加新列:\n{}".format(df))