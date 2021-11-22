import os
import xlwings as xw

# 全路径
full_file_path = os.getcwd() + '/files/销售情况.xlsx'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开工作薄
wb = app.books.open(full_file_path)
# 获取工作薄中所有工作表
worksheets = wb.sheets
# 需要删除的工作表关键字
key_name = '二'
# 遍历获取的工作表
for i in worksheets:
    # 若工作表名中包含删除关键字
    if i.name.find(key_name) > 0:
        # 删除工作表
        i.delete()

# 另存重命名工作表后的工作薄
wb.save()
# 退出 Excel 程序
app.quit()
