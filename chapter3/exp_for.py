print('-----for循环字符串-----------')
# for循环字符串
for letter in 'good':
    print(f'当前字母 :{letter}')

print('-----for循环数字序列-----------')
number = [1, 2, 3]
# for循环数字序列
for num in number:
    print(f'当前数字：{num}')

print('-----for循环字典-----------')
tups = {'name': '小智', 'number': '001'}
# for循环字典
for tup in tups:
    print(f'{tup}:{tups[tup]}')
