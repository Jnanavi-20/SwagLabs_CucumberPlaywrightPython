import openpyxl

def read_login_data(file, sheet):

    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append({
            "username": row[0],
            "password": row[1],
            "result": row[2]
        })

    return data