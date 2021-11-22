import xlwings as xw
import pandas as pd
import os

# 全路径
full_path = os.getcwd() + '/files'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))
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
        c_data = t_values.reindex(columns=['商品名称', '序号', '商品sku', '库存量',
                                           '销售单价', '商品产地', '商品编号', '生产日期'])
        # 将调整列顺序后的数据合并的创建的DataFrame对象中
        empty_table = empty_table.append(c_data, ignore_index=True)
        # 对指定列进行升序排序，默认排序顺序是升序
        empty_table = empty_table.sort_values(by='库存量')
    select_shopping = '文件夹'
    # 根据指定列筛选数据
    select_value = empty_table[empty_table['商品名称'] == select_shopping]
    # 创建一个新的工作薄
    new_workbook = xw.books.add()
    # 异常捕获
    try:
        # 在工作薄中新增工作表，以select_shopping值命名工作表
        new_worksheet = new_workbook.sheets.add(select_shopping)
        # 在新工作表中写入数据
        new_worksheet['A1'].options(index=False).value = select_value
        # 自动调整工作表的行高和列宽
        new_worksheet.autofit()
        # 保存新工作薄
        new_workbook.save(os.path.join(full_path, f'{select_shopping}.xlsx'))
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
