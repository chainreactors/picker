---
title: Linux安装rinetd实现TCP/UDP端口转发(rinetd使用教程)
url: https://blog.upx8.com/3144
source: 黑海洋 - WIKI
date: 2022-12-11
fetch_date: 2025-10-04T01:12:32.901255
---

# Linux安装rinetd实现TCP/UDP端口转发(rinetd使用教程)

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux安装rinetd实现TCP/UDP端口转发(rinetd使用教程)

发布时间:
2022-12-10

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
19541

rinetd可较haproxy可实现UDP/TCP转发，haproxy仅能转发TCP。（以下为Centos7环境）

## 一、安装rinetd

Github链接：[https://github.com/samhocevar/rinetd](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NhbWhvY2V2YXIvcmluZXRk)

安装依赖，编译工具

gcc是GCC中的GUN C Compiler（C 编译器）

g++是GCC中的GUN C++ Compiler（C++编译器）

以CentOS为例，安装后是没有C语言和C++编译环境的，需要手动安装

|  |  |
| --- | --- |
|  | #安装依赖 |
|  | yum -y install gcc gcc-c++ make automake |
|  | #下载rinetd,无法链接可看文章：https://maobuni.com/2022/06/01/linux-shell-proxy/ |
|  | #或先下载后上传 |
|  | wget https://github.com/samhocevar/rinetd/releases/download/v0.73/rinetd-0.73.tar.gz |
|  | #解压 |
|  | tar -zxvf rinetd-0.73.tar.gz |
|  | #进入目录 |
|  | cd rinetd-0.73 |
|  | #编译安装 |
|  | ./bootstrap |
|  | ./configure |
|  | make && make install |

## 二、转发配置文件

rinetd配置文件的格式如下:

* `0.0.0.0`：源IP
* `2018`：源端口
* `192.168.1.2`：目标IP
* `2019`：目标端口

**TCP转发文件编写格式**

|  |  |
| --- | --- |
|  | #新建rinetd配置文件 |
|  | vi /etc/rinetd.conf |
|  | #填写如下内容，意为监听本地2022端口并转发至192.168.1.2的2023端口 |
|  | 0.0.0.0 2022 192.168.1.2 2023 |
|  | #以配置文件启动rinetd |
|  | rinetd -c /etc/rinetd.conf |

**UDP转发文件编写格式**

```
127.0.0.1   8000/udp  192.168.1.2     8000/udp
```

意为监听本地8000UDP端口，并转发至192.168.1.2的8000端口

## 三、创建systemd服务

|  |  |
| --- | --- |
|  | #创建rinetd服务 |
|  | vi /etc/systemd/system/rinetd.service |
|  | #写入以下内容 |
|  | [Unit] |
|  | Description=rinetd |
|  | After=network.target |
|  |  |
|  | [Service] |
|  | Type=forking |
|  | ExecStart=/usr/local/sbin/rinetd -c /etc/rinetd.conf |
|  |  |
|  | [Install] |
|  | WantedBy=multi-user.target |

`systemctl daemon-reload`重载daemon使其生效，以下为rinetd服务管理命令

|  |  |
| --- | --- |
|  | #启动rinetd |
|  | systemctl start rinetd |
|  | #设置开机启动 |
|  | systemctl enable rinetd |
|  | #停止rinetd |
|  | systemctl stop rinetd |
|  | #重启 |
|  | systemctl restart rinetd |

rinetd支持转发到域名，rinetd会提前解析域名，并将解析出的IP缓存到内存中，域名解析IP发生了变化必须重启rinetd才会生效更改，域名IP经常发生变化的情况下需要自己写个shell重启rinetd。

需要UDP且需要携带原始IP地址（haproxy的proxy参数），可考虑混用。可用于转发Windows remote desk。

[取消回复](https://blog.upx8.com/3144#respond-post-3144)

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