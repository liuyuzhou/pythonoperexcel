import xlwings as xw

# 创建一个新的App，并在新App中新建一个Book
wb = xw.Book()
# 保存工作薄
wb.save('files\\1.xlsx')
# 关闭工作薄
wb.close()
