import os
import xlwings as xw
import pandas as pd

# 全路径
full_path = os.getcwd() + '/files'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)

# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))
# 获取指定工作薄中所有工作表
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

        # 统计 库存量 的最大值
        max_val = t_values['库存量'].max()
        # 统计 库存量 的最小值
        min_val = t_values['库存量'].min()
        # 在当前指定单元格写入指定文本内容
        i.range('I1').value = '最大库存量'
        # 在当前指定单元格写入统计出的最大值
        i.range('J1').value = max_val
        # 在当前指定单元格写入指定文本内容
        i.range('I2').value = '最小库存量'
        # 在当前指定单元格写入统计出的最小值
        i.range('J2').value = min_val
    # 保存工作薄
    workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
