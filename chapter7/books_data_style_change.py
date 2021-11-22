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
        # 获取工作表中数据区域最后一行的行号
        row_num = j['A1'].current_region.last_cell.row
        # 将 E 列 销售单价 的格式更改为带货币符号的两位小数格式
        j[f'E2:E{row_num}'].number_format = '￥#,##0.00'
        # 将 H 列 生产日期 的格式更改为 年-月-日 的格式
        j[f'H2:H{row_num}'].number_format = 'yyyy-mm-dd'
    # 保存当前工作薄
    workbook.save()
    # 关闭当前工作薄
    workbook.close()
# 退出Excel程序
app.quit()
