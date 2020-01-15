import glob
import os
from PyPDF2 import PdfFileReader

def rename (file, text):
    if (text in file):
        os.rename(file, file.replace(text, ""))
        file = file.replace(text, "")
    return file

def clean(file):
    file = rename (file, "[ torrent ]")
    return (file)

folder ="D:\\Temp\\eBook\\"
for file in glob.glob(folder + "*.epub"):
    print (clean (file))

