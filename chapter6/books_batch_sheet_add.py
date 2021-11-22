import xlwings as xw

# 当前App下新建一个Book
app = xw.App(visible=False)
# 新建工作薄
workbook = app.books.add()
# 数字字符串集合
num_list = ['一', '二', '三', '四', '五', '六']
# 遍历数字字符串集合
for num_str in num_list:
    # 新增一个名为 销售{num_str}部 的工作表
    worksheet = workbook.sheets.add(f'销售{num_str}部')
# 保存工作薄
workbook.save('files\\销售情况.xlsx')
# 关闭工作薄
workbook.close()
# 退出excel程序
app.quit()
