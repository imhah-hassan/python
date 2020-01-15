SET PY=C:\Program Files\Python37
SET PATH=%PY%;%PATH%
del D:\APPS\Jenkins\workspace\OrangePy\*.xml
D:
CD D:\pCloud\sync\Acial2019\python\selenium
taskkill /F /IM chromedriver.exe 

py testsuite_tnr.py
