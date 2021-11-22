import os
import xlwings as xw
import pandas as pd

# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 全路径
full_path = os.getcwd() + '/files'
# 文件全路径及名称
full_file_name = os.path.join(full_path, '商品信息.xlsx')
# 打开工作薄
workbook = app.books.open(full_file_name)
# 取得工作薄中所有工作表
worksheet_list = workbook.sheets
# 创建一个空的列表用于存放列表数据
data_list = list()
extract_columns = ['商品sku', '商品名称', '库存量']
# 遍历工作表
for i in worksheet_list:
    # 读取当前工作表的所有数据
    table_values = i.range('A1').expand().options(pd.DataFrame).value
    # 若读取的工作表数据是None，则继续下一个循环
    if table_values.empty:
        continue

    # 根据指定条件提取数据
    filter_data = table_values[extract_columns]
    # 提取的数据若不为空
    if not filter_data.empty:
        # 提取的数据追加到列表中
        data_list.append(filter_data)
# 新建工作薄
new_workbook = xw.books.add()
# 在新工作薄中新增名为 装饰品 的工作表
new_worksheet = new_workbook.sheets.add('数据提取')
# 将提取出的行数据写入工作表 装饰品 中
new_worksheet.range('A1').value = pd.concat(data_list, ignore_index=False)
# 保存新工作薄并命名
new_workbook.save(os.path.join(full_path, '商品信息提取表.xlsx'))
# 关闭新工作薄
new_workbook.close()
# 关闭工作薄
workbook.close()
# 退出Excel程序
app.quit()
