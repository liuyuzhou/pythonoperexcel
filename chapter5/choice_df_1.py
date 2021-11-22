import pandas as pd

dict_v = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
          'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dict_v)
print(df['one'])