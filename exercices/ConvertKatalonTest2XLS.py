import os
from glob import glob
from bs4 import BeautifulSoup
import xlwt

def get_td_content(text):
    start = 0
    text = str(text)
    if ('<td' in text):
        start = text.index('<td')+3
        if ('>' in text):
            start = text.index('>')
        text = text[start:]
        if ('<datalist>' in text):
            text=text[1:text.index('<datalist>')]
        else:
            text = text[1:text.index('</td>')]
    return (text)

def export_katalon_to_xls(wk, file):
    ws = wk.add_sheet(os.path.basename(file))
    f = open(file, 'r')
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser' )
    tables = soup.find_all('table')
    row_index=0
    for table in tables:
        table_head = table.find('thead')
        table_title = table_head.find_all('tr')
        for row in table_title:
            test = row.find_all('td')
            test_name=get_td_content(test[0])
        # Write test name
        ws.write(row_index, 0, test_name)
        row_index=row_index+1
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        col_index=0
        for row in rows:
            cols = row.find_all('td')
            for col in cols:
                td = str(col)
                ws.write(row_index,col_index,get_td_content(td))
                col_index = col_index+1
            col_index=0
            row_index=row_index+1
        row_index=row_index+1


path = 'D:\\DVLP\\php\\credit-auto\\credit-auto\\tests\\katalon\\'
file = "credit-auto.html"
wk = xlwt.Workbook()
export_katalon_to_xls (wk, path + file)
wk.save (path +"credit-auto.xls")


for dir in glob(path+"\\*\\"):
    dirs = dir.split('\\')
    print("Processing directory : ", dir)
    wk = xlwt.Workbook()
    for file in glob(dir + "**\\*.html", recursive=True):
        print(" ---- > Processing file : ", file)
        export_katalon_to_xls (wk, file)
    print(dir + dirs [len(dirs)-2] + ".xls")
    wk.save (dir + dirs [len(dirs)-2] + ".xls")
