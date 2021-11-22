import os
import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt

# 全路径
full_path = os.getcwd() + '/files'
# 从指定工作薄中读取数据
df = pd.read_excel(os.path.join(full_path, '商品信息.xlsx'))
# 创建一个绘图窗口
figure = plt.figure()
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决坐标值为负数时无法正常显示负号的问题
plt.rcParams['axes.unicode_minus'] = False
# 指定列为 x 坐标值
x = df['商品名称']
# 指定列为 y 坐标值
y1 = df['销售单价']
# 指定列为 y 坐标值
y2 = df['库存量']
# 制作柱形图
plt.bar(x, y1, color='black', label='销售单价')
# 设置 y 轴取值范围
plt.ylim(0, 60)
# 添加并设置 x 轴标题
plt.xlabel('商品名称',
           fontdict={'family': 'SimSun', 'color': 'black', 'size': 15},
           labelpad=5)
# 为柱形图添加和设置图例
plt.legend(loc='upper left', fontsize=12)
# 为图表设置双坐标轴
plt.twinx()
# 制作折线图
plt.plot(x, y2, color='black', linewidth=2, label='库存量')
# 设置 y 轴取值范围
plt.ylim(0, 120)
# 为折线图添加和设置图例
plt.legend(loc='upper right', fontsize=12)
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))
# 异常捕获
try:
    # 取得指定工作薄中的所有工作表
    sheet_list = workbook.sheets
    # 从所有工作表中取得指定名称的工作表
    select_sheet = [sheet for sheet in sheet_list if sheet.name == '基本信息']
    # 找到了指定的工作表
    if select_sheet:
        # 从筛选结果集中取得第一个工作表
        worksheet = select_sheet[0]
        # 在工作表中插入柱形图
        worksheet.pictures.add(figure, left=500)
        # 保存工作薄
        workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
