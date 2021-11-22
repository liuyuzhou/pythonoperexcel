import pandas as pd

un_sorted_df = pd.DataFrame({'col1': [2, 1, 1, 1], 'col2': [1, 3, 2, 4]})
sorted_df = un_sorted_df.sort_values(by=['col1', 'col2'])
print(sorted_df)