import os
import xlwings as xw

# 启动Excel程序
app = xw.apps.add()
# 全路径
full_path = os.getcwd() + '/files'
# 文件全路径及名称
full_file_name = os.path.join(full_path, '商品信息.xlsx')
# 打开工作薄
workbook = app.books.open(full_file_name)
# 库存数列表
store_datas = list()
# 异常捕获
try:
    # 遍历工作表
    for i, worksheet in enumerate(workbook.sheets):
        # 取得表格块所有数据
        table_values = worksheet['A2'].expand('table').value
        # 若 down_values 为空，继续下一个循环
        if not table_values:
            continue

        # 取得的数据追加到库存列表
        store_datas.extend(table_values)
    # 定义一个字典，用于存放商品名称和商品库存的对应关系
    s_dict = dict()
    # 遍历库存数据
    for i in range(len(store_datas)):
        # 取得商品名称
        shopping_name = store_datas[i][2]
        # 取得商品库存
        shopping_store = store_datas[i][3]
        # 判断字典中是否已经存在 key 为 shopping_name 的记录
        if shopping_name not in s_dict:
            # 不存在，则生成一个以 shopping_name 为key的字典记录，value值为 shopping_store
            s_dict[shopping_name] = shopping_store
        else:
            # 已经存在指定shopping_name，则指定shopping_name的库存增加
            s_dict[shopping_name] += shopping_store
    # 商品名称库存列表
    shopping_store_list = list()
    # 遍历商品名称库存字典
    for key_v, value_v in s_dict.items():
        # 商品名称库存
        name_store = [key_v, value_v]
        # 商品名称库存列表追加 商品名称库存
        shopping_store_list.append(name_store)
    # 商品名称库存列表 第一个位置插入一个元素
    shopping_store_list.insert(0, ['商品名称', '库存总量'])
    # 新建工作薄
    new_workbook = xw.books.add()
    # 在新工作薄中新增名为 库存统计 的工作表
    new_worksheet = new_workbook.sheets.add('库存统计')
    # 将提取出的行数据写入工作表 库存统计 中
    new_worksheet['A1'].value = shopping_store_list
    # 自动调整工作表的行高和列宽
    new_worksheet.autofit()
    # 保存新工作薄并命名
    new_workbook.save(os.path.join(full_path, '商品库存统计.xlsx'))
    # 关闭新工作薄
    new_workbook.close()
# 不管前面代码执行是否发生异常，都执行该语句块的语句
finally:
    # 关闭工作薄
    workbook.close()
# 退出Excel程序
app.quit()
