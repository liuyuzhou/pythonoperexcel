path = '../chapter8/test.txt'
f_name = open(path, 'w')
print(f"write length:{f_name.write('Hello world!')}")
f_name.close()
