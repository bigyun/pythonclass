#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb
import sys
import re
import pycurl
import StringIO
import urllib,json

'''
实现操作数据库省市区生成json格式
'''
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
Province=[] #省
City={}#市
City_temp=[]
Country={}#区
Country_temp=[]
if __name__=="__main__":
    data = Mysql("192.168.1.16",3306,"root","htu.cc","dgc_New")
    #得到省份
    '''
    sql = 'select area_id,area_name,area_parent_id from dgc_area where area_deep=1'
    for line in data.get_all(sql):
        Province.append({"id":line[0],"name":line[1],"pid":line[2]})
    '''
    #print json.dumps(Province)
    #得到市区
    '''
    sql_temp = 'select area_id from dgc_area where area_deep=1'
    for line in  data.get_all(sql_temp):
        sql2 = 'select area_id,area_name,area_parent_id from dgc_area where area_parent_id=%d' % line[0]
        for j in data.get_all(sql2):
            City_temp.append({"id":j[0],"name":j[1],"pid":j[2]})
        City[line[0]] = City_temp
        City_temp=[]
    '''
    #print json.dumps(City)
    #得到地区
    sql_temp2 = 'select area_id from dgc_area where area_deep=2'
    for line in data.get_all(sql_temp2):
        sql3 = 'select area_id,area_name,area_parent_id from dgc_area where area_parent_id=%d' % line[0]
        for k in data.get_all(sql3):
            Country_temp.append({"id": k[0], "name": k[1], "pid": k[2]})
        Country[line[0]] = Country_temp
        Country_temp = []
    print json.dumps(Country)



