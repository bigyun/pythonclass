#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

re={'dianxin':0,'liantong':0,'other':0,'all':0}
 
reip={'dianxin':'','liantong':'','other':''}
tcpfile = open('tcp.txt')
ipfile = open('ips.txt','r',True)
reipf = open('reip.txt','w')
ips = []
i=0
j=56

def Ip2long(ip_str):
    '''把字符串形式的IP地址转换成long int 形式'''
    ips=ip_str.split('.')
    ip_long=int(ips[3])+int(ips[2])*256+int(ips[1])*(256**2)+int(ips[0])*(256**3)
    return ip_long
def BinarySearch(lists, target): 
    low = 0
    high = len(lists) - 1
 
    while low <= high:
        mid = (low + high) // 2
        midVal = lists[mid]
 
        if midVal[1] < target:
            low = mid + 1
        elif midVal[0] > target:
            high = mid - 1
        else:
            return mid
    return -1

for line in ipfile.readlines():
    try: 
		l = line.split(' ')
		start = Ip2long(l[0])
		end = Ip2long(l[1])
		ips.append([start,end,line])
    except Exception,e:
		#pass
        print (str(e))+"    E1"

print len(ips)

for line in tcpfile.readlines():
    try:
        lines=line.split(' ')
        #outSocket = lines[3]
        outSocket = lines[2]
        os=outSocket.split(".")
        out = os[0]+"."+os[1]+"."+os[2]+"."+os[3]
        #length =int(line.split('length ')[1].split(',')[0])
        length = int(lines[len(lines)-1])
        longOutIp = Ip2long(out)
        TargetIndex = BinarySearch(ips,longOutIp)
        if TargetIndex!=-1:
			try:
				TargetVal = ips[TargetIndex]
				if "dianxin" in TargetVal[2]:
					re['dianxin']+=length
					re['dianxin']+=j
					reip['dianxin']+=lines[2]+' '+str(length)+','
				elif "liantong" in TargetVal[2]:
					re['liantong']+=length
					re['liantong']+=j
					reip['liantong']+=lines[2]+' '+str(length)+','
				else:
					re['other']+=length
					re['other']+=j
					reip['other']+=lines[2]+' '+str(length)+','
				re['all']+=length
				re['all']+=j
			except Exception,e:
				#pass
				print (str(e))+"    E3"
    except Exception,e:
		pass
		#print line
    i+=1

tcpfile.close()
ipfile.close()
print re
print "dianxin:",re['dianxin']*1.0/re['all'],"liantong:",re['liantong']*1.0/re['all'],"other:",re['other']*1.0/re['all']
reipf.write(str(reip))
reipf.close()


