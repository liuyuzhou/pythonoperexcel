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
    # 文件遍历
    for i in sheet_list:
        # 读取当前工作表的数据
        t_values = i.range('A1').expand('table').options(pd.DataFrame).value
        # 如果t_values为None，则继续循环
        if t_values.empty:
            continue

        # 对指定列求和，如库存量
        sum_val = t_values['库存量'].sum()
        # 将求和结果写入指定单元格
        i.range('J1').value = sum_val
    # 保存工作薄
    workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
