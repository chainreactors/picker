---
title: minio分布式存储 安装minio（设置开机自启动）
url: https://blog.upx8.com/3163
source: 黑海洋 - WIKI
date: 2023-01-05
fetch_date: 2025-10-04T03:04:33.670274
---

# minio分布式存储 安装minio（设置开机自启动）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# minio分布式存储 安装minio（设置开机自启动）

发布时间:
2023-01-04

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
20684

1，准备安装目录和文件

系统:CentOs

#进入安装目录

cd /home/minio

minio下载地址

也可以在线下载二进制文件

wget https://dl.min.io/server/minio/release/linux-amd64/minio

2，安装

2.1赋权

chmod +x minio

2.2设置用户名、密码

#修改Minio的初始账号密码（也可以不修改）

#初始账号：minioadmin

#初始密码：minioadmin

#设置控制台账号（最少3位）

export MINIO\_ACCESS\_KEY=admin

#设置密码（最少8位）

export MINIO\_SECRET\_KEY=12345678

2.3创建存储目录及日志文件

#创建存储目录

mkdir -p /home/minio/data

#进入 cd /home/minio

#创建日志文件 touch minio.log

3后台启动

3.1进入执行文件目录

cd /opt/minio

#后台启动

nohup /home/minio/minio server --address :9800 --console-address :9889 /home/minio/data >/home/minio/minio.log 2>&1 &

备注:

nohup：后台启动

./minio server：启动命令

--address :9800：指定API端口

--console-address :9000：指定控制台端口

/home/minio/data：指定存储目录

>/home/minio/minio.log 2>&1 ：控制台日志重定向到/home/minio/minio.log文件中

&：后台运行

注：

--console-address :9000

#启动Minio (需要进入minio存放目录下)#50000 固定端口号 否则每次启动Minio会随机生成一个不一样的端口（控制台会有打印信息）

4.将Minio设置成系统服务：

#以上步骤，如果Ctrl+C退出后，这个Minio服务同时也停止了

#如果需要它在后台运行就需要把它添加到后台服务里边

#切换文件目录

cd /usr/local/minio

#创建目录

mkdir conf

#创建配置文件

mkdir minio.conf

---------------------------------------------------------------------

#minio.conf文件内容

#数据存放目录

MINIO\_VOLUMES="/usr/local/data"

#端口号设置

MINIO\_OPTS="--console-address :9000"

#用户名

MINIO\_ROOT\_USER="minio"

#密码

MINIO\_ROOT\_PASSWORD="12345678"

--------------------------------------------------------------------------

#在/etc/systemd/system目录下新建一个minio.service

#切换文件目录

cd /etc/systemd/system

#创建配置文件

mkdir minio.service

----------------------------------------------------------------------------

#minio.service文件内容

[Unit]

Description=MinIO

Documentation=https://docs.min.io

Wants=network-online.target

After=network-online.target

#minio文件具体位置

AssertFileIsExecutable=/usr/local/minio/minio

[Service]

# User and group 用户 组

User=root

Group=root

#创建的配置文件 minio.conf

EnvironmentFile=/usr/local/minio/conf/minio.conf

ExecStart=/usr/local/minio/minio server $MINIO\_OPTS $MINIO\_VOLUMES

# Let systemd restart this service always

Restart=always

# Specifies the maximum file descriptor number that can be opened by this process

LimitNOFILE=65536

# Disable timeout logic and wait until process is stopped

TimeoutStopSec=infinity

SendSIGKILL=no

[Install]

WantedBy=multi-user.target

5正式启用和状态查看

#将服务设置为每次开机启动

systemctl enable minio.service

#重新加载某个服务的配置文件，如果新安装了一个服务，归属于 systemctl 管理，要是新服务的服务程序配置文件生效，需重新加载

systemctl daemon-reload

#启动服务

systemctl start minio

#停止服务

systemctl stop minio

#重启服务

systemctl restrat minio

#查看服务状态

systemctl status minio.service

#打开页面访问登录成功即可

http://192.168.80.137:9000

[取消回复](https://blog.upx8.com/3163#respond-post-3163)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")