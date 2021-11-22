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
# 唯一值数据列表
unique_data = list()
# 异常捕获
try:
    # 遍历指定工作薄中的工作表
    for i, worksheet in enumerate(workbook.sheets):
        # 取得工作表中 列C2 的数据值
        down_values = worksheet['C2'].expand('down').value
        # 若 down_values 为空，继续下一个循环
        if not down_values:
            continue

        # 将取得的数据值追加到数据列表
        unique_data.extend(down_values)
    # 数据列表数据去重
    unique_data = list(set(unique_data))
    # 数据列表第一行插入标题名
    unique_data.insert(0, '商品名称')
    # 新建工作薄
    new_workbook = xw.books.add()
    # 在新工作薄中新增名为 装饰品 的工作表
    new_worksheet = new_workbook.sheets.add('商品名称')
    # 将提取出的行数据写入工作表 装饰品 中
    new_worksheet['A1'].options(transpose=True).value = unique_data
    # 自动调整工作表的行高和列宽
    new_worksheet.autofit()
    # 保存新工作薄并命名
    new_workbook.save(os.path.join(full_path, '商品名称.xlsx'))
    # 关闭新工作薄
    new_workbook.close()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
