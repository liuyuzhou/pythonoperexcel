import os
import xlwings as xw
import pandas as pd

# 全路径
full_path = os.getcwd() + '/files'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))
# 取得指定工作薄中的所有工作表
sheet_list = workbook.sheets
# 异常捕获
try:
    # 遍历工作表
    for i in sheet_list:
        # 读取当前工作表的数据
        t_values = i.range('A1').expand('table')
        # 若 t_values 为空，继续循环
        if not t_values:
            continue

        # 使用选中的单元格区域中的数据创建一个DataFrame
        table_data = t_values.options(pd.DataFrame).value
        # 如果t_values为None，则继续循环
        if table_data.empty:
            continue

        # 对指定列求和，如库存量
        sum_val = table_data['库存量'].sum()
        # 获取指定列（库存量）的列号
        column = t_values.value[0].index('库存量') + 1
        # 获取数据区域最后一行的行号
        row = t_values.shape[0]
        # 将求和结果写入指定列（库存量）最后一个单元格下方的单元格中
        i.range(row + 1, column).value = sum_val
    # 保存工作薄
    workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
