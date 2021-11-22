import os
import xlwings as xw

# 全路径
full_path = os.getcwd() + '/files\\商品信息.xlsx'
# 指定需要合并的工作表名称
sheet_name_list = ['文件夹', '笔记本', '装饰品', '铅笔']
new_sheet_name = '信息合计'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 打开要合并的工作薄
workbook = app.books.open(full_path)
# 遍历工作表
for i in workbook.sheets:
    # 判断工作薄中是否已经存在名为 new_sheet_name 的工作表
    if new_sheet_name == i.name:
        i.delete()

# 在工作薄中新增一个名为 new_sheet_name 的工作表
new_worksheet = workbook.sheets.add(new_sheet_name)
# 定义一个空对象，用于存放工作表中的列标题
header = None
# 定义一个空列表对象
all_data = list()
# 遍历工作薄中的工作表
for j in workbook.sheets:
    # 如果当前工作表表名不是在需要合并的工作表列表中，则继续查找
    if j.name not in sheet_name_list:
        continue

    # 若header对象为空
    if header is None:
        # header对象赋值读取的列标题
        header = j['A1:H1'].value

    # 读取要合并的工作表中的数据
    values = j['A2'].expand('table').value
    # 将多个工作表的数据合并
    all_data += values

# 将工作表的列标题复制到新增工作表中
new_worksheet['A1'].value = header
# 将合并的工作表数据复制到新增工作表中
new_worksheet['A2'].value = all_data
# 自动调整新增工作表的行高和列宽
new_worksheet.autofit()
# 保存工作薄
workbook.save()
# 关闭工作薄
workbook.close()
# 退出Excel程序
app.quit()
