import os
import xlwings as xw

# 全路径
full_path_file = os.getcwd() + '/files\\商品信息.xlsx'
# 要拆分的工作表名称
sheet_name = '基本信息'

# 启动Excel程序
app = xw.App(visible=True, add_book=False)
# 打开工作薄
workbook = app.books.open(full_path_file)
# 选中需要拆分的工作表
worksheet = workbook.sheets[sheet_name]
# 读取要拆分的工作表中的所有数据
data_v = worksheet.range('A2').expand('table').value
# 创建一个空字典
data_dict = dict()
# 按行遍历工作表数据
for i in range(len(data_v)):
    # 获取当前行的商品名称，用于数据分类
    product_name = data_v[i][2]
    # 判断字典中是否有对应的商品名称
    if product_name not in data_dict:
        # 如果指定商品名称不存在，则创建一个空列表，用于存放当前商品名称对应的行数据
        data_dict[product_name] = list()
    # 将当前行的数据追加到当前商品名称对应的列表中
    data_dict[product_name].append(data_v[i])

# 按商品名称遍历分类后的数据
for key_v, value_v in data_dict.items():
    # 在工作薄中新建工作表，工作表名称为当前商品名称
    new_worksheet = workbook.sheets.add(key_v)
    # 将要拆分的工作表的列标题复制到新建的工作表中
    new_worksheet['A1'].value = worksheet['A1:H1'].value
    # 将当前商品名称下的数据复制到新建工作表中
    new_worksheet['A2'].value = value_v

# 保存工作薄
workbook.save()
# 关闭工作薄
workbook.close()
# 退出Excel程序
app.quit()
