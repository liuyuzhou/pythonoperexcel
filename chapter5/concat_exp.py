import pandas as pd

first = pd.DataFrame({
         'Name': ['meng', 'zhi', 'wang'],
         'number': ['1001', '1002', '1003'],
         'score': [98, 95, 91]},
         index=[1, 2, 3])
second = pd.DataFrame({
         'Name': ['li', 'zhang', 'ming'],
         'number': ['1001', '1002', '1005'],
         'score': [93, 100, 97]},
         index=[1, 2, 3])
rs = pd.concat([first, second])
print('对象连接：\n{}'.format(rs))

# 通过键参数把特定的键与每个碎片的DataFrame关联起来
rs = pd.concat([first, second], keys=['x', 'y'])
print('使用键参数关联碎片：\n{}'.format(rs))

# 如果想要生成的对象必须遵循自己的索引，请将ignore_index设置为True
rs = pd.concat([first, second], keys=['x', 'y'], ignore_index=True)
print('使生成对象遵循自己的索引：\n{}'.format(rs))

# 如果需要沿axis=1添加两个对象
rs = pd.concat([first, second], axis=1)
print('沿axis设置值添加对象：\n{}'.format(rs))