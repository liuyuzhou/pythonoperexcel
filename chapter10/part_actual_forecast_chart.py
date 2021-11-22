import os
import xlwings as xw
import pandas as pd
import matplotlib.pyplot as plt

# 全路径
full_path = os.getcwd() + '/files'


# 自定义函数获取记录总行数
def get_total_row(full_file_name, sheet_name, include_header=False):
    """
    full_file_name:需要打开文件的全路径
    sheet_name:需要访问的工作表
    include_header:是否包含标题行，默认不包含
    return: 返回数据的行数，默认不包含标题行
    """
    # 启动Excel程序
    app = xw.App(visible=False, add_book=False)
    # 打开工作薄
    workbook = app.books.open(full_file_name)
    # 异常捕获
    try:
        # 从工作薄中取得指定工作表
        worksheet = workbook.sheets[sheet_name]
        # 取得工作表中的数据
        table_values = worksheet.range('A1').expand()
        # 读取当前工作表中数据的行数
        row_num = table_values.shape[0]
        # 若不包含标题行，返回的行数为 获取的行号数减去1
        if not include_header:
            row_num = row_num - 1
    # 不管前面代码执行是否发生异常，都执行该语句块的语句
    finally:
        # 关闭工作薄
        workbook.close()
    # 退出Excel程序
    app.quit()
    return row_num


# 文件全路径及名称
full_file = os.path.join(full_path, '商品信息.xlsx')
# 指定工作表名称
sheet_name = '预估库存'
# 从指定工作薄中读取数据
df = pd.read_excel(full_file, sheet_name=sheet_name)
# 定义变量 sum_val，用于存储总库存量
sum_val = 0
# 取得指定工作表中的数据行数
data_row = get_total_row(full_file, sheet_name)
# 根据数据行数遍历表格数据，计算 三分之二的数据
for i in range(data_row // 3 * 2):
    # 累加所有的库存量
    sum_val = df['库存量'][i] + sum_val
# 获取预估库存量
estimate_num = df['库存量'][data_row - 1]
# 计算得到的总库存与预估库存的百分比
percentage = sum_val / estimate_num
# 制作柱形图，填充色为black
plt.bar(1, 1, color='black')
# 制作柱形图，填充色为yellow
plt.bar(1, percentage, color='yellow')
# 设置图表x轴的取值范围
plt.xlim(0, 2)
# 设置图表y轴的取值范围
plt.ylim(0, 1.2)
# 添加并设置数据标签
plt.text(1, percentage - 0.01, percentage, ha='center', va='top',
         fontdict={'color': 'black', 'size': 20})
# 显示制作的温度计图
plt.show()
