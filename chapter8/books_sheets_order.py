import xlwings as xw
import pandas as pd
import os

# 全路径
full_path = os.getcwd() + '/files'
# 取得指定路径下的全部文件
book_list = os.listdir(full_path)
# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 文件遍历
for i in book_list:
    # 若文件以指定字符开头或不以指定字符结尾，则继续循环
    if i.startswith('~$') or not i.endswith('.xlsx'):
        continue

    # 打开指定工作薄
    workbook = app.books.open(os.path.join(full_path, i))
    # 异常捕获
    try:
        # 取得工作薄的所有工作表
        sheet_list = workbook.sheets
        # 遍历工作表
        for j in sheet_list:
            # 读取当前工作表数据并转换为DataFrame格式
            table_values = j.range('A1').expand('table').options(pd.DataFrame).value
            # 工作表中的table_values为None，继续下一个循环
            if table_values.empty:
                continue

            # 对指定列进行升序排序，默认排序顺序是升序
            sort_result = table_values.sort_values(by='库存量')
            # 将排序结果写入当前工作表，替换原有数据
            j.range('A1').value = sort_result

        # 保存工作薄
        workbook.save()
    # 不管前面代码执行是否发生异常，都执行该语句块的语句
    finally:
        # 关闭工作薄
        workbook.close()
# 退出Excel程序
app.quit()
