# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:15:24 2020

@author: Administrator
"""
import csv
import os 

i=0
j = 0
path='path'

if __name__ == '__main__': 
    imp = open(+path, 'r',encoding="utf-8")
    #out = open('mycsv.csv' , 'wb')
    #writer = csv.writer(out)
    myCsv = csv.reader(imp, quoting=csv.QUOTE_NONE, quotechar=' ', delimiter=',')
    if not os.path.isdir(path):
        os.mkdir(path)
    for row in myCsv:
            if i == 0:
                out = open(path+str(j)+'.csv','a+',encoding="utf-8", newline='')
                writer = csv.writer(out)
            else:     
                writer.writerow(row)
                #print(str(j)+':'+str(i))
                
            if i == 29999:
                i = -1
                j += 1
            i+=1

    print(j)
    imp.close()
    out.close()