# 示例1
for letter in 'hello':
    if letter == 'l':
        break
    print(f'当前字母为:{letter}')

# 示例2
num = 10
while num > 0:
    print(f'输出数字为:{num}')
    num -= 1
    if num == 8:
        break
