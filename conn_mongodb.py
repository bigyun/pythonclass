#!/usr/bin/python
# coding: utf-8
import pymongo
import random,datetime


class DBConn():
    servers = "127.0.0.1"
    port = 27017
    def connect(self):
        self.conn = pymongo.MongoClient(self.servers)
        dbs = self.conn.test
        dbs.authenticate("user","pass")
        return dbs
    def get(self):
        return self.connect()
        #return conn.collection_names()
    def insert(self,new_post):
        conn = self.get()
        posts = conn.post#(post为表名字,如果不存在会新建)
        posts.insert(new_post)
    def update(self,name):
        conn = self.get()
        conn.update({name:"newname"},post)
    def get_item(self):
        conn = self.get()
        posts = conn.post
        return posts.find()
    def delete(self,id):
        conn = self.get()
        posts = conn.post
        posts.remove({"AccountID": 22, "UserName": "libing"})
    def close(self):
        return self.conn.disconnect()

if __name__ == '__main__':
    try:
        dbconn = DBConn()
        new_post = {"AccountID": 22, "UserName": "libing", 'date': datetime.datetime.now()}
        result = dbconn.get_item()
        for item in result:
            print item
        #print u'所有聚集:',conn.collection_names()
        new_posts = [{"AccountID":22,"UserName":"liuw",'date':datetime.datetime.now()},
             {"AccountID":23,"UserName":"urling",'date':datetime.datetime.now()}]#每条记录插入时间都不一样
    except Exception as ex:
        print(ex)