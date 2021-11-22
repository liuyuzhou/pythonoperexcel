import os
import xlwings as xw

# 全路径
full_path = os.getcwd() + '/files'
# 取得指定路径下所有文件
file_list = os.listdir(full_path)
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 遍历所有文件
for i in file_list:
    # 若是非xlsx文件或是以~$（已打开）开头的文件，继续循环
    if not i.endswith('.xlsx') or i.startswith('~$'):
        continue

    # 文件全路径及名称
    file_full_path_name = os.path.join(full_path, i)
    # 打开工作薄
    workbook = app.books.open(file_full_path_name)
    # 遍历当前工作薄中的工作表
    for j in workbook.sheets:
        # 在工作表中选择要调整的单元格区域
        value = j.range('A1').expand('table')
        # 对选中的单元格的列宽进行调整
        value.column_width = 15
        # 对选中单元格的高度进行调整
        value.row_height = 25
    # 保存当前工作薄
    workbook.save()
    # 关闭当前工作薄
    workbook.close()
# 退出Excel程序
app.quit()