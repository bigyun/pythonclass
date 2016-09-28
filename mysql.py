#!/usr/bin/python
#coding=utf-8
import MySQLdb
import sys
import re
import pycurl
import StringIO
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')


class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf
#数据库操作类
class Mysql():
    def __init__(self,host,port,user,passs,db):
        self.conn=MySQLdb.connect(host=host,user=user,passwd=passs,db=db,charset="utf8")
    def get(self,sql):
        if self.conn:
            cur = self.conn.cursor()
            cur.execute(sql)
            rows = cur.rowcount
            cur.close()
            return rows
    def get_all(self,sql):
        if self.conn:
            cur = self.conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            cur.close()
            return results
    def update(self,sql):
        if self.conn:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return 1
    def delete(self,sql):
        if self.conn:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return 1
    def add(self,sql):
        if self.conn:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return 1
    def close(self):
        self.conn.close()



#得到文件中的sn号生成列表

sn_list = []
sn_list_no = []
def get():
    f = open('product.txt','r')
    for i in  f:
        #去除空行
        if not i[:-1].strip():
            pass
        else:
            sn_list.append(i[:-2])
    f.close()
#查询等于outfile中的
def in_goods():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="olddgc",charset="utf8")
    if conn:
        f = open('outfile','r')
        for i in  f:
            print i.strip()
            cur=conn.cursor()
            #sql = 'select * from nq_goods where goods_sn = "%s"' % i.strip()
            sql = 'select * from nq_goods where goods_sn = "123"'
            cur.execute(sql)
            rows = cur.rowcount
            print rows
            cur.close()

        conn.close()

#调用图片服务生成图片
#得到图片地址和goods_id
data_list=[]
data_new_list=[]
def get_img_goods():
    conn = Mysql("192.168.1.16","3306","root","htu.cc","dgc_New")
    sql = 'select goods_id,goods_desc from dgc_goods where goods_desc like "%old.dagongchang.com%"'
    data =  conn.get_all(sql)
    for line in data:
        #print line[0]
        img = re.compile(r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>""", re.I)
        m = img.findall(line[1])
        m.insert(0,line[0])
        data_list.append(m)
    conn.close()
#生成新图片和goods_id
url_list = 'http://newimg.dagongchang.com/photohander.php?fld=lee'
def get_new_img():
    for imgs in data_list:
        goodsid = imgs[0]
        img = imgs[1:]
        print goodsid
        for line in img:
            print line
            post_data_dic = {"fileimg": line}
            crl = pycurl.Curl()
            crl.setopt(pycurl.VERBOSE, 1)
            crl.setopt(pycurl.FOLLOWLOCATION, 1)
            crl.setopt(pycurl.MAXREDIRS, 5)
            crl.setopt(pycurl.CONNECTTIMEOUT, 60)
            crl.setopt(pycurl.TIMEOUT, 300)
            crl.setopt(pycurl.HTTPPROXYTUNNEL, 1)
            # crl.setopt(pycurl.NOSIGNAL, 1)
            crl.fp = StringIO.StringIO()
            crl.setopt(pycurl.USERAGENT, "dhgu hoho")
            crl.setopt(crl.POSTFIELDS, urllib.urlencode(post_data_dic))
            crl.setopt(pycurl.URL, url_list)
            crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
            crl.perform()
            the_page = crl.fp.getvalue()
            crl.close()
            print the_page
            exit()



if __name__=="__main__":
        get_img_goods()
        get_new_img()



    #print "未导入列表:"+str(sn_list_no)+"数量"+str(len(sn_list_no))