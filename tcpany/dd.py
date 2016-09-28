#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

ipfile = open('ips.txt','r',True)
fp = open('test2.txt','w') 
for line in ipfile.readlines():
    try: 
		l = line.split(' ')	
		c = l[len(l)-1]
		#print c
		if 'yidong' in c:
			
			fp.write(line.replace('ÒÆ¶¯yidong','ÒÆ¶¯'))
		
    except Exception,e:
		#pass
        print (str(e))+"    E1"
ipfile.close()	