import os
import xlwings as xw

# 全路径
full_file = os.getcwd() + '/files\\商品信息.xlsx'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开指定工作薄
workbook = app.books.open(full_file)
# 遍历工作薄中所有工作表
for i in workbook.sheets:
    # 在工作表中选择要调整的单元格区域
    value = i.range('A1').expand('table')
    # 对选中的单元格的列宽进行调整
    value.column_width = 10
    # 对选中单元格的高度进行调整
    value.row_height = 15
# 保存当前工作薄
workbook.save()
# 关闭当前工作薄
workbook.close()
# 退出Excel程序
app.quit()
