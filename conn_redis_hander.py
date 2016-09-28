#!/usr/bin/python
# coding: utf-8
import redis

class Redis_Hander():
    def __init__(self):
        self.conn = redis.Redis(host='localhost', port=6379, password=123456, db=0)
        self.num = 500
        self.max = 10
    #字符串类型
    def Str(self,key,value):
        if self.conn.get(key):
            if self.conn.get(key) < 5:
                self.conn.incr(key,5)
            else:
                self.conn.decr(key, 5)
            return self.conn.get(key)
        else:
            self.conn.set(key,value)
    #列表类型
    def List_hander(self,key,value):
        if len(self.conn.lrange(key,0,-1)) < self.max:
            if value >= self.num:
                self.conn.rpush(key, value)
            else:
                self.conn.lpush(key, value)
        else:
            if value >= self.num:
                self.conn.rpop(key)
            else:
                self.conn.lpop(key)
        return self.conn.lrange(key,0,-1)
    #集合类型
    def Gather(self,key,*arg):
        if self.conn.scard(key) < 5:
            self.conn.sadd(key,arg)
        else:
            self.conn.srem(key,arg)
        return  self.conn.scard(key)
    #散列或哈希
    def Hash(self,key,dicts):
        return self.conn.hmset(key,dicts)
    #有序集合
    def Order_Gather(self,key):
        return self.conn.zadd(key,'a',12,'b',45)



hander = Redis_Hander()
#print hander.Str('lee',123)
#print hander.List_hander('zhang',567)
nums = [1,23,45,34]
#print hander.Gather('zhang:',567,34,23,12,54)

#print hander.Hash('hash',{'name':'lee','age':18})
print hander.Order_Gather('order_gather:')



