import os
import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt
from sklearn import linear_model

# 全路径
full_path = os.getcwd() + '/files'
# 指定工作表名称
sheet_name = '商品名称库存单价'
# 文件全路径及文件名
full_file_name = os.path.join(full_path, '商品信息.xlsx')
# 从指定工作薄中读取指定工作表数据
df = pd.read_excel(full_file_name, sheet_name=sheet_name)


def draw_ring():
    """
    绘制圆环图
    :return:
    """
    # 创建一个绘图窗口
    figure = plt.figure()
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决坐标值为负数时无法正常显示负号的问题
    plt.rcParams['axes.unicode_minus'] = False
    # 指定列为 x 坐标值
    x = df['商品名称']
    # 指定列为 y 坐标值
    y = df['库存量']
    # 制作饼图并分离饼图块
    plt.pie(y, labels=x, labeldistance=1.1, autopct='%.2f%%', pctdistance=0.85,
            radius=1.0, wedgeprops={'width': 0.3, 'linewidth': 2, 'edgecolor': 'white'})
    # 添加并设置图表标题
    plt.title(label='商品库存占比环形图', fontdict={'color': 'black', 'size': 30}, loc='center')

    return figure


def draw_pie():
    """
    绘制饼图
    :return:
    """
    # 创建一个绘图窗口
    figure = plt.figure()
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决坐标值为负数时无法正常显示负号的问题
    plt.rcParams['axes.unicode_minus'] = False
    # 指定列为 x 坐标值
    x = df['商品名称']
    # 指定列为 y 坐标值
    y = df['库存量']
    # 制作饼图并分离饼图块
    plt.pie(y, labels=x, labeldistance=1.1, autopct='%.2f%%', pctdistance=0.8,
            startangle=90, radius=1.0, explode=[0, 0, 0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0])
    # 添加并设置图表标题
    plt.title(label='商品库存占比图', fontdict={'color': 'black', 'size': 30}, loc='center')

    return figure


def bubble_chart():
    """
    气泡图
    :return:
    """
    figure = plt.figure()
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决坐标值为负数时无法正常显示负号的问题
    plt.rcParams['axes.unicode_minus'] = False
    # 指定列为 x 坐标值
    x = df['库存量']
    # 指定列为 y 坐标值
    y = df['销售单价']
    # 指定列为 z 坐标值
    z = df['商品名称']
    # 制作气泡图
    plt.scatter(x, y, s=y * 30, color='black', marker='o')
    # 添加并设置x轴标题
    plt.xlabel('销售单价',
               fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 15},
               labelpad=5)
    # 添加并设置y轴标题
    plt.ylabel('库存量',
               fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 15},
               labelpad=5)
    # 添加并设置图表标题
    plt.title('库存与销售单价关系图',
              fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 20},
              loc='center')
    # 遍历取得的数据
    for a, b, c in zip(x, y, z):
        # 添加并设置数据标签
        plt.text(a, b, c, ha='center', va='center', fontsize=14, color='white')
    # 设置x轴取值范围
    plt.xlim(0, 150)
    # 设置y轴取值范围
    plt.ylim(0, 180)

    return figure


def plot_trend_chart():
    """
    折线图
    :return:
    """
    figure = plt.figure()
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决坐标值为负数时无法正常显示负号的问题
    plt.rcParams['axes.unicode_minus'] = False
    # 指定列为 x 坐标值
    x = df['商品名称']
    # 指定列为 y 坐标值
    y = df['库存量']
    # 制作折线图
    plt.plot(x, y, color='black', linewidth=2, linestyle='solid')
    # 添加并设置图表标题
    plt.title(label='库存量趋势图',
              fontdict={'color': 'black', 'size': 30}, loc='center')
    # 获取最大库存量
    max_store = df['库存量'].max()
    # 选取最高销售额对应的行数据
    df_max = df[df['库存量'] == max_store]
    # 遍历折线图的数据点
    for a, b in zip(df_max['商品名称'], df_max['库存量']):
        # 添加并设置数据标签
        plt.text(a, b + 0.05, (a, b), ha='center', va='bottom', fontsize=10)
    # 隐藏坐标轴
    plt.axis('off')

    return figure


def scatter_chart_add_trend():
    """
    散点图线型趋势
    :return:
    """
    # 创建一个绘图窗口
    figure = plt.figure()
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决坐标值为负数时无法正常显示负号的问题
    plt.rcParams['axes.unicode_minus'] = False
    # 指定列为 x 坐标值
    x = df['库存量']
    # 指定列为 y 坐标值
    y = df['销售单价']
    # 制作散点图
    plt.scatter(x, y, s=200, color='black', marker='o', edgecolors='black')
    # 添加并设置x轴标题
    plt.xlabel('库存量',
               fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 15},
               labelpad=5)
    # 添加并设置y轴标题
    plt.ylabel('销售单价',
               fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 15},
               labelpad=5)
    # 添加并设置图表标题
    plt.title('库存与销售单价关系图',
              fontdict={'family': 'Microsoft YaHei', 'color': 'black', 'size': 20},
              loc='center')
    # 创建一个线型回归模型，并用自变量和因变量数据对线型回归模型进行训练，拟合出线型回归方程
    model = linear_model.LinearRegression().fit(x.values.reshape(-1, 1), y)
    # 模型预测
    pred = model.predict(x.values.reshape(-1, 1))
    # 绘制线性趋势线
    plt.plot(x, pred, color='black', linewidth=2, linestyle='solid', label='线型趋势图')
    # 设置图例
    plt.legend(loc='upper left')
    # 设置x轴取值范围
    plt.xlim(0, 150)
    # 设置y轴取值范围
    plt.ylim(0, 180)

    return figure


def workbook_picture_insert():
    """
    在工作表中插入图
    """
    # 启动Excel程序
    app = xw.App(visible=False, add_book=False)
    # 打开指定工作薄
    workbook = app.books.open(os.path.join(full_path, '商品信息.xlsx'))

    ring_figure = draw_ring()
    pie_figure = draw_pie()
    bubble_figure = bubble_chart()
    plot_figure = plot_trend_chart()
    scatter_figure = scatter_chart_add_trend()

    # 异常捕获
    try:
        # 取得指定工作薄中的所有工作表
        sheet_list = workbook.sheets
        # 从所有工作表中取得指定名称的工作表
        select_sheet = [sheet for sheet in sheet_list if sheet.name == sheet_name]
        # 找到了指定的工作表
        if select_sheet:
            # 从筛选结果集中取得第一个工作表
            worksheet = select_sheet[0]
            # 在工作表中插入圆环图
            worksheet.pictures.add(ring_figure, name='圆环图', update=True, left=180)
            # 在工作表中插入饼图
            worksheet.pictures.add(pie_figure, name='饼图', update=True, left=500)
            # 在工作表中插入气泡图
            worksheet.pictures.add(bubble_figure, name='气泡图', update=True,
                                   left=180, top=350)
            # 在工作表中插入折线图
            worksheet.pictures.add(plot_figure, name='折线图', update=True,
                                   left=600, top=350)
            # 在工作表中插入散点图
            worksheet.pictures.add(scatter_figure, name='散点图', update=True, left=820)
            # 保存工作薄
            workbook.save(os.path.join(full_path, '全量信息对比图.xlsx'))
    # 不管前面代码执行是否发生异常，都执行该语句块的语句
    finally:
        # 关闭工作薄
        workbook.close()
    # 退出Excel程序
    app.quit()


if __name__ == '__main__':
    workbook_picture_insert()
