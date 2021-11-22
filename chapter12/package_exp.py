import pandas as pd

# 从工作薄中读取要进行相关性分析的数据
df = pd.read_excel('商品信息.xlsx', index_col='商品名称')
# 计算任意两个变量之间的相关系数
corr_result = df.corr()['库存量']
# 输出计算出的相关系数
print(f'相关系数结果：\n{corr_result}')
# 等待输入
input()
