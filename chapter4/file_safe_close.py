path = '../chapter8/test.txt'
try:
    f_name = open(path, 'w')
    print(f"write length:{f_name.write('Hello world!')}")
finally:
    if f_name:
        f_name.close()
