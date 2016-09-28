#!/usr/bin/env python
#coding=utf-8
import MySQLdb
import memcache
import sys
import time
def get_data(mysql_conn):
    mc = memcache.Client(['127.0.0.1:12211'],debug=1)
    t1 =time.time()
    value = mc.get('lee')
    if value == None:
        t1 = time.time()
        print t1
        query = "select session_key,session_data from django_session"
        cursor= mysql_conn.cursor()
        cursor.execute(query)
        item = cursor.fetchone()
        t2 = time.time()
        print t2
        t = round(t2-t1)
        print "from mysql cost %s sec" %t
        print item
        mc.set('lee',item,60)
    else :
        t2 = time.time()
        t=round(t2-t1)
        print "from memcache cost %s sec" %t
        print value
if __name__ =='__main__':
    mysql_conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='newbigdata',port=3306,charset='utf8')
    get_data(mysql_conn)
