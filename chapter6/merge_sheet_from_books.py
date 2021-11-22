import os
import xlwings as xw

# 全路径
full_path = os.getcwd() + '/files'
# 取得指定路径下的全部文件
file_list = os.listdir(full_path)
# 指定工作表名
sheet_name = '基本信息'
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 定义一个空对象，用于存放工作表中的列标题
header = None
# 定义一个空列表对象
all_data = list()
# 遍历文件列表
for i in file_list:
    # 以指定条件进行过滤
    if not i.startswith('2021'):
        continue

    # 构建文件全路径
    file_path = os.path.join(full_path, i)
    # 打开要合并的工作薄
    workbook = app.books.open(file_path)
    # 遍历要合并的工作薄中的工作表
    for j in workbook.sheets:
        # 工作表的名称是否和指定的工作表名称相同，若不同，则继续遍历
        if j.name != sheet_name:
            continue

        # 若header对象为空
        if header is None:
            # header对象赋值读取的列标题
            header = j['A1:H1'].value

        # 读取要合并的工作表中的数据
        values = j['A2'].expand('table').value
        # 将多个工作薄中同名工作表的数据合并
        all_data += values

# 新建工作薄
new_workbook = xw.Book()
# 在新建工作薄中添加名为指定的 sheet_name 的工作表
new_worksheet = new_workbook.sheets.add(sheet_name)
# 将工作表的列标题复制到新增工作表中
new_worksheet['A1'].value = header
# 将合并的工作表数据复制到新增工作表中
new_worksheet['A2'].value = all_data
# 自动调整新增工作表的行高和列宽
new_worksheet.autofit()
# 构建新工作薄的全路径
new_file_full_path = os.path.join(full_path, '信息合计表.xlsx')
# 根据指定路径及名称新建工作薄并保存
new_workbook.save(new_file_full_path)
# 关闭新工作薄
new_workbook.close()
# 退出Excel程序
app.quit()
