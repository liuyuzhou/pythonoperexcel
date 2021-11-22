import os
import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt
from sklearn import linear_model

# 全路径
full_path = os.getcwd() + '/files'
# 指定工作表名称
sheet_name = '库存与单价'
# 文件全路径及文件名
full_file_name = os.path.join(full_path, '商品信息.xlsx')
# 从指定工作薄中读取指定工作表数据
df = pd.read_excel(full_file_name, sheet_name=sheet_name)
# 创建一个绘图窗口
figure = plt.figure()
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决坐标值为负数时无法正常显示负号的问题
plt.rcParams['axes.unicode_minus'] = False
# 指定列为 x 坐标值
x = df['库存量']
# 指定列为 y 坐标值
y = df['销售单价']
# 制作散点图
plt.scatter(x, y, s=200, color='black', marker='o', edgecolors='black')
# 添加并设置x轴标题
plt.xlabel('库存量',
           fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 15},
           labelpad=5)
# 添加并设置y轴标题
plt.ylabel('销售单价',
           fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 15},
           labelpad=5)
# 添加并设置图表标题
plt.title('库存与销售单价关系图',
          fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 20},
          loc='center')
# 设置x轴取值范围
plt.xlim(0, 150)
# 设置y轴取值范围
plt.ylim(0, 180)
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))
# 异常捕获
try:
    # 取得指定工作薄中的所有工作表
    sheet_list = workbook.sheets
    # 从所有工作表中取得指定名称的工作表
    select_sheet = [sheet for sheet in sheet_list if sheet.name == sheet_name]
    # 找到了指定的工作表
    if select_sheet:
        # 从筛选结果集中取得第一个工作表
        worksheet = select_sheet[0]
        # 在工作表中插入散点图
        worksheet.pictures.add(figure, name='散点图', update=True, left=300)
        # 保存工作薄
        workbook.save(os.path.join(full_path, '库存与销售单价关系.xlsx'))
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
