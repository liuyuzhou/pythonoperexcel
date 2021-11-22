import xlwings as xw

# 将城市名存放在一个列表中
city_list = ['北京', '上海', '广州', '深圳', '杭州', '武汉', '成都']
# 当前App下新建一个Book，visible参数控制创建文件时可见的属性
app = xw.App(visible=True, add_book=False)
for city_name in city_list:
    # 新建工作薄
    wb = app.books.add()
    # 保存新建的工作薄
    wb.save(f'files\\2021年{city_name}一季度销售报表.xlsx')
    # 关闭当前工作薄
    wb.close()
# 退出Excel程序
app.quit()
