import os
import xlwings as xw

# 全路径
full_path = os.getcwd() + '/files'
# 取得全路径下的所有文件列表
file_list = os.listdir(full_path)
# 启动Excel程序
app = xw.App(visible=True, add_book=False)
# 遍历文件列表
for i in file_list:
    # 如果当前文件不是以 .xlsx 后缀结尾，则继续查找
    if not i.endswith('.xlsx'):
        continue

    # 打开当前工作薄，需要全路径加上当前文件名
    app.books.open(full_path + '\\' + i)
