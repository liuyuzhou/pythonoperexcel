import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 全路径
full_path = os.getcwd() + '/files'
# 从指定工作薄中读取指定工作表数据
df = pd.read_excel(os.path.join(full_path, '商品信息.xlsx'), sheet_name='性能参数')
# 将数据中的指定列设置为行索引
df = df.set_index('性能评价指标')
# 转置数据表格
df = df.T
# 将转置后数据中行索引那一列的名称修改为指定值
df.index.name = '品牌'


# 自定义一个函数
def plot_radar(data, feature):
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决坐标值为负数时无法正常显示负号的问题
    plt.rcParams['axes.unicode_minus'] = False
    # 指定名称指定
    col_list = ['动力性', '燃油经济性', '制动性', '操控稳定性', '行驶平顺性', '通过性', '安全性', '环保性']
    # 指定颜色设置
    color_list = ['black', 'blue', 'red', 'yellow']
    # 根据要显示的指标个数对圆形进行等分
    angles = np.linspace(0.1 * np.pi, 2.1 * np.pi, len(col_list), endpoint=False)
    # 连接刻度线数据
    angles = np.concatenate((angles, [angles[0]]))
    # 设置显示图表的窗口大小
    fig = plt.figure(figsize=(8, 8))
    # 设置图表在窗口中的显示位置，并设置坐标轴为极坐标体系
    ax = fig.add_subplot(111, polar=True)
    # 数据遍历
    for i, c in enumerate(feature):
        # 获取指定数据的指标数据
        stats = data.loc[c]
        # 连接品牌的指标数据
        stats = np.concatenate((stats, [stats[0]]))
        # 制作雷达图
        ax.plot(angles, stats, '-', linewidth=6, c=color_list[i], label=f'{c}')
        # 为雷达图填充颜色
        ax.fill(angles, stats, color=color_list[i], alpha=0.25)
    # 为雷达图添加图例
    ax.legend()
    # 隐藏坐标轴数据
    ax.set_yticklabels([])
    # 添加并设置数据标签
    ax.set_thetagrids(angles * 180 / np.pi, fontsize=16)
    # 显示制作的雷达图
    plt.show()
    # 返回对象
    return fig


# 调用自定义函数制作雷达图，查看指定品牌的性能评价
fig_radar = plot_radar(df, ['D品牌'])
