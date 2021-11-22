path = '../chapter8/test.txt'

f_name = open(path, 'w')
print(f"write length:{f_name.write('Hello world!')}")
f_name = open(path, 'r')
print(f'read result:{f_name.read()}')

f_name = open(path, 'a')
print(f"add length:{f_name.write('welcome!')}")
f_name = open(path, 'r')
print(f'read result:{f_name.read()}')
