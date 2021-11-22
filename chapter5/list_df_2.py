import pandas as pd

data = [['xiao meng', 20], ['xiao zhi', 21], ['xiao qiang', 23]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)