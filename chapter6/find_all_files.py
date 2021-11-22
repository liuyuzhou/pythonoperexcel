import os

# 全路径
full_path = os.getcwd() + '/files'
# 取得全路径下的所有文件列表
file_list = os.listdir(full_path)
# 遍历文件列表
for i in file_list:
    # 如果当前文件不是以 .xlsx 后缀结尾，则继续查找，使用了字符串中的endswith方法
    if not i.endswith('.xlsx'):
        continue

    # 打印以 .xlsx 后缀结尾的文件名
    print(f'找到的文件名：{i}')
