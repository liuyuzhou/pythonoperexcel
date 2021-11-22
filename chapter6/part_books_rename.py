import os

# 全路径
full_path = os.getcwd() + '/files'
# 取得全路径下的所有文件列表
file_list = os.listdir(full_path)
# 定义重命名文本字典，key：工作薄名称关键字；value：工作薄中需要重命名的新关键字
rename_file_dict = {'6月': '年中销量统计', '12月': '年终销量统计'}
# 工作薄中需要替换的旧关键字
old_book_name = '销量统计'
# 遍历找到的文件列表
for file_name in file_list:
    # 遍历字典，同时取得 key和value 的值
    for key_v, value_v in rename_file_dict.items():
        # 如果 file_name 中没有找到指定的旧关键字，则不做替换
        if file_name.find(key_v) <= 0:
            continue

        # 如果 file_name 不以 .xlsx 结尾，则不做替换
        if not file_name.endswith('.xlsx'):
            continue

        # 构建新的文件名
        new_file_name = file_name.replace(old_book_name, value_v)
        # 构建原工作薄的完整路径
        old_file_path = os.path.join(full_path, file_name)
        # 构建新工作薄的完整路径
        new_file_path = os.path.join(full_path, new_file_name)
        # 执行重命名
        os.rename(old_file_path, new_file_path)
