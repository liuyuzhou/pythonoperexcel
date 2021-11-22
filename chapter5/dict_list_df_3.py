import pandas as pd

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

df_1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df_1)

df_2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df_2)