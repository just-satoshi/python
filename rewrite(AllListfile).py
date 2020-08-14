# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os 
import csv
import zipfile

#壓縮
def Achive_Folder_To_ZIP(sFilePath):
    """
    input : Folder path and name
    output: using zipfile to ZIP folder
    """
    #zf = zipfile.ZipFile(sFilePath + '.ZIP', mode='w')#只儲存不壓縮
    zf = zipfile.ZipFile(sFilePath + '.ZIP', mode = 'w', compression = zipfile.ZIP_DEFLATED)#預設的壓縮模式
    os.chdir(sFilePath)
    #print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            #print aFile
            zf.write(aFile)
    zf.close()


filenameDB ='path'
filename='path'

if not os.path.isdir(filenameDB):
    os.mkdir(filenameDB)
for root, dirs, files in os.walk(filename):
    #for name in dirs:
    #    print("目錄--->",os.path.join(root, name))
    for name in files:
        i = 0
        print("檔案--->",os.path.join(root, name))
        f = open(os.path.join(root, name),encoding="utf-8")
        myCsv = csv.reader(f, delimiter='|', quoting=csv.QUOTE_NONE, quotechar=' ')
        #myCsv = csv.reader(f, quoting=csv.QUOTE_NONE, quotechar=' ')
        headers = next(myCsv)
        f2 = open(filenameDB+name.replace('.csv', '.json'),'a+',encoding="utf-8")
        f2.write('[')
        for rows in myCsv:  
            i+=1
            #Debug
            #print(name+':'+str(i))
            if rows[0]== '' :
                print(os.path.join(root, name)+':'+str(i)+":null")
            else:                       
                #CsvRemoveReplace
                row = [item.replace(r'"', r'\"').replace('，', ',').replace('\t','') for item in rows]    
                #DBFunction
                DBFunction = ()
                #print('\033[1;3'+str(i%8)+'m'+name+':'+str(i)+':'+str(rows[0])+'\033[0m')
                if i!=1: f2.write(',')
                
                #writeDBFunction
                f2.write(DBFunction)   

        f2.write(']')  
        f2.close()  
        f.close()
    #print(len(df))
        
#壓縮路徑
Achive_Folder_To_ZIP(filenameDB)     
        
 