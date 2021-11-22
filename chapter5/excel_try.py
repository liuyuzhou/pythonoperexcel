import xlwings as xw

# 当前App下新建一个Book
app = xw.App(visible=True, add_book=False)
# 新建工作薄
workbook = app.books.add()
# 保存新建的工作薄
workbook.save('创建测试.xlsx')
# 关闭工作薄
workbook.close()
# 退出excel程序
app.quit()
