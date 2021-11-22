import os
import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw

# 全路径
full_path = os.getcwd() + '/files'
# 读取指定工作薄中的数据
df = pd.read_excel(os.path.join(full_path, '方差分析.xlsx'))
# 选取指定列的数据用于分析
df = df[['A型号', 'B型号', 'C型号', 'D型号', 'E型号']]
# 创建绘图窗口
figure = plt.figure()
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制箱形图并删除网格线
df.boxplot(grid=False)
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
    # 将绘制的箱形图插入工作表
    worksheet.pictures.add(figure, name='', update=True, left=500, top=10)
    # 保存工作薄
    workbook.save(os.path.join(full_path, '箱形图.xlsx'))
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
