---
title: 速看！Redis服务器被植入后门
url: https://www.freebuf.com/news/351413.html
source: FreeBuf网络安全行业门户
date: 2022-12-03
fetch_date: 2025-10-04T00:24:22.446095
---

# 速看！Redis服务器被植入后门

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

速看！Redis服务器被植入后门

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

速看！Redis服务器被植入后门

2022-12-02 14:26:48

所属地 上海

![](https://image.3001.net/images/20221202/1669962182_638999c61597793c21612.png!small)

被研究人员称之为Redigo的一种基于Go的新的恶意软件，它一直针对有CVE-2022-0543漏洞的Redis服务器并植入一个隐秘的后门允许命令执行。

CVE-2022-0543是Redis（远程字典服务器）软件中的一个关键漏洞，具有非常高的威胁性。它在2022年2月被发现并修复。修复几个月后，仍有攻击者继续在未打补丁的机器上利用它。针对于此漏洞的恶意软件的名称Redigo则是由它的目标机器和构建它的编程语言创造的。

今天，AquaSec报告说，其易受CVE-2022-0543影响的Redis蜜罐捕获了一个新的恶意软件，该恶意软件并没有被Virus Total上的安全软件检测到。

![](https://image.3001.net/images/20221202/1669962222_638999ee825936f3333e9.png!small)

## Redigo攻击

AquaSec说，Redigo攻击从6379端口的扫描开始，以定位暴露在开放网络上的Redis服务器。找到目标端点后，atacker连接并运行以下命令:

INFO - 检查Redis的版本，以确定服务器是否有CVE-2022-0543的漏洞。
SLAVEOF - 创建一个攻击服务器的副本。
REPLCONF - 配置从攻击服务器到新创建副本的连接。
PSYNC - 启动复制流并下载服务器磁盘上的共享库 "exp\_lin.so"。
MODULE LOAD - 从下载的动态库中加载模块，该模块能够执行任意命令并利用CVE-2022-0543。
SLAVEOF NO ONE - 将有漏洞的Redis服务器转变成主服务器。

![](https://image.3001.net/images/20221202/1669962292_63899a34d91feb6131aef.png!small)

利用植入后门的命令执行能力，攻击者收集主机的硬件信息，然后下载Redigo（redis-1.2-SNAPSHOT）。该恶意软件在升级权限后被执行。

攻击者通过6379端口模拟正常的Redis通信，以逃避网络分析工具的检测，同时试图隐藏来自Redigo的命令和控制服务器的流量。

由于AquaSec公司蜜罐的攻击时间限制，其分析师无法确定Redigo在环境中站稳脚跟后到底做了什么。

![](https://image.3001.net/images/20221202/1669962349_63899a6d3940811bc05eb.png!small)

AquaSec表示，Redigo的最终目标很可能是将易受攻击的服务器作为机器人加入网络，进行分布式拒绝服务（DDoS）攻击，或者在被攻击的系统上运行加密货币矿工。

此外，由于Redis是一个数据库，访问数据并窃取它也可能是Redigo攻击的目的。

> 参考来源：https://www.bleepingcomputer.com/news/security/new-redigo-malware-drops-stealthy-backdoor-on-redis-servers/

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

Redigo攻击

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