import xlwings as xw

# 当前App下新建一个Book
app = xw.App(visible=False)
# 新建工作薄
workbook = app.books.add()
# 新增一个名为 公司统计 的工作表
worksheet = workbook.sheets.add('公司统计')
# 在A1单元格写入值
worksheet.range('A1').value = '公司名称'
# 保存工作薄
workbook.save('files\\公司.xlsx')
# 关闭工作薄
workbook.close()
# 退出excel程序
app.quit()
