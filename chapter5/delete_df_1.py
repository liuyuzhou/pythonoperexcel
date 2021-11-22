import pandas as pd

dict_v = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
          'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
          'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(dict_v)
print("初始数据帧:\n{}".format(df))

del df['one']
print("使用删除函数删除第一列:\n{}".format(df))

df.pop('two')
print("使用POP函数删除一列:\n{}".format(df))