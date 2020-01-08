import xlwt
from faker import Faker
myFactory = Faker()


wk = xlwt.Workbook()
ws = wk.add_sheet("Employes")

ws.write(0, 0, "FirstName")
ws.write(0, 1, "LastName")


for row in range(1,10):
    ws.write (row, 0, myFactory.first_name())
    ws.write (row, 1, myFactory.last_name())

wk.save ("C:\\Formation\\exercice15.xls")