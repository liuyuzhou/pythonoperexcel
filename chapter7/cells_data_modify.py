import os
import xlwings as xw

# 全路径
full_path = os.getcwd() + '/files'
# 取得指定路径下所有文件
file_list = os.listdir(full_path)
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 遍历所有文件
for i in file_list:
    # 若是非xlsx文件或是以~$（已打开）开头的文件，继续循环
    if not i.endswith('.xlsx') or i.startswith('~$'):
        continue

    # 文件全路径及名称
    file_full_path_name = os.path.join(full_path, i)
    # 打开工作薄
    workbook = app.books.open(file_full_path_name)
    # 遍历当前工作薄中的工作表
    for j in workbook.sheets:
        # 读取工作表数据
        table_values = j['A2'].expand('table').value
        # 若读取的工作表数据是None，则继续下一个循环
        if not table_values:
            continue

        # 按行遍历工作表数据
        for index_num, value_v in enumerate(table_values):
            # 判断当前行的第三列数据数据中的商品名称是否为 笔记本
            if value_v[2] == '笔记本':
                # 将名称为笔记本的列，库存量都增加 100
                table_values[index_num][3] = table_values[index_num][3] + 100
                # 将名称为笔记本的列，销售单价都打9.5折
                table_values[index_num][4] = table_values[index_num][4] * 0.95
        # 将替换后的数据写入工作表
        j['A2'].expand('table').value = table_values
    # 保存当前工作薄
    workbook.save()
    # 关闭当前工作薄
    workbook.close()
# 退出Excel程序
app.quit()
