import pandas as pd

left = pd.DataFrame({'id': [1, 2, 3],
                     'Name': ['meng', 'zhi', 'wang'],
                     'number': ['1001', '1002', '1003']})
right = pd.DataFrame({'id': [1, 2, 3],
                      'Name': ['li', 'zhang', 'ming'],
                      'number': ['1002', '1003', '1005']})
print('左数据帧：\n{}'.format(left))
print('右数据帧：\n{}'.format(right))
rs = pd.merge(left, right, on='id')
print('由id合并数据帧：\n{}'.format(rs))