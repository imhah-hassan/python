import glob
import os
import time
import datetime
import pymysql

class Fichier:
    def __init__(self, nom, chemin, creation, modification, size):
        self.nom = nom
        self.chemin = chemin
        self.creation = datetime.datetime.strptime(creation, '%a %b  %d %H:%M:%S %Y')
        self.modification = datetime.datetime.strptime(modification, '%a %b  %d %H:%M:%S %Y')
        self.size = size

def InsertFile (fichier):
    conn = pymysql.connect(host='localhost', user='root', passwd=None, db='locatedb')
    query = "INSERT INTO files(fullname, path, creation, modification, sizebytes, sizeko, sizemo) " \
            "VALUES(%s, %s, %s, %s, %s, %s, %s)"
    args = (fichier.nom, fichier.chemin, fichier.creation, fichier.modification, fichier.size, fichier.size / 1024,
           fichier.size / 1024 / 1024)
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    cur.close()
    conn.close()


path='J:\\Music\\'
index = 1
for filename in glob.iglob(path + '**\\*.mp3', recursive=True):
    print("\r ( " + str(index) + " )" + filename, end=" ")
    index += 1
    info = os.stat(filename)
    fic = Fichier(os.path.basename(filename),
                    path,
                    time.ctime(os.path.getctime(filename)),
                    time.ctime(os.path.getmtime(filename)),
                    info.st_size)
    InsertFile(fic)





