#!/usr/bin/python

import glob, os
import re, time, shutil, datetime, codecs, sys, time
import pandas as pd


typeFile = input ('choisir l\'extensions des doublons, ex csv ou avi tous = * :') #['mkv','avi','csv']
source =  input('choisir le chemin de depart, ex /media : ') #'/media/Disk_2/PC/Formation_DEV/_Python'
dico = {}
c = 0
#print (os.name)

for fullPath in glob.glob(source+'/**/*' , recursive=True): #recuper avro a la racine du script
    try :
        c += 1
        #print(fullPath)
        l = fullPath.split('/')  # split le fullPath avec \
        filename = l[-1]  # prend dernier element du split pour n'avoir que le fichier
        ext = str(filename.split('.')[-1])
        #print(ext)
        if typeFile == '*' :
            if filename not in dico.keys():
                dico[filename]={'n': 1, 'fullpath': [fullPath]}
            else :
                dico[filename]['n'] += 1
                dico[filename]['fullpath'].append(fullPath)
        elif ext in typeFile :
            #print(fullPath)
            #print('*** file :', filename)
            if filename not in dico.keys():
                dico[filename]={'n': 1, 'fullpath': [fullPath]}
            else :
                dico[filename]['n'] += 1
                dico[filename]['fullpath'].append(fullPath)
        else :
            pass
    except :
        print('error : ', fullPath)
print('nb fichiers : ',c)

for k,v in dico.items():
    #print(k, v)
    if dico[k]['n'] > 1 :
        print('doublons :', k, v)







