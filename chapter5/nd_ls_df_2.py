import pandas as pd

data = {'Name': ['xiao meng', 'xiao zhi', 'xiao qiang', 'xiao wang'], 'Age': [20, 21, 23, 22]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)