import os

# 全路径
full_path = os.getcwd() + '/files'
# 取得全路径下的所有文件列表
file_list = os.listdir(full_path)
# 工作薄中需要替换的旧关键字
old_book_name = '统计'
# 工作薄中需要替换的新关键字
new_book_name = '销量统计'
# 遍历找到的文件列表
for file_name in file_list:
    # 如果 file_name 中没有找到指定的旧关键字，则不做替换
    if file_name.find(old_book_name) <= 0:
        continue

    # 如果 file_name 不以 .xlsx 结尾，则不做替换
    if not file_name.endswith('.xlsx'):
        continue

    # 构建新的文件名
    new_file_name = file_name.replace(old_book_name, new_book_name)
    # 构建原工作薄的完整路径
    old_file_path = os.path.join(full_path, file_name)
    # 构建新工作薄的完整路径
    new_file_path = os.path.join(full_path, new_file_name)
    # 执行重命名
    os.rename(old_file_path, new_file_path)
