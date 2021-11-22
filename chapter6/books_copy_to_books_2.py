import os
import xlwings as xw

# 启动Excel程序
app = xw.App(visible=False, add_book=False)
# 全路径
full_path = os.getcwd() + '/files'
# 取得全路径下的所有文件列表，称为目标工作薄
file_list = os.listdir(full_path)

# 打开指定工作薄，该工作薄用于将工作薄中所有工作表和内容拷贝到其它工作薄，称为来源工作薄
source_wb = app.books.open(os.getcwd() + '/files/公司.xlsx')
# 获得来源工作薄中所有工作表
s_worksheet_list = source_wb.sheets
# 遍历目标工作薄
for file_name in file_list:
    # 对 file_name 判断是否是工作薄，不是则跳过；若是来源工作薄，也跳过
    if not file_name.endswith('.xlsx') or file_name.startswith('公司'):
        continue

    # 打开目标工作薄
    target_wb = app.books.open(os.path.join(full_path, file_name))
    # 取得目标工作薄的所有工作表
    target_wt_list = target_wb.sheets
    # 遍历来源工作薄中的工作表
    for s_worksheet in s_worksheet_list:
        # 取得来源工作薄中要复制的工作表数据
        s_contents = s_worksheet.range('A1').expand('table').value
        # 获取来源工作薄中工作表名称
        s_sheet_name = s_worksheet.name
        # 是否存在同名工作薄
        is_exists_sheet_name = False
        # 遍历目标工作表
        for t_worksheet in target_wt_list:
            # 取得工作表名称
            t_sheet_name = t_worksheet.name
            # 判断来源工作表名和目标工作表名是否相同，若相同，终止循环
            if s_sheet_name == t_sheet_name:
                # is_exists_sheet_name 变量赋值 True
                is_exists_sheet_name = True
                break

        # 如果来源工作表名称不在目标工作表列表中，则在目标工作薄中新增加工作表
        if not is_exists_sheet_name:
            # 在目标工作薄中新增工作表
            target_wb.sheets.add(name=s_sheet_name, after=len(target_wb.sheets))
        # # 将来源工作表中读取的数据写入新增工作表
        target_wb.sheets[s_sheet_name].range('A1').value = s_contents
    # 保存目标工作薄
    target_wb.save()
# 退出Excel程序
app.quit()
