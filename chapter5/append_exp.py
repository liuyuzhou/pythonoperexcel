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
rs = first.append(second)
print('append函数带一个对象：\n{}'.format(rs))

rs = first.append([second, first])
print('append函数带多个对象：\n{}'.format(rs))