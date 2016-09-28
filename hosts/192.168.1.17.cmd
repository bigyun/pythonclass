磁盘空间#df -lP | grep -e 'echnweb$' | awk '{print $5}'#<85%
磁盘空间#df -lP | grep -e 'var$' | awk '{print $5}'#<85%
磁盘空间#df -lP | grep -e 'usr$' | awk '{print $5}'#<85%
磁盘空间#df -lP | grep -e '/$' | awk '{print $5}'#<85%
内存#free -m | sed -n '3p' | awk '{printf("%d%\n", 1319/30793*100)}'#<70%
swap使用情况#free -m | awk '{if(NR==4){print $3}}'#=0
openresty1进程存在#ps -ef | grep openresty1naxsi | grep master | wc -l#=2
openresty2进程存在#ps -ef | grep openresty2naxsi | grep master | wc -l#=2
memcached进程存在#ps -ef | grep memcached | grep -v grep | wc -l#=2
端口检查#netstat -na | grep 10001 | grep LISTEN|grep -v grep | wc -l#=1
端口检查#netstat -na | grep 10002 | grep LISTEN|grep -v grep | wc -l#=1
端口检查#netstat -na | grep 10003 | grep LISTEN|grep -v grep | wc -l#=1
端口检查#netstat -na | grep 10004 | grep LISTEN|grep -v grep | wc -l#=1
