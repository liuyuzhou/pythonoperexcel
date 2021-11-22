import os
import xlwings as xw
import pandas as pd

# 全路径
full_path = os.getcwd() + '/files'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)

# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))
# 取得指定工作薄中所有工作表
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

        # 用读取的数据制作数据透视表
        pivot_table = pd.pivot_table(t_values, values='库存量', index='商品产地',
                                     columns='商品名称', aggfunc='sum', fill_value=0,
                                     margins=True, margins_name='总库存')
        # 将制作的数据透视表写入当前工作表
        i.range('J1').value = pivot_table
    # 保存工作薄
    workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
