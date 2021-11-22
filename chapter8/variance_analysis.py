import os
import pandas as pd
import xlwings as xw
# 导入 ols() 函数
from statsmodels.formula.api import ols
# 导入 anova_lm() 函数
from statsmodels.stats.anova import anova_lm

# 全路径
full_path = os.getcwd() + '/files'
# 读取指定工作薄中的数据
df = pd.read_excel(os.path.join(full_path, '方差分析.xlsx'))
# 选取指定列的数据用于分析
df = df[['A型号', 'B型号', 'C型号', 'D型号', 'E型号']]
# 将列名转换为列数据，重构 DataFrame
df_melt = df.melt()
# 重命名列
df_melt.columns = ['Treat', 'Value']
# 创建一个空 DataFrame 用于汇总数据
df_describe = pd.DataFrame()
# 计算指定列的平均值、最大值和最小值
df_describe['A型号'] = df['A型号'].describe()
# 计算指定列的平均值、最大值和最小值
df_describe['B型号'] = df['B型号'].describe()
# 计算指定列的平均值、最大值和最小值
df_describe['C型号'] = df['C型号'].describe()
# 计算指定列的平均值、最大值和最小值
df_describe['D型号'] = df['D型号'].describe()
# 计算指定列的平均值、最大值和最小值
df_describe['E型号'] = df['E型号'].describe()
# 对样本数据进行最小二乘线性拟合计算
model = ols('Value~C(Treat)', data=df_melt).fit()
# 对样本数据进行方差分析
anova_table = anova_lm(model, typ=3)
# 开启Excel程序
app = xw.App(visible=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '方差分析.xlsx'))
# 异常捕获
try:
    # 取得指定工作薄中的所有工作表
    sheet_list = workbook.sheets
    # 从所有工作表中取得指定名称的工作表
    select_sheet = [sheet for sheet in sheet_list if sheet.name == '单因素方差分析']
    # 从筛选结果集中取得第一个工作表
    worksheet = select_sheet[0]
    # 将计算出的平均值、最大值和最小值等数据转置行列并写入工作表
    worksheet.range('H2').value = df_describe.T
    # 在工作表中写入指定文本内容
    worksheet.range('H14').value = '方差分析'
    # 将方差分析的结果写入工作表
    worksheet.range('H15').value = anova_table
    # 保存工作薄
    workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
