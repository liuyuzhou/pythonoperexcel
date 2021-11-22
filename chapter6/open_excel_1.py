import xlwings as xw

# 当前App下新建一个Book，visible参数控制创建文件时可见的属性
# visible 参数用于设置Excel程序窗口的可见性，True表示显示Excel窗口，False表示隐藏
# add_book参数用于设置启动Excel窗口后是否新建工作薄，True表示新建，False表示不新建
app = xw.App(visible=True, add_book=False)
# 打开当前目录中files文件夹下的 1.xlsx 工作薄
wb = app.books.open('files\\1.xlsx')
# 保存工作薄
wb.save()
# 关闭工作薄
wb.close()
# 退出excel程序
app.quit()
