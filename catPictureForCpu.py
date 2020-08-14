# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:04:11 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:00:26 2020

@author: Administrator
"""
from multiprocessing import Pool
import multiprocessing
import csv
import requests 
from os.path import getsize
import pandas as pd
from tqdm import tqdm
import os
import time
DownloadFilePath = 'path
DownloadUrlPath = 'path'
cpus = multiprocessing.cpu_count()
#df = pd.read_csv(DownloadUrlPath,encoding="utf-8",delimiter='|')
#progress = tqdm(total=len(df)) 

def fileTextErr(FileName,e,row):
    errLog = open(DownloadFilePath+'errLog.csv','a+',encoding="utf-8", newline='') 
    writerErr = csv.writer(errLog)
    print(FileName+':error')
    print(e)
    reErr=[e]
    writerErr.writerow(row+reErr)
    errLog.close()

def fileSizeErr(FileName,size,row):
    errSizeLog = open(DownloadFilePath+'errSizeLog.csv','a+',encoding="utf-8", newline='')
    writerSize = csv.writer(errSizeLog)  
    print('%s = %d bytes' % (FileName, size))
    os.remove(FileName)
    writerSize.writerow(row)
    errSizeLog.close()

def fileDLErr(FileName,row):
    errDLLog = open(DownloadFilePath+'errDLLog.csv','a+',encoding="utf-8", newline='')
    writerDL = csv.writer(errDLLog) 
    print(FileName,"DLErr")
    writerDL.writerow(row)   
    errDLLog.close()     

def logfile(rename):
    f = open(DownloadFilePath+'fileSucLog.txt')
    if rename == f.read().replace(' ',''):
        return True
    else:
        return False

def mainDownload(DownloadFilePath,DownloadUrlPath):    
    i=0
    with open(DownloadUrlPath,encoding="utf-8") as f:   
        myCsv = csv.reader(f, delimiter='|')
        headers = next(myCsv)           
        for row in myCsv:   
            i+=1
            #progress.update(1)     
            try:
                #SettingFilePath
                rename = str(row[2]).replace('\\','_Bac_').replace('/','_Sla_').replace(':','_Col_').replace('*','_Ast_').replace('?','_Que_').replace('"','_Dou_').replace('<','_Les_').replace('>','_Mor_').replace('|','_Str_')
                FileName = DownloadFilePath+rename+'.jpg'              
                url = str(row[2]).replace(' ', '%20')
                if ".jpg" in url:
                    t0 = time.time()
                    with open(FileName, 'wb') as f2:               
                        f2.write(requests.get(url,stream=True).content)
                        f2.close() 
                        print(time.time() - t0)
                    #fileSizeErr
                    size = getsize(FileName)
                    if size <=2048:
                        fileSizeErr(FileName,size,row)
                else:
                    #fileDLErr
                     fileDLErr(FileName,row)                          
            except Exception as e:
                #fileTextErr
                fileTextErr(FileName,e,row)
            time.sleep(1)
            if i ==100: break
                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    f.close()
    
if __name__ == '__main__': 
    cpus = multiprocessing.cpu_count()
    pool = Pool(cpus-1)
    pool.apply_async(mainDownload(DownloadFilePath,DownloadUrlPath))
    pool.close()
    pool.join()