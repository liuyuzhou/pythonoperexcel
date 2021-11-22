import pandas as pd

left = pd.DataFrame({'id': [1, 2, 3],
                     'Name': ['meng', 'zhi', 'wang'],
                     'number': ['1001', '1002', '1003']})
right = pd.DataFrame({'id': [1, 2, 3],
                      'Name': ['li', 'zhang', 'ming'],
                      'number': ['1001', '1002', '1005']})
rs = pd.merge(left, right, on=['id', 'number'])
print('由多个键合并数据帧：\n{}'.format(rs))