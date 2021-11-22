import matplotlib.pyplot as plt

# 设置 x 坐标的数据
x = [1, 2, 3, 4, 5, 6]
# 设置 y 坐标的数据
y = [2 * a for a in x]
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制图形
plt.bar(x, y, width=0.5, align='center', color='black')
# x 轴命名
plt.xlabel('x 坐标')
# y 轴命名
plt.ylabel('y 坐标')
# 显示绘制的图形
plt.show()
