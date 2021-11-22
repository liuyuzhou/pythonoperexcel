import xlwings as xw
import pandas as pd
import os

# 全路径
full_path = os.getcwd() + '/files'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品分类.xlsx'))
# 异常捕获
try:
    # 取得工作薄中所有工作表
    sheet_list = workbook.sheets
    # 创建一个空的DataFrame
    empty_table = pd.DataFrame()
    # 遍历工作表
    for i, j in enumerate(sheet_list):
        # 当前当前工作表的数据
        t_values = j.range('A1').options(pd.DataFrame, header=1, index=False,
                                         expand='table').value
        # 调整列的顺序
        c_data = t_values.reindex(columns=['商品产地', '序号', '商品sku', '商品名称',
                                           '销售单价', '商品编号', '生产日期', '库存量'])
        # 将调整列顺序后的数据合并的创建的DataFrame对象中
        empty_table = empty_table.append(c_data, ignore_index=True)
    # 根据指定列筛选数据
    empty_table = empty_table.groupby('商品产地')
    # 创建一个新的工作薄
    new_workbook = xw.books.add()
    # 异常捕获
    try:
        # 遍历筛选的数据，idx对应商品产地，group对应物品所有明细数据
        for idx, group in empty_table:
            # 在工作薄中新增工作表，以商品产地命名工作表
            new_worksheet = new_workbook.sheets.add(idx)
            # 在新工作表中写入数据
            new_worksheet['A1'].options(index=False).value = group
            # 获取当前工作表数据区域右下角的单元格
            last_cell = new_worksheet['A1'].expand('table').last_cell
            # 获取数据区域最后一行的行号
            last_row = last_cell.row
            # 获取数据区域最后一列的列号
            last_column = last_cell.column
            # 将数据区域最后一列的列号（数字）转换为该列的列标（字母）
            last_column_letter = chr(64 + last_column)
            # 获取数据区域右下角单元格下方的单元格的位置
            sum_cell_name = f'{last_column_letter}{last_row + 1}'
            # 获取数据区域右下角单元格的位置
            sum_last_row_name = f'{last_column_letter}{last_row}'
            # 根据单元格位置构造Excel公式，对库存量进行求和
            formula = f'SUM({last_column_letter}2:{sum_last_row_name})'
            # 将求和公式写入数据区域右下角单元格下方的单元格中
            new_worksheet[sum_cell_name].formula = formula
            # 自动调整工作表的行高和列宽
            new_worksheet.autofit()
        # 保存新工作薄
        new_workbook.save(os.path.join(full_path, '商品产地.xlsx'))
    # 不管前面代码执行是否发生异常，都执行该语句块的语句
    finally:
        # 关闭新工作薄
        new_workbook.close()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
