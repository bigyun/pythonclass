#!/usr/bin/python
# coding: utf-8
import redis
import time

'''
登录系统和购物车@lee

'''


class Login():
    def __init__(self):
        self.conn = redis.Redis(host='localhost', port=6379, password=123456, db=0)
        self.one_day = 86400
        self.vote_score =55
        self.per_page = 25
    #获取令牌的用户
    def check_token(self,token):
        return self.conn.hget('login:',token)
    #更新令牌和浏览商品(item商品id)
    def update_token(self,token,user,item=None):
        timenow = time.time()
        self.conn.hset('login:',token,user)
        self.conn.zadd('recent:',token,timenow)
        #记录用户浏览的商品和保留25个商品
        if item:
            self.conn.zadd('viewd:' +   token,item,timenow)
            self.conn.zremrangebyrank('viewd:' + token,0,-26)
    #添加购物车
    def add_to_cart(self,session,item,count):
        if count <= 0:
            self.conn.hrem('cart:'+session,item)
        else:
            self.conn.hset('cart:'+session,item,count)



login = Login()

#更新令牌和浏览商品
#print login.update_token('123','lee',1)


#获取令牌的用户
print login.check_token('123')

