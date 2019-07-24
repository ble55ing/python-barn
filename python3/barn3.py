#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 比较两个字符串前面相等的长度
def cmpstreq(str1,str2):
    if len(str1)>len(str2):
        tmp = str1
        str1 = str2
        str2 = tmp
    low =0;
    high = len(str1)+1
    i = (low + high) / 2
    while i>low and i<high:
        if str2.find(str1[:i])==0:
            low = i
        else:
            high=i
        i = (low + high) / 2
    return i

#两个字符串异或，得到新的字符串
def stringxor(str1,str2):
    orxstr=""
    for i in range(0,len(str2)-1):
        rst=ord(list(str1)[i])^ord(list(str2)[i])
        orxstr=orxstr+ chr(rst)
    return orxstr

#开次方根
def sqrtt(n,e):
    qt=n**(1.0/e);
    z=int(qt);
    c=z;
    ee=0;
    while c>0:
        c = c // 16;
        ee = ee +1;
    c=1;
    while ee>1:
        ee = ee-1;
        c = c * 16;
    #zx = 0x10000000000000000000000000000000000000000000000000;
    zx=c;
    while(1):
        z=z+zx;
        while(pow(z,e)<n):
            z=z+zx;
        if pow(z,e)==n:
            print ("%x"%(z));
            break;
        z=z-zx;
        zx=zx//16;
    return z

