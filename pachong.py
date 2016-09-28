# coding: utf-8
import urllib2
#import BeautifulSoup
import re
import chardet
import sys
import urllib2
from bs4 import BeautifulSoup

#设置默认encoding方式
import sys
reload(sys)
sys.setdefaultencoding('gbk')
#抓取静态内容
def Fetch_Static(url):
    up=urllib2.urlopen(url)#打开目标页面，存入变量up
    content=up.read()#从up中读入该HTML文件
    key1="喜欢"#设置关键字1
    key2="喜欢"#设置关键字2
    pa=content.find(key1)#找出关键字1的位置
    pt=content.find(key2,pa)#找出关键字2的位置(从字1后面开始查找)
    urlx=content[pa:pt]#得到关键字1与关键字2之间的内容(即想要的数据)
    typeEncode = sys.getfilesystemencoding()##系统默认编码
    infoencode = chardet.detect(content).get('encoding','utf-8')
    html = content.decode(infoencode,'ignore').encode(typeEncode)
    return html

'''
首先打开火狐打开动态网页“http://beian.hndrc.gov.cn/indexinvestment.jsp?id=162518;
f12调试—网络可以查看到真正的内容;
我们看到是http://beian.hndrc.gov.cn/indexinvestment.action
然后根据编号就可以打开真实的地址http://beian.hndrc.gov.cn/indexinvestment.action?id=162518;
下面我们就可以抓取了
'''
#抓取动态内容(有的网页利用ajax从后台调用可以用火狐看到)

def Fetch_Dynamicic(url):
    up=urllib2.urlopen(url)#打开目标页面，存入变量up
    content=up.read()#从up中读入该HTML文件
    key1="喜欢"#设置关键字1
    key2="喜欢"#设置关键字2
    pa=content.find(key1)#找出关键字1的位置
    pt=content.find(key2,pa)#找出关键字2的位置(从字1后面开始查找)
    urlx=content[pa:pt]#得到关键字1与关键字2之间的内容(即想要的数据)
    typeEncode = sys.getfilesystemencoding()##系统默认编码
    infoencode = chardet.detect(content).get('encoding','utf-8')
    html = content.decode(infoencode,'ignore').encode(typeEncode)
    return html
#if __name__ == '__main__':
#    try:
#        #print Fetch_Static("http://mm.taobao.com/json/request_top_list.htm?type=0&page=1")
#        print  Fetch_Static("http://beian.hndrc.gov.cn/indexinvestment.action?id=162518")
#    except Exception, ex:
#         print Exception, ":", ex
'''
正如“不论是静态网页，动态网页，模拟登陆等，都要先分析、搞懂逻辑，再去写代码”所说，编程语言只是一个工具，
重要的是解决问题的思路。有了思路，再寻找趁手的工具去解决，就OK了。
'''
'''
#file = open('webdata.txt','a')
#line = paper_name + '#' + paper_author + '#' + paper_desc + '#' + citeTimes + '\n'
# 对象file的write方法将字符串line写入file中
#file = file.write(line)
# 再一次的，做个随手关闭文件的好青年
#file.close()
'''




url = 'http://news.baidu.com/' #待抓取的网页地址
content = urllib2.urlopen(url).read() #获取网页的html文本
#使用BeautifulSoup解析html
soup = BeautifulSoup(content, from_encoding = 'gbk') 
#识别热点新闻
hotNews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
for i in hotNews:
    print i.a.text #打印新闻标题
    print i.a['href'] #打印新闻链接
