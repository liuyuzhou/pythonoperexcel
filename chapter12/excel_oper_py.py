import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello,this is self define!":
        sheet["A1"].value = "Use xlwings by self define!"
    else:
        sheet["A1"].value = "Hello xlwings,this is self define!"


@xw.func
def hello(name):
    return f"Hello {name},this is self define!"


@xw.func
def num_multiply(x, y):
    """
    返回两个参数之积
    """
    return f'{x}乘以{y}之积为：{x * y}'


if __name__ == "__main__":
    xw.Book("自定义工作薄.xlsm").set_mock_caller()
    main()
