#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

re={'henan':0,'shandong':0,'jiangsu': 0,'anhui': 0,'zhejiang': 0,'fujian': 0,'shanghai': 0,'guangdong': 0,'guangxi': 0,'hainan': 0,\
'hubei': 0,'hunan': 0,'jiangxi': 0,'beijing': 0,'tianjin': 0,'hebei': 0,'shanxi': 0,'neimenggu': 0,'ningxia': 0,'xinjiang': 0,\
'qinghai': 0,'shanxi2': 0,'gansu': 0,'sichuan': 0,'yunnan': 0,'guizhou': 0,'xizang': 0,'chongqing': 0,'liaoning': 0,'jilin': 0,\
'heilongjiang': 0,'taiwan': 0,'xianggang': 0,'aomen': 0,'other':0,'all':0}
re2={'hunan':0,'all':0}
 
reip={'henan':'','shandong':'','jiangsu': '','anhui': '','zhejiang': '','fujian': '','shanghai': '','guangdong': '','guangxi': '','hainan': '',\
'hubei': '','hunan': '','jiangxi': '','beijing': '','tianjin': '','hebei': '','shanxi': '','neimenggu': '','ningxia': '','xinjiang': '',\
'qinghai': '','shanxi2': '','gansu': '','sichuan': '','yunnan': '','guizhou': '','xizang': '','chongqing': '','liaoning': '','jilin': '',\
'heilongjiang': '','taiwan': '','xianggang': '','aomen': ''}
tcpfile = open('gs.txt')
ipfile = open('ips.txt','r',True)
reipf = open('reip.txt','w')
ips = []
i=0

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
		c = l[2]
		ips.append([start,end,c])
    except Exception,e:
		#pass
        print (str(e))+"    E1"
#print len(ips)
for line in tcpfile.readlines():
    try:
        lines=line.split(' ')
        outSocket = lines[2]
        os=outSocket.split(".")
        out = os[0]+"."+os[1]+"."+os[2]+"."+os[3]
        length = int(lines[len(lines)-1])
        #print str(i)+"  "+str(length)
        #print re
        longOutIp = Ip2long(out)
        re['all']+=length
        TargetIndex = BinarySearch(ips,longOutIp)
        if TargetIndex!=-1:
			try:
				TargetVal = ips[TargetIndex]
				if "hunan" in TargetVal[2]:
				    re['hunan']+=length
				    reip['hunan']+=lines[2]+' '+str(length)+','
				elif "henan" in TargetVal[2]:
				    re['henan']+=length
				    reip['henan']+=lines[2]+' '+str(length)+','
				elif "shandong" in TargetVal[2]:
				    re['shandong']+=length
				    reip['shandong']+=lines[2]+' '+str(length)+','
				elif "jiangsu" in TargetVal[2]:
				    re['jiangsu']+=length
				    reip['jiangsu']+=lines[2]+' '+str(length)+','
				elif "anhui" in TargetVal[2]:
				    re['anhui']+=length
				    reip['anhui']+=lines[2]+' '+str(length)+','
				elif "zhejiang" in TargetVal[2]:
				    re['zhejiang']+=length
				    reip['zhejiang']+=lines[2]+' '+str(length)+','
				elif "fujian" in TargetVal[2]:
				    re['fujian']+=length
				    reip['fujian']+=lines[2]+' '+str(length)+','
				elif "shanghai" in TargetVal[2]:
				    re['shanghai']+=length
				    reip['shanghai']+=lines[2]+' '+str(length)+','
				elif "guangdong" in TargetVal[2]:
				    re['guangdong']+=length
				    reip['guangdong']+=lines[2]+' '+str(length)+','
				elif "guangxi" in TargetVal[2]:
				    re['guangxi']+=length
				    reip['guangxi']+=lines[2]+' '+str(length)+','
				elif "hainan" in TargetVal[2]:
				    re['hainan']+=length
				    reip['hainan']+=lines[2]+' '+str(length)+','
				elif "hubei" in TargetVal[2]:
				    re['hubei']+=length
				    reip['hubei']+=lines[2]+' '+str(length)+','
				elif "hunan" in TargetVal[2]:
				    re['hunan']+=length
				    reip['hunan']+=lines[2]+' '+str(length)+','
				elif "jiangxi" in TargetVal[2]:
				    re['jiangxi']+=length
				    reip['jiangxi']+=lines[2]+' '+str(length)+','
				elif "beijing" in TargetVal[2]:
				    re['beijing']+=length
				    reip['beijing']+=lines[2]+' '+str(length)+','
				elif "tianjin" in TargetVal[2]:
				    re['tianjin']+=length
				    reip['tianjin']+=lines[2]+' '+str(length)+','
				elif "hebei" in TargetVal[2]:
				    re['hebei']+=length
				    reip['hebei']+=lines[2]+' '+str(length)+','
				elif "shanxi" in TargetVal[2]:
				    re['shanxi']+=length
				    reip['shanxi']+=lines[2]+' '+str(length)+','
				elif "neimenggu" in TargetVal[2]:
				    re['neimenggu']+=length
				    reip['neimenggu']+=lines[2]+' '+str(length)+','
				elif "ningxia" in TargetVal[2]:
				    re['ningxia']+=length
				    reip['ningxia']+=lines[2]+' '+str(length)+','
				elif "xinjiang" in TargetVal[2]:
				    re['xinjiang']+=length
				    reip['xinjiang']+=lines[2]+' '+str(length)+','

				elif "qinghai" in TargetVal[2]:
				    re['qinghai']+=length
				    reip['qinghai']+=lines[2]+' '+str(length)+','

				elif "shanxi2" in TargetVal[2]:
				    re['shanxi2']+=length
				    reip['shanxi2']+=lines[2]+' '+str(length)+','

				elif "gansu" in TargetVal[2]:
				    re['gansu']+=length
				    reip['gansu']+=lines[2]+' '+str(length)+','

				elif "sichuan" in TargetVal[2]:
				    re['sichuan']+=length
				    reip['sichuan']+=lines[2]+' '+str(length)+','
	
				elif "yunnan" in TargetVal[2]:
				    re['yunnan']+=length
				    reip['yunnan']+=lines[2]+' '+str(length)+','

				elif "guizhou" in TargetVal[2]:
				    re['guizhou']+=length
				    reip['guizhou']+=lines[2]+' '+str(length)+','

				elif "guangdong" in TargetVal[2]:
				    re['guangdong']+=length
				    reip['guangdong']+=lines[2]+' '+str(length)+','

				elif "xizang" in TargetVal[2]:
				    re['xizang']+=length
				    reip['xizang']+=lines[2]+' '+str(length)+','

				elif "chongqing" in TargetVal[2]:
				    re['chongqing']+=length
				    reip['chongqing']+=lines[2]+' '+str(length)+','

				elif "liaoning" in TargetVal[2]:
				    re['liaoning']+=length
				    reip['liaoning']+=lines[2]+' '+str(length)+','

				elif "jilin" in TargetVal[2]:
				    re['jilin']+=length
				    reip['jilin']+=lines[2]+' '+str(length)+','

				elif "heilongjiang" in TargetVal[2]:
				    re['heilongjiang']+=length
				    reip['heilongjiang']+=lines[2]+' '+str(length)+','

				elif "taiwan" in TargetVal[2]:
				    re['taiwan']+=length
				    reip['taiwan']+=lines[2]+' '+str(length)+','

				elif "xianggang" in TargetVal[2]:
				    re['xianggang']+=length
				    reip['xianggang']+=lines[2]+' '+str(length)+','

				elif "aomen" in TargetVal[2]:
				    re['aomen']+=length
				    reip['aomen']+=lines[2]+' '+str(length)+','

				else:
				    re['other']+=length
			except Exception,e:
				#pass
				print (str(e))+"    E3"
    except Exception,e:
		#pass
        print (str(e))+"   E2"
    i+=1
tcpfile.close()
ipfile.close()
print "gs:"
print re
reipf.write(str(reip))
reipf.close()


