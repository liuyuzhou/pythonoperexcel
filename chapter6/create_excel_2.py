import xlwings as xw

# 当前App下新建一个Book，visible参数控制创建文件时可见的属性
# visible 参数用于设置Excel程序窗口的可见性，True表示显示Excel窗口，False表示隐藏
# add_book参数用于设置启动Excel窗口后是否新建工作薄，True表示新建，False表示不新建
app = xw.App(visible=False, add_book=False)
wb = app.books.add()
# 保存工作薄
wb.save('files\\1.xlsx')
# 关闭工作薄
wb.close()
# 结束进程，退出Excel程序
app.quit()