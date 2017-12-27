import win32com.client
# https://wikidocs.net/3645
# 엑셀 다루기....


excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('D:\\Python\\temp\\test.xlsx')
ws = wb.ActiveSheet

ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10