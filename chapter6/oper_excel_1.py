import xlwings as xw

# 当前App下新建一个Book
app = xw.App(visible=True, add_book=False)
# 打开当前目录中files文件夹下的 1.xlsx 工作薄
wb = app.books.open('files\\1.xlsx')
# 实例化一个工作表对象
sheet_1 = wb.sheets["sheet1"]
# 在A1单元格写入值
sheet_1.range('A1').value = 'python操作excel'
# 保存工作薄
wb.save()
# 关闭工作薄
wb.close()
# 退出excel程序
app.quit()
