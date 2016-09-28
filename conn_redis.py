#!/usr/bin/python
# coding: utf-8
import redis
import time


'''

文章投票系统实现@lee
'''


#文章操作
class Article():
  def __init__(self):
    self.conn = redis.Redis(host='localhost', port=6379, password=123456, db=0)
    self.one_day = 86400
    self.vote_score =55
    self.per_page = 25
  #得到文章
  def get_articles(self,page,order='score:'):
    start = (page-1) * self.per_page
    end = start + self.per_page -1
    ids= self.conn.zrevrange(order,start,end)
    articles = []
    for id in ids:
      article_data = self.conn.hgetall(id)
      article_data['id'] = id
      #得到文章信息保存到列表
      articles.append(article_data)
    return articles

  #发布文章
  def post_articles(self,user,title,link):
    #生成文章唯一id
    article_id = str(self.conn.incr('article:'))
    voted = 'voted:' + article_id
    #把发布文章用户发到已投票名单里
    self.conn.sadd(voted,user)
    self.conn.expire(voted,self.one_day)
    now = time.time()
    article = 'aiticle:' + article_id
    #文章表保存文章投票信息
    self.conn.hmset(article,{
        'title': title,
        'link' :  link,
        'poster:':  user,
        'time:':  now,
        'votes:': 1,
    })
    #将文章保存在根据时间和评分排序的有序集合
    self.conn.zadd('score:',article,now +self.vote_score )
    self.conn.zadd('time:',article,now)
    return article_id
  #文章分组
  def add_remove_groups(self,article_id,to_add=[],to_remove=[]):
    article = 'article:'  + article_id
    #添加文章分组
    for group in to_add:
      self.conn.sadd('group:' + group,article)
    #移出文章
    for group in to_remove:
      self.conn.srem('group:' + group,article)
  #根据评分或时间取出分组中的文章
  def get_group_articles(self,group,page,order='score:'):
    key = order + group + ':'
    print key
    if not self.conn.exists(key):
      print 'group:' + group  + order
      self.conn.zinterstore(key,('group:' + group,order),aggregate='MAX',)
      self.conn.expire(key,60)
    return self.get_articles(page,key)
  #投票
  def vote(self,user,article):
    #投票时间超过一天就不能投
    cutooff = time.time() - self.one_day
    if self.conn.zscore('time:',article) < cutooff:
      return
    article_id = article.partition(':')[-1]
    #用户第一次投票就增加投票数
    if self.conn.sadd('voted:' + article_id,user):
      #评分增加
      self.conn.zincrby('score:',article,self.vote_score)
      #文章表投票增加
      self.conn.hincrby(article,'votes:',1)
      print '成功投票'

article =  Article()
#发布
#print article.post_articles('liu','明天你好','http://www.baidu.com')
#print article.post_articles('zhang','测试','http://www.baidu.com')
#print article.post_articles('liu','这样美','http://www.baidu.com')
'''
print article.post_articles('guo','郭燕','http://www.baidu.com')
print article.post_articles('chen','陈龙','http://www.baidu.com')
print article.post_articles('li','李冬雪','http://www.baidu.com')
print article.post_articles('zhao','赵雨琪','http://www.baidu.com')
'''


#投票
'''
print article.vote('jiang','aiticle:2')
print article.vote('haung','aiticle:2')
print article.vote('mei','aiticle:2')
'''

#分组
'''
print article.add_remove_groups('1',['测试组'])
print article.add_remove_groups('3',['测试组'])
print article.add_remove_groups('5',['测试组'])
print article.add_remove_groups('2',['营销组'])
print article.add_remove_groups('6',['营销组'])
print article.add_remove_groups('2',['qq'])
print article.add_remove_groups('6',['qq'])
'''
print article.add_remove_groups('2',['wangwang'])
print article.add_remove_groups('6',['wangwang'])

#获取分组和排名文章
print article.get_group_articles('wangwang',1)

#获取文章
#print article.get_articles(1)


