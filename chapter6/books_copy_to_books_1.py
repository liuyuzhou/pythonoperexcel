import os
import xlwings as xw

# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 全路径
full_path = os.getcwd() + '/files'
# 取得全路径下的所有文件列表，称为目标工作薄
file_list = os.listdir(full_path)

# 打开指定工作薄，该工作薄用于将工作薄中所有工作表和内容拷贝到其它工作薄，称为来源工作薄
wb = app.books.open('/chapter6\\files\\公司.xlsx')
# 获得来源工作薄中所有工作表
worksheet_list = wb.sheets
# 遍历目标工作薄
for file_name in file_list:
    # 对 file_name 判断是否是工作薄，不是则跳过；若是来源工作薄，也跳过
    if not file_name.endswith('.xlsx') or file_name.startswith('公司'):
        continue

    # 打开目标工作薄
    workbooks = app.books.open(os.path.join(full_path, file_name))
    # 遍历来源工作薄中的工作表
    for worksheet in worksheet_list:
        # 取得来源工作薄中要复制的工作表数据
        contents = worksheet.range('A1').expand('table').value
        # 获取来源工作薄中工作表名称
        sheet_name = worksheet.name
        # 在目标工作薄中新增工作表
        workbooks.sheets.add(name=sheet_name, after=len(workbooks.sheets))
        # 将来源工作表中读取的数据写入新增工作表
        workbooks.sheets[sheet_name].range('A1').value = contents
    # 保存目标工作薄
    workbooks.save()
# 退出Excel程序
app.quit()
