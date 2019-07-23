#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
import time
import re

bill_path = r'README.md'
bill_result_path = r'bill_result.txt'
#中文分句，根据一些字符将字符串分成一段一段的，然后统计词频
fr = open(bill_path,'r')
frsen=""
for line in fr:
  frsen+=line[:-1]
  frsen+='!'
fr.close()
sentences = re.split('（|）|、|。|，|：|！|\:|\,|\(|\.|\!|\"|\.|？|\?',frsen)
data = dict(Counter(sentences))
doublelist=[]
with open(bill_result_path,'w') as fw:
	for k,v in data.items():
		if v>1 and len(k)>9:
			fw.write("%s,%d\n" % (k,v))
			doublelist.append(k)
print doublelist
#对原文件中重复的部分进行去重，写入新文件
linelist = []
fxx = open("README.md","r")
fw = open("README1.md","w")
for line in fxx:
    res=0
    for one in doublelist:
        if line.find(one) >= 0:
            res = 1
            linelist.append(line)
            break;
    if res==0 and len(line)>2:
        fw.write(line+"\n")
fxx.close()

for one in doublelist:
    i=0
    ii=0
    while ii <len(linelist):
        if linelist[ii].find(one)>=0 and i==0:
            i=1
            fw.write(linelist[ii]+"\n")
            del linelist[ii]
        elif linelist[ii].find(one)>=0 and (linelist[ii].find("A")>0 or linelist[ii].find("B")>0 or linelist[ii].find("C")>0 or linelist[ii].find("D")>0):
            fw.write(linelist[ii]+"\n")
            del linelist[ii]
        else:
            ii+=1

fw.close()



