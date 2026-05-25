import openpyxl

def read_login_data(file, sheet):

    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]

    data = []
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {}
        for key, value in zip(headers, row):
            row_data[key.lower()] = clean(value)

        data.append(row_data)

    return data

def clean(value):
    if value is None:
        return ""
    value = str(value).strip()
    if value == '""':
        return ""
    return value
