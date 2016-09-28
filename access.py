#!/usr/bin/python 
# coding: utf-8
import sys, os, urllib2, json,re,time
reload(sys) 
sys.setdefaultencoding('utf8')  
import datetime,time
from functools import wraps

#此程序处理nginx日志,得到省份，省份访问量

#判断函数执行时间
def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running %s: %s seconds" %
        (function.func_name, str(t1-t0))
        )
    return result
  return function_timer



ips = {}  #ip作为字典的key，访问次数做value
city_name = {}  #城市作为字典的key，访问次数城市ip次数做value
ipsnew={}
ipfile = open('ips.txt','r',True)
ipss = []  #纯真数据库ip地址



def Ip2long(ip_str):
    '''把字符串形式的IP地址转换成long int 形式'''
    longip=ip_str.split('.')
    ip_long=int(longip[3])+int(longip[2])*256+int(longip[1])*(256**2)+int(longip[0])*(256**3)
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

#获取纯真数据库
for line in ipfile.readlines():
    try:
        l = line.split(' ')
        start = Ip2long(l[0])
        end = Ip2long(l[1])
        ipss.append([start,end,line])
    except Exception,e:
        #pass
        print (str(e))+"    E1"
class Access(object):
    def __init__(self,listdirs):
        self.listdirs = listdirs
    def get_ip(self):        #得到日志中ip和访问次数的字典
        listdir2 = os.listdir(self.listdirs)

        for i in listdir2:
            fh = open(self.listdirs+"/"+i, "r").readlines()  # 我的是把日志和代码在一个目录下面
            print i
            for line in fh:
                if re.search('spider|Googlebot|Yahoo|180.175.93.8|114.95.231.141',line):
                    #print line
                    pass
                else:
                    ip = line.split(" ")[0]
                    if 6 < len(ip) <= 15:
                        ips[ip] = ips.get(ip, 0) + 1
        return ips
    def get_ip_sort(self):
        #降续排序ip和次数
        listdir2 = os.listdir(self.listdirs)
        for i in listdir2:
            fh = open(self.listdirs + "/" + i, "r").readlines()  # 我的是把日志和代码在一个目录下面
            for line in fh:
                if re.search('spider|Googlebot|Yahoo|180.175.93.8|114.95.231.141', line):
                    #print line
                    pass
                else:
                    ip = line.split(" ")[0]
                    if 6 < len(ip) <= 15:
                        ips[ip] = ips.get(ip, 0) + 1
        ipsnew=sorted(ips.iteritems(),key=lambda d:d[1],reverse=True)
        return ipsnew
    def get_ip_area(self):           #得到城市名和访问次数的字典
        try:
            datas = self.get_ip()
            for i in datas:
                TargetIndex = BinarySearch(ipss,Ip2long(i))
                if TargetIndex!=-1:
                    try:
                        TargetVal = ipss[TargetIndex]
                        if "shanghai" in TargetVal[2]:
                            city_name['上海'] = city_name.get('上海', 0) + datas[i]
                        elif "guangdong" in TargetVal[2]:
                            city_name['广东'] = city_name.get('广东', 0) + datas[i]
                        elif "henan" in TargetVal[2]:
                            city_name['河南'] = city_name.get('河南', 0) + datas[i]
                        elif "shandong" in TargetVal[2]:
                            city_name['山东'] = city_name.get('山东', 0) + datas[i]
                        elif "jiangsu" in TargetVal[2]:
                            city_name['江苏'] = city_name.get('江苏', 0) + datas[i]
                        elif "anhui" in TargetVal[2]:
                            city_name['安徽'] = city_name.get('安徽', 0) + datas[i]
                        elif "zhejiang" in TargetVal[2]:
                            city_name['浙江'] = city_name.get('浙江', 0) + datas[i]
                        elif "fujian" in TargetVal[2]:
                            city_name['福建'] = city_name.get('福建', 0) + datas[i]
                        elif "guangxi" in TargetVal[2]:
                            city_name['广西'] = city_name.get('广西', 0) + datas[i]
                        elif "hainan" in TargetVal[2]:
                            city_name['海南'] = city_name.get('海南', 0) + datas[i]
                        elif "hubei" in TargetVal[2]:
                            city_name['湖北'] = city_name.get('湖北', 0) + datas[i]
                        elif "hunan" in TargetVal[2]:
                            city_name['湖南'] = city_name.get('湖南', 0) + datas[i]
                        elif "jiangxii" in TargetVal[2]:
                            city_name['江西'] = city_name.get('江西', 0) + datas[i]
                        elif "beijing" in TargetVal[2]:
                            city_name['北京'] = city_name.get('北京', 0) + datas[i]
                        elif "tianjin" in TargetVal[2]:
                            city_name['天津'] = city_name.get('天津', 0) + datas[i]
                        elif "hebei" in TargetVal[2]:
                            city_name['河北'] = city_name.get('河北', 0) + datas[i]
                        elif "shanxii" in TargetVal[2]:
                            city_name['山西'] = city_name.get('山西', 0) + datas[i]
                        elif "neimenggu" in TargetVal[2]:
                            city_name['内蒙古'] = city_name.get('内蒙古', 0) + datas[i]
                        elif "ningxia" in TargetVal[2]:
                            city_name['宁夏'] = city_name.get('宁夏', 0) + datas[i]
                        elif "xinjiang" in TargetVal[2]:
                            city_name['新疆'] = city_name.get('新疆', 0) + datas[i]
                        elif "qinghai" in TargetVal[2]:
                            city_name['青海'] = city_name.get('青海', 0) + datas[i]
                        elif "shanxi2" in TargetVal[2]:
                            city_name['陕西'] = city_name.get('陕西', 0) + datas[i]
                        elif "gansu" in TargetVal[2]:
                            city_name['甘肃'] = city_name.get('甘肃', 0) + datas[i]
                        elif "sichuan" in TargetVal[2]:
                            city_name['四川'] = city_name.get('四川', 0) + datas[i]
                        elif "yunnan" in TargetVal[2]:
                            city_name['云南'] = city_name.get('云南', 0) + datas[i]
                        elif "guizhou" in TargetVal[2]:
                            city_name['贵州'] = city_name.get('贵州', 0) + datas[i]
                        elif "xizang" in TargetVal[2]:
                            city_name['西藏'] = city_name.get('西藏', 0) + datas[i]
                        elif "chongqing" in TargetVal[2]:
                            city_name['重庆'] = city_name.get('重庆', 0) + datas[i]
                        elif "liaoning" in TargetVal[2]:
                            city_name['辽宁'] = city_name.get('辽宁', 0) + datas[i]
                        elif "jiling" in TargetVal[2]:
                            city_name['吉林'] = city_name.get('吉林', 0) + datas[i]
                        elif "heilongjiang" in TargetVal[2]:
                            city_name['黑龙江'] = city_name.get('黑龙江', 0) + datas[i]
                        elif "taiwan" in TargetVal[2]:
                            city_name['台湾'] = city_name.get('台湾', 0) + datas[i]
                        elif "xianggang" in TargetVal[2]:
                            city_name['香港'] = city_name.get('香港', 0) + datas[i]
                        elif "aomen" in TargetVal[2]:
                            city_name['澳门'] = city_name.get('澳门', 0) + datas[i]
                        else:
                            pass
                    except Exception,e:
                        #pass
                        print (str(e))+"    E3"
            return city_name
        except Exception as ex:
            print(ex)
    def save_file(self,file_dir):
        try:
            datas=self.get_ip_area()
            f = file(file_dir + 'city.txt', 'w')#先清空数据
            f.close()
            for key in datas:
                gg = key+" "+str(city_name[key])
                f = file(file_dir+'city.txt','a')
                print gg
                continue
                f.write(gg)
                f.write("\n")
                f.close()
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    accesss=Access('/data/python/new')
    #print accesss.get_ip_sort()#按倒叙排序
    accesss.get_ip()
    accesss.get_ip_area()
    accesss.save_file('/data/python/')