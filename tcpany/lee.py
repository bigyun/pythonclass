#!/usr/bin/python
# -*- coding: UTF-8 -*-

#获取联通，电信和移动ip数据包占比和ip数占比
import os, sys

re={'dianxin':0,'liantong':0,'yidong':0 ,'tietong':0,'other':0,'all':0}
re_packet={'dianxin':0,'liantong':0,'yidong':0 ,'tietong':0,'other':0,'all':0}
 
tcpfile = open('tcp.txt')
ipfile = open('ips.txt','r',True)
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
		#print len(l)
		#exit()
		start = Ip2long(l[0])
		end = Ip2long(l[1])
		c = l[len(l)-1]
		#print c
		ips.append([start,end,c])
    except Exception,e:
		#pass
        print (str(e))+"    E1"
#print len(ips)
#print ips[1]
#exit()
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
        TargetIndex = BinarySearch(ips,longOutIp)
        if TargetIndex!=-1:
			try:
				TargetVal = ips[TargetIndex]
				if "dianxin" in TargetVal[2]:
				    re['dianxin']+=1
				    re_packet['dianxin']+=length
				    re['all']+=1
				    re_packet['all']+=length
				elif "liantong" in TargetVal[2]:
				    re['liantong']+=1
				    re_packet['liantong']+=1
				    re['all']+=1
				    re_packet['all']+=length
				#elif "yidong" in TargetVal[2]:
				#    re['yidong']+=1
				#	 re['all']+=1
				#elif "tietong" in TargetVal[2]:
				#	re['tietong']+=1
				#	re['all']+=1
				else:
				    re['other']+=1
				    re_packet['other']+=length
				    re['all']+=1
				    re_packet['all']+=length
			except Exception,e:
				#pass
				print (str(e))+"    E3"
    except Exception,e:
		#pass
        print (str(e))+"   E2"
    i+=1
tcpfile.close()
ipfile.close()
print re
print "dianxin_ip:",re['dianxin']*1.0/re['all'],"liantong_ip:",re['liantong']*1.0/re['all'],"other_ip:",re['other']*1.0/re['all']

print "dianxin_packet:",re_packet['dianxin']*1.0/re_packet['all'],"liantong_packet:",re_packet['liantong']*1.0/re_packet['all'],"other:",re_packet['other']*1.0/re_packet['all']



