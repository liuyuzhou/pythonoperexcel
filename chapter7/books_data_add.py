import os
import xlwings as xw

# 启动Excel程序
app = xw.apps.add()
# 全路径
full_path = os.getcwd() + '/files'
# 文件全路径及名称
full_file_name = os.path.join(full_path, '商品信息提取表.xlsx')
# 打开工作薄
workbook = app.books.open(full_file_name)
# 从工作薄中取得指定工作表
worksheet = workbook.sheets['数据提取']
# 取得工作表中的数据
table_values = worksheet.range('A1').expand()
# 读取当前工作表中数据的行数
row_num = table_values.shape[0]
# 异常捕获
try:
    # 待追加内容
    add_content = [[778, 'SKU009977', '笔记本', '300'], [779, 'SKU009978', '装饰品', '500']]
    # 将指定数据追加到当前数据的最后一行后
    worksheet.range(row_num + 1, 1).value = add_content
    # 保存工作薄
    workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
