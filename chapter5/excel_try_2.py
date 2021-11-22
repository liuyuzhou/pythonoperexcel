import xlwings as xw

# 当前App下新建一个Book
app = xw.App(visible=True, add_book=False)
# 打开指定工作薄
wb = app.books.open('创建测试.xlsx')
# 实例化一个工作表对象
sheet_1 = wb.sheets["sheet1"]
# 在A1单元格写入值
sheet_1.range('A1').value = 'Hello, world'
# 保存工作薄
wb.save()
# 关闭工作薄
wb.close()
# 退出excel程序
app.quit()
