import os
import xlwings as xw
import pandas as pd

# 全路径
full_path = os.getcwd() + '/files'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))
# 异常捕获
try:
    # 取得指定工作薄中的所有工作表
    sheet_list = workbook.sheets
    # 遍历工作表
    for i in sheet_list:
        # 当前工作表是否为指定工作表，不是继续循环
        if i.name != '基本信息':
            continue

        # 读取当前工作表数据
        table_value = i.range('A1').expand().options(pd.DataFrame).value
        # 若是空的工作表，则继续循环
        if table_value.empty:
            continue

        # 设置图表的位置和尺寸
        chart = i.charts.add(left=200, top=0, width=355, height=211)
        # 读取工作表中要制作图表的数据
        chart.set_source_data(i['A1'].expand())
        # 制作条形图
        chart.chart_type = 'bar_clustered'
    # 保存工作薄
    workbook.save(os.path.join(full_path, '条形图.xlsx'))
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()