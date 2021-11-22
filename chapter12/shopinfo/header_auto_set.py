import xlwings as xw


def header_set():
    # 调用本函数的工作薄
    workbook = xw.Book.caller()
    # 取得指定工作表
    worksheet = workbook.sheets[0]
    # 取得指定单元格数据
    get_val = worksheet.range('B100').value
    # 选择工作表
    sheet = workbook.sheets[get_val]
    # 指定单元格设置内容
    sheet.range('A1').value = '序号'
    sheet.range('B1').value = '商品sku'
    sheet.range('C1').value = '商品名称'
    sheet.range('D1').value = '库存量'
    sheet.range('E1').value = '销售单价'
    sheet.range('F1').value = '商品产地'
    sheet.range('G1').value = '商品编号'
    sheet.range('H1').value = '生产日期'
