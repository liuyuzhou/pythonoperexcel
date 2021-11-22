import os

# 全路径
full_path = os.getcwd() + '/files'
# 取得全路径下的所有文件列表
file_list = os.listdir(full_path)
# 需要删除的工作薄名称的关键字
remove_key = '销量统计'
# 遍历工作薄
for file in file_list:
    # 工作薄名称中是否找到指定关键字
    if file.find(remove_key) < 0:
        continue

    # 根据路径删除指定文件
    os.remove(os.path.join(full_path, file))
