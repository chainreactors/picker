---
title: 内网渗透之内网信息收集总结
url: https://www.freebuf.com/articles/system/421736.html
source: FreeBuf网络安全行业门户
date: 2025-02-14
fetch_date: 2025-10-06T20:35:57.520842
---

# 内网渗透之内网信息收集总结

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

内网渗透 | 内网信息收集总结

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

内网渗透 | 内网信息收集总结

2025-02-13 16:46:20

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## ****目录****

* 主机发现
* 主机信息收集
* 敏感信息、配置文件收集
* 域信息收集
* Linux信息收集

## ****一、主机发现****

已经获取的一台内网的主机权限，如何在内网中寻找我们需要的目标资产，就需要我们根据收集当前主机同网段的其他机器，查看网络链接，看能否发现新网段，为后续内网横移做准备。

### ****1、网络连接****

命令（netstat -ano）

![1739435586_67adae427eabe04937635.png!small?1739435587421](https://image.3001.net/images/20250213/1739435586_67adae427eabe04937635.png!small?1739435587421)

查看有连接的其他IP服务，可以收集到内网其他机器的IP地址。

### ****2、icmp探测****

ping c 端
for /l %i in (1,1,255) do @ping 192.168.31.%i -w 1 -n 1 | find /i "ttl"

ping b 端
for /l %i in (1,1,244) do @ping -a 10.0.%i.1 -w 1 -n 1 | find /i "Ping"

实例

for /l %i in (1,1,255) do @ping 192.168.21.%i -w 1 -n 1 | find /i "ttl"

![1739435673_67adae9907e63a6a74ebc.png!small?1739435674596](https://image.3001.net/images/20250213/1739435673_67adae9907e63a6a74ebc.png!small?1739435674596)

### ****3、路由表信息****

查看路由表信息

![1739435660_67adae8c64b95403398b9.png!small?1739435669792](https://image.3001.net/images/20250213/1739435660_67adae8c64b95403398b9.png!small?1739435669792)

route print

![1739435666_67adae92db75740a186c3.png!small?1739435669792](https://image.3001.net/images/20250213/1739435666_67adae92db75740a186c3.png!small?1739435669792)

### ****4、ARP发现主机****

arp-scan

sudo arp-scan 192.168.183.1/24

![1739435673_67adae998f7c6142ba38d.png!small?1739435674596](https://image.3001.net/images/20250213/1739435673_67adae998f7c6142ba38d.png!small?1739435674596)

### ****5、NetBIOS发现主机****

NetBIOS是windows网络邻居协议，在局域网上程序可使用的应用程序编程接口。也是计算机的标识名，用于局域网中计算机之间的互相访问。

使用nbtscan工具发现网络中其他机器

![1739435682_67adaea2c3be914008030.png!small?1739435684733](https://image.3001.net/images/20250213/1739435682_67adaea2c3be914008030.png!small?1739435684733)

nbtscan在内网中的扫描动静很大，可以使用windows自带的命令nbtstat 对指定IP进行识别

![1739435689_67adaea9bf52a72d6d957.png!small?1739435691493](https://image.3001.net/images/20250213/1739435689_67adaea9bf52a72d6d957.png!small?1739435691493)

nbtstat -A 192.168.21.129

![1739435698_67adaeb265faccdc32d32.png!small?1739435706853](https://image.3001.net/images/20250213/1739435698_67adaeb265faccdc32d32.png!small?1739435706853)

### ****6、net命令****

net view 不带参数，显示域列表、计算机列表或指定计算机的共享资源列表

net Session 不带参数，显示所有与本地计算机的回话信息

### ****7、HOSTS文件****

在内网中有些系统可能没有做地址解析，管理员会把记录写在hosts文件中，所以可以翻找一下这个文件，也许可以找到关键系统。

C:\Windows\System32\drivers\etc\hosts

### ****8、DNS Cache****

查看dns解析记录

ipconfig /displaydns

![1739435713_67adaec12179f350fb977.png!small?1739435714759](https://image.3001.net/images/20250213/1739435713_67adaec12179f350fb977.png!small?1739435714759)

## ****二、主机信息收集****

主机信息收集

收集本地敏感信息

域信息收集

### ****1、whoami /all****

查看账号、权限信息

![1739435740_67adaedc1a88c45996370.png!small?1739435742488](https://image.3001.net/images/20250213/1739435740_67adaedc1a88c45996370.png!small?1739435742488)

Mandatory Label\High Mandatory Level 表明是 UAC用户

### ****2、systeminfo****

![1739435751_67adaee7f146b61e7bde1.png!small?1739435761537](https://image.3001.net/images/20250213/1739435751_67adaee7f146b61e7bde1.png!small?1739435761537)

### ****3、操作系统识别****

2003/xp

2008/window7

2012及以后

详细版本

### ****4、tasklist /svc****

进程查看，看是否有杀软、hids

![1739435764_67adaef43d682bf960e8f.png!small?1739435766434](https://image.3001.net/images/20250213/1739435764_67adaef43d682bf960e8f.png!small?1739435766434)

### ****5、服务****

sc query

![1739435814_67adaf26a53d83c851d77.png!small?1739435816834](https://image.3001.net/images/20250213/1739435814_67adaf26a53d83c851d77.png!small?1739435816834)

### ****6、网络配置****

ipconfig /all

![1739435782_67adaf0674724491f84ce.png!small?1739435799087](https://image.3001.net/images/20250213/1739435782_67adaf0674724491f84ce.png!small?1739435799087)

### ****7、网络连接****

查看本地开放端口、连接、代理等

netstat -ano 、route print

### ****8、用户、组****

****（1）CMD命令****

net user / net users 显示计算机上的用户帐户列表

![1739435814_67adaf269c73cc9fd69c2.png!small?1739435816834](https://image.3001.net/images/20250213/1739435814_67adaf269c73cc9fd69c2.png!small?1739435816834)

net user %username% 查看当前用户

![1739435824_67adaf30850fcbaa27a77.png!small?1739435826356](https://image.3001.net/images/20250213/1739435824_67adaf30850fcbaa27a77.png!small?1739435826356)

net user liukaifeng01 查看指定用户

![1739435836_67adaf3c00450f861e953.png!small?1739435837044](https://image.3001.net/images/20250213/1739435836_67adaf3c00450f861e953.png!small?1739435837044)

net localgroup 查看用户组信息

![1739435845_67adaf4523e6e32de6659.png!small?1739435845820](https://image.3001.net/images/20250213/1739435845_67adaf4523e6e32de6659.png!small?1739435845820)

net localgroup Administrators 查看哪些用户在Administrators组里

![](https://image.3001.net/images/20250213/1739435850_67adaf4ae7677)

# 系统安全 # 内网渗透

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

目录

一、主机发现

* 1、网络连接
* 2、icmp探测
* 3、路由表信息
* 4、ARP发现主机
* 5、NetBIOS发现主机
* 6、net命令
* 7、HOSTS文件
* 8、DNS Cache

二、主机信息收集

* 1、whoami /all
* 2、systeminfo
* 3、操作系统识别
* 4、tasklist /svc
* 5、服务
* 6、网络配置
* 7、网络连接
* 8、用户、组
* 9、arp
* 10、RDP信息
* 11、补丁信息
* 12、IPC连接
* 13、默认共享
* 14、防火墙
* 15、启动项
* 16、日志
* 17、软件、进程
* 18、dsquery
* 19、杀软

三、敏感信息、配置文件收集

* 1、Windows无人值守应答文件
* 2、自动登录
* 3、Web配置文件
* 4、Windows敏感信息收集命令
* 5、浏览器信息收集
* 6、剪切板信息收集
* 7、IIS信息收集

四、域信息收集

五、Linux信息收集

* 1、服务信息
* 2、用户信息
* 3、用户权限
* 4、环境变量信息
* 5、网络信息
* 6、计划任务信息
* 7、重要文件信息
* 8、特征文件

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)