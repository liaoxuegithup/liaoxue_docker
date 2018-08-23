停止老版本Mongodb

1
2
>use admin
>db.shutdownServer();
下载解压新版本Mongodb

1
2
3
4
wget https://fastdl.mongodb.org/linux/mongodb-linux-i686-3.0.2.tgz
gzip -d mongodb-linux-i686-3.0.2.tgz
tar xvf mongodb-linux-i686-3.0.2.tar
mv mongodb-linux-i686-3.0.2 mongodb3.0.2
创建两个目录

1
2
mkdir data
mkdir logs
把老版本的Mongodb配置文件拷贝到新Mongodb目录

1
cp /data/mongodb2.6.4/mongodb.conf /data/mongodb3.0.2/
mongodb.conf内容示例：

1
2
3
4
5
6
7
bind_ip=127.0.0.1
port=27017
dbpath=/data/mongodb3.0.2/data/
logpath=/data/mongodb3.0.2/logs/mongodb.log
logappend=true
auth=true
fork=true
通过Mongodb3启动Mongodb准备备份

1
/data/mongodb3.0.2/bin/mongod --dbpath /data/mongodb2.6.4/data/
备份

1
/data/mongodb3.0.2/bin/mongodump --out /data/mongodb3.0.2/bak/
然后关闭数据库，重新启动,使用WiredTiger引擎

1
/data/mongodb3.0.2/bin/mongod --storageEngine wiredTiger --dbpath /data/mongodb3.0.2/data/
恢复数据

1
/data/mongodb3.0.2/bin/mongorestore /data/mongodb3.0.2/bak/
恢复完成以后，再停止Mongodb。

修改mongodb.conf

1
2
3
4
5
6
7
8
bind_ip=127.0.0.1
port=27017
dbpath=/data/mongodb3.0.2/data/
logpath=/data/mongodb3.0.2/logs/mongodb.log
logappend=true
auth=true
fork=true
storageEngine=wiredTiger
然后启动Mongodb

1
2
3
4
5
/data/mongodb3.0.2/bin/mongod --config /data/mongodb3.0.2/mongodb.conf
------分割线------结果------
about to fork child process, waiting until server is ready for connections.
forked process: 11197
child process started successfully, parent exiting
记得删除先前版本/usr/bin/mongo,把新版本的复制过去

测试了AUTH，一切正常，创建的账户也没丢失。

另外数据相比2版本的，确实占用了很少的空间。以后再也不会随随便便删除集合（释放空间很麻烦），删除数据库了。

1
2
3
4
5
6
7
[root@localhost mongodb3.0.2]# mongo
MongoDB shell version: 3.0.2
connecting to: test
> use datatest
switched to db datatest
> db.auth('admin','admin')
1
一切正常，删除以前的目录，跟备份数据的目录。

Update:

更新到Mongodb3.0.2版本以后，一切正常，在使用 mongostat的时候，不能像以前一样直接使用

1
mongostat -u admin -p admin
命令直接查看状态

显示如下：

1
2
# mongostat -u admin -p admin
2015-04-16T10:48:13.192+0800    --authenticationDatabase is required when authenticating against a non $external database
现在需要多加个参数“--authenticationDatabase”

命令如下：

1
# mongostat -u root -p root123 --authenticationDatabase=admin
测试的时候，还只能选择"admin"这个数据库，选择其他的数据库，用其他库的认证账户都不行

错误如下：

1
2015-04-16T10:49:57.912+0800    Failed: not authorized on admin to execute command { serverStatus: 1, recordStats: 0 }
或者

1
2015-04-16T10:51:17.267+0800    Failed: error connecting to db server: server returned error on SASL authentication step: Authentication failed.
mongotop命令也一样

另外竟然mongostat不显示操作的库名了。





查看数据库的连接数

查看mongodb链接数
netstat -an |grep ESTA |awk '{print$5 "\n"}' |awk 'BEGIN {FS=":"} {COUNT[$1]++}END{for(a in COUNT) print a, COUNT[a]}' |sort -k 2 -nr

转自:http://www.cnblogs.com/TeaIng-Index/p/4429256.html