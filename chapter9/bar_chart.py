import matplotlib.pyplot as plt

# 设置 x 坐标的数据
x = [1, 2, 3, 4, 5, 6]
# 设置 y 坐标的数据
y = [5 * a for a in x]
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制图形
plt.barh(x, y, align='center', color='black')
# x 轴命名
plt.xlabel('y 坐标数值')
# y 轴命名
plt.ylabel('x 坐标数值')
# 显示绘制的图形
plt.show()
