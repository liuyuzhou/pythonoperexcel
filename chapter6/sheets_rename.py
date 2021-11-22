import os
import xlwings as xw

# 全路径
full_file_path = os.getcwd() + '/files\\销售情况.xlsx'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开工作薄
wb = app.books.open(full_file_path)
# 获取工作薄中所有工作表
worksheets = wb.sheets
# 遍历获取的工作表
for i in range(len(worksheets)):
    # 重命名工作表，将工作表中的 部 重命名为 分部
    worksheets[i].name = worksheets[i].name.replace('部', '分部')

# 另存重命名工作表后的工作薄
wb.save(full_file_path)
# 退出 Excel 程序
app.quit()
