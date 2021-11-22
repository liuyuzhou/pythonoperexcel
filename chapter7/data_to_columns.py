import os
import xlwings as xw
import pandas as pd

# 启动Excel程序
app = xw.apps.add()
# 全路径
full_path = os.getcwd() + '/files'
# 取得指定路径下的所有工作薄
file_list = os.listdir(full_path)
# 异常捕获
try:
    # 遍历工作薄
    for i in file_list:
        # 若工作薄以 ~$ 开头 或 不是以 .xlsx 结尾，则继续循环
        if i.startswith('~$') or not i.endswith('.xlsx'):
            continue

        # 构建文件的全路径及文件名
        file_full_name = os.path.join(full_path, i)
        # 打开工作薄
        workbook = app.books.open(file_full_name)
        # 取得当前工作薄的所有工作表
        sheet_list = workbook.sheets
        # 指定目标工作表名称
        target_sheet = '商品基本信息'
        # 遍历工作表列表，取得与目标工作表名称相同的工作表
        find_sheet = [sheet for sheet in sheet_list if sheet.name == target_sheet]
        # 若没有找到目标工作表，继续循环查找
        if not find_sheet:
            continue

        # 将找到的目标工作表赋值给 worksheet对象
        worksheet = find_sheet[0]
        # 从目标工作表中取得列表数据，结合pandas取得
        values = worksheet.range('A1').options(pd.DataFrame, header=1, index=False, expand='table').value
        # values为None，继续下一个循环
        if values.empty:
            continue
        #
        new_values = values['装箱情况'].str.split('*', expand=True)
        #
        values['个数（个）'] = new_values[0]
        #
        values['盒数（盒）'] = new_values[1]
        #
        values.drop(column=['装箱情况'], inplace=True)
        # 转置数据的行列
        values = values.T
        #
        values.columns = values.iloc[0]
        #
        values.index.name = values.iloc[0].index.name
        #
        values.drop(values.iloc[0].index.name, inplace=True)
        # 清除目标工作表中原有数据
        worksheet.clear()
        #
        worksheet['A1'].value = values
        # 自动调整工作表的行高和列宽
        worksheet.autofit()
        # 保存工作薄
        workbook.save()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭新工作薄
    workbook.close()
# 退出Excel程序
app.quit()
