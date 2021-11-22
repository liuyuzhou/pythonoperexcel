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

        # 合并指定数据列，指定合并后数据列的名称
        values['装箱情况'] = values['个数（个）'].astype('str') + '*' + values['盒数（盒）'].astype('str')
        # 删除指定标题的列
        values.drop(columns=['个数（个）'], inplace=True)
        # 删除指定标题的列
        values.drop(columns=['盒数（盒）'], inplace=True)
        # 清除目标工作表中原有数据
        worksheet.clear()
        # 将处理好的数据写入工作表
        worksheet['A1'].options(index=False).value = values
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
