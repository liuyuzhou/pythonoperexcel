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
        # 设置工作表标题行的字体为 楷体
        j['A1:H1'].api.Font.Name = '楷体'
        # 设置工作表标题的字号为 12 磅
        j['A1:H1'].api.Font.Size = 12
        # 加粗工作表标题行
        j['A1:H1'].api.Font.Bold = True
        # 设置工作表标题行的字体颜色为 白色
        j['A1:H1'].api.Font.Color = xw.utils.rgb_to_int((255, 255, 255))
        # 设置工作表标题行的单元格填充颜色为 黑色
        j['A1:H1'].color = xw.utils.rgb_to_int((0, 0, 0))
        # 设置工作表标题行的水平对齐方式为 居中
        j['A1:H1'].api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
        # 设置工作表标题行的垂直对齐方式为 居中
        j['A1:H1'].api.VerticalAlignment = xw.constants.VAlign.xlVAlignCenter
        # 设置工作表正文的字体为 宋体
        j['A2'].expand('table').api.Font.Name = '宋体'
        # 设置工作表正文的字号为 10 磅
        j['A2'].expand('table').api.Font.Size = 10
        # 设置工作表正文的水平对齐方式为 靠左
        j['A2'].expand('table').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignLeft
        # 设置工作表正文的垂直对齐方式为 居中
        j['A2'].expand('table').api.VerticalAlignment = xw.constants.VAlign.xlVAlignCenter
        # 从单元格 A1 开始为工作表添加边框
        for cell in j['A1'].expand('table'):
            for b in range(7, 12):
                # 设置单元格的边框线型
                cell.api.Borders(b).LineStyle = 1
                # 设置单元格的边框粗细
                cell.api.Borders(b).Weight = 2
    # 保存当前工作薄
    workbook.save()
    # 关闭当前工作薄
    workbook.close()
# 退出Excel程序
app.quit()
