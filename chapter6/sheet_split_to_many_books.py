import xlwings as xw
import os

# 全路径
full_path = os.getcwd() + '/files'
s_books = os.path.join(full_path, '商品信息.xlsx')
# 要拆分的工作表名称
s_sheet_name = '基本信息'

# 启动Excel程序
app = xw.App(visible=True, add_book=False)
# 打开来源工作薄
s_workbook = app.books.open(s_books)
# 选中需要拆分的工作表
s_worksheet = s_workbook.sheets[s_sheet_name]
# 读取要拆分的工作表中的所有数据
s_data_v = s_worksheet.range('A2').expand('table').value
# 创建一个空字典
data_dict = dict()
# 按行遍历工作表数据
for i in range(len(s_data_v)):
    # 获取当前行的商品名称，用于数据分类
    product_name = s_data_v[i][2]
    # 判断字典中是否有对应的商品名称
    if product_name not in data_dict:
        # 如果指定商品名称不存在，则创建一个空列表，用于存放当前商品名称对应的行数据
        data_dict[product_name] = list()
    # 将当前行的数据追加到当前商品名称对应的列表中
    data_dict[product_name].append(s_data_v[i])

# 按商品名称遍历分类后的数据
for key_v, value_v in data_dict.items():
    # 新建工作薄
    new_workbook = xw.books.add()
    # 在工作薄中新建工作表，工作表名称为当前商品名称
    new_worksheet = new_workbook.sheets.add(key_v)
    # 将要拆分的工作表的列标题复制到新建的工作表中
    new_worksheet['A1'].value = s_worksheet['A1:H1'].value
    # 将当前商品名称下的数据复制到新建工作表中
    new_worksheet['A2'].value = value_v
    # 以当前商品名称命名新建工作薄
    new_books_full_path_name = os.path.join(full_path, f'{key_v}.xlsx')
    # 保存新工作薄
    new_workbook.save(new_books_full_path_name)
# 退出Excel程序
app.quit()
