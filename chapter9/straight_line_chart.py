import matplotlib.pyplot as plt

# 设置 x 坐标的数据
x = [1, 2, 3, 4, 5, 6]
# 设置 y 坐标的数据
y = [2 * a for a in x]
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制图形
plt.plot(x, y, color='black', linewidth=3, linestyle='solid')
# x 轴命名
plt.xlabel('x 坐标')
# y 轴命名
plt.ylabel('y 坐标')
# 显示绘制的图形
plt.show()
