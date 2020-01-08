from faker import Factory
import xlwt
import random
from pathlib import Path
import os
xlsFile = "C:\\Formation\\employees.xls"

file = Path("xlsFile")
if file.is_file():
    # file exists
    os.remove (xlsFile)

wk = xlwt.Workbook()
ws= wk.add_sheet("Employes")

fakerFR = Factory.create('fr_FR')
# Première ligne : entête des données
ws.write(0, 0, "last_name")
ws.write(0, 1, "first_name")
ws.write(0, 2, "dateOfBirth")
ws.write(0, 3, "address")
ws.write(0, 4, "email")

for i in range(1, 10000):
    lastName = fakerFR.last_name()
    firstName = fakerFR.first_name()
    ws.write (i, 0, lastName)
    ws.write(i, 1, firstName )
    age=str(round(random.random() * 15) + 20)
    ws.write(i, 2, str(fakerFR.past_date(start_date="-" + age  +"y", tzinfo=None)))
    ws.write(i, 3, fakerFR.address())
    ws.write(i, 4, firstName+"." + lastName+"@" + fakerFR.free_email_domain())

wk.save (xlsFile)