#!/usr/bin/python 
# coding: utf-8
from __future__ import division #整数相除有小数点
import sys, os, urllib2, json
reload(sys) 
sys.setdefaultencoding('utf8')  
import datetime

#此程序处理省份和访问量，得出省份，访问量和访问比率
city_all={} 
fh = open("/data/python/city.txt", "r").readlines()                                                               #我的是把日志和代码在一个目录下面
for line in fh:
      name = line.split(" ")[0]
      num =  line.split(" ")[1]
      city_all[name] = int(num)
list_all = city_all.values()
all = reduce(lambda x,y:x+y,list_all) #得到访问总量
print all
all = all
f = file('photo.txt','a')
f.write("访问者位置"+" "+"访问量"+" "+"访问比率")
f.write("\n")
for key in city_all:
    print  key + " " +str(city_all[key]) + " " +  str(round(city_all[key]/all*100,2))+"%"
    gg=key + " " +str(city_all[key]) + " " +  str(round(city_all[key]/all*100,2))+"%"
    f.write(gg)
    f.write("\n")
f.close()