# coding:utf-8
import cookielib,sys
import mechanize
import urllib
import urllib2
import re
import sys
reload(sys)
#from pytesser import *
sys.setdefaultencoding("utf-8")
# 防止中文报错


'''模拟登录大工厂erp后台'''
#loginurl = 'http://192.168.1.196:8013/AdminUser/ValidateLogon'#erp后台
loginurl='http://192.168.1.196/zentao/user-login.html' #禅道
logindomain = 'http://192.168.1.196/'

class Login(object):
    def __init__(self):
        self.adminName = ''
        self.adminPwd = ''
        self.domain = ''
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
    def setLoginInfo(self,adminName,adminPwd ,domain):
        '''设置用户登录信息'''
        self.adminName = adminName
        self.adminPwd = adminPwd
        self.domain = domain
    def login(self):
        '''登录网站'''
        loginparams = {'domain':self.domain,'account':self.adminName, 'password':self.adminPwd}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)
        response = urllib2.urlopen(req)
        thePage = response.info()#打印cookie信息
        #thePage = response.read()
        #print thePage
    def get_info(self,urlinfo):
        ''' 得到列表信息'''
        response2 = urllib2.urlopen(urlinfo)
        print response2.read()

if __name__ == '__main__':
        userlogin = Login()
        username = 'lilongfei'
        password = '123456789'
        domain = logindomain
        userlogin.setLoginInfo(username,password,domain)
        userlogin.login()
        #userlogin.get_info('http://192.168.1.196/zentao/bug-browse-2-0-unconfirmed-0.html')


#以上是动态生成验证码的网址
#image = Image.open('test.tif')  # Open image object using PIL
#print image_to_string(image)     # Run tesseract.exe on image


