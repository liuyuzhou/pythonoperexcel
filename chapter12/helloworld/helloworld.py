import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"


@xw.func
def hello(name):
    return f"Hello {name}!"


@xw.sub
def num_add():
    wb = xw.Book.caller()
    x = wb.sheets[0].range('B1').value
    y = wb.sheets[0].range('C1').value
    total_val = str(x + y)
    wb.sheets[0].range('A1').value = total_val


if __name__ == "__main__":
    xw.Book("helloworld.xlsm").set_mock_caller()
    main()
