# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:21:30 2020

@author: Administrator
"""

import os
from opencc import OpenCC


filename='path'
outFile='path'
#翻譯文字設定
cc = OpenCC('s2twp')

for root, dirs, files in os.walk(filename):
    for name in dirs:
        print("目錄--->",os.path.join(root, name))
        if not os.path.isdir(outFile+'\\'+name):
            os.mkdir(outFile+'\\'+name)
        for root1, dirs1, files1 in os.walk(root+'\\'+name):
            for fname in files1:
              print("檔案--->",os.path.join(root1, fname))  
              f = open(os.path.join(root1, fname),encoding="utf-8")
              words = f.read()             
              f2 = open(outFile+'\\'+name+'\\'+fname,'a+',encoding="utf-8")
              f2.write(cc.convert(words))
              f2.close()
              f.close()
    for name in files:
        print("檔案--->",os.path.join(root, name))  
        f = open(os.path.join(root, name),encoding="utf-8")
        words = f.read()
        f2 = open(outFile+'\\'+name,'a+',encoding="utf-8")
        f2.write(cc.convert(words))
        f2.close()
        f.close()


#converter = opencc.OpenCC('s2twp.json')
#print(converter.convert('汉字')) # 漢字