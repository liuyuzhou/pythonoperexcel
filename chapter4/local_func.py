def local_func():
    x = 100
    print(f'变量x：{x}')


print(f'函数体外访问变量x：{x}')
local_func()
