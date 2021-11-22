import pandas as pd
import os
# 导入 matplotlib 模块
import matplotlib.pyplot as plt
import xlwings as xw

# 全路径
full_path = os.getcwd() + '/files'
# 读取指定工作薄中的数据
df = pd.read_excel(os.path.join(full_path, '商品.xlsx'))
# 重命名数据列
df.columns = ['序号', '商品sku', '库存量']
# 删除指定列
df = df.drop(columns=['序号', '商品sku'])
# 计算数据的个数、平均数、最大值和最小值等描述数据
df_describe = df.astype('float').describe()
# 将指定列的数据分成 7 个均等的区间
df_cut = pd.cut(df['库存量'], bins=9, precision=2)
# 统计各个区间的数据
cut_count = df['库存量'].groupby(df_cut).count()
# 创建一个空 DataFrame 用于汇总数据
df_all = pd.DataFrame()
# 将数据写入 DataFrame 中
df_all['计数'] = cut_count
# 将索引重置为数字序号
df_all_new = df_all.reset_index()
# 将列的数据转换为字符串类型
df_all_new['库存量'] = df_all_new['库存量'].apply(lambda x: str(x))
# 创建绘图窗口
fig = plt.figure()
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 使用指定列数据绘制直方图
n, bins, patches = plt.hist(df['库存量'], bins=9, edgecolor='black', linewidth=0.5)
# 将直方图x轴的刻度标签设置为各区间的端点值
plt.xticks(bins)
# 设置直方图的图表标题
plt.title('库存量分析')
# 设置直方图x轴的标题
plt.xlabel('库存量')
# 设置直方图y轴的标题
plt.ylabel('频数')
# 开启Excel程序
app = xw.App(visible=False)
# 打开指定工作薄
workbook = app.books.open(os.path.join(full_path, '商品.xlsx'))
# 异常捕获
try:
    # 取得指定工作薄中的所有工作表
    sheet_list = workbook.sheets
    # 从所有工作表中取得指定名称的工作表
    select_sheet = [sheet for sheet in sheet_list if sheet.name == '商品信息']
    # 找到了指定的工作表
    if select_sheet:
        # 从筛选结果集中取得第一个工作表
        worksheet = select_sheet[0]
        # 将计算出的个数、平均值、最大值和最小值等数据写入工作表
        worksheet.range('E2').value = df_describe
        # 将区间数据写入工作表
        worksheet.range('H2').value = df_all_new
        # 将绘制的直方图转换为图片并写入工作表
        worksheet.pictures.add(fig, name='图1', update=True, left=400, top=200)
        # 根据数据内容自动调整工作表的行高和列宽
        worksheet.autofit()
        # 保存工作薄
        workbook.save(os.path.join(full_path, '库存统计1.xlsx'))
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
