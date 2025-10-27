---
title: 对BP机发起网络攻击，竟可以制造全国性大爆炸？
url: https://www.freebuf.com/news/411206.html
source: FreeBuf网络安全行业门户
date: 2024-09-19
fetch_date: 2025-10-06T18:25:32.104046
---

# 对BP机发起网络攻击，竟可以制造全国性大爆炸？

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

对BP机发起网络攻击，为什么可以制造全国性大爆炸？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

对BP机发起网络攻击，为什么可以制造全国性大爆炸？

2024-09-18 17:16:08

所属地 上海

> 电影中的剧情照进现实。恶意威胁组织通过对BP机（寻呼机）发起网络攻击，导致黎巴嫩全国范围内的BP机（寻呼机）几乎被同时引爆，造成9人丧生、近2800人受伤。

据《华尔街日报》等多家媒体报道，9月17日，黎巴嫩看守政府召开部长会议期间，黎巴嫩境内发生了一场巨大的爆炸事件，真主党（Hezbollah）成员携带的寻呼机在全国范围内几乎同时爆炸，导致9人丧生、近2800人受伤，其中约200人伤情危重。黎真主党发表声明认为以色列对寻呼机爆炸负有“全部责任”。![](https://image.3001.net/images/20240918/1726650937_66ea9a3990965a96a84b6.png!small)

据悉，黎真主党武装人员近来较为普遍地使用寻呼机，通过这种技术含量较低的通信设备避免以色列追踪他们的位置，以及应对通信安全挑战。但此次发生爆炸的BP机基本都集中在真主党成员，意味着其通信系统很有可能被渗透，凸显出设备安全方面的巨大漏洞。![](https://image.3001.net/images/20240918/1726650619_66ea98fb842a2dcdf5a33.jpg!small)

## **网络攻击引发BP机爆炸？**

BP机爆炸事件迅速在全球范围内引发广泛关注。据媒体报道，爆炸的BP机型号为AR-924，由台湾省的Gold Apollo公司生产。据专业人士分析，这些BP机中早已被植入微量炸药，攻击者通过远程引爆的方式进行遥控，让这些BP机在接收到特定信号后发生爆炸。

但在这个过程中，有两个问题需要解决。

一是定位问题。从现有情况来看，此次爆炸几乎只涉及真主党成员所使用的BP机，说明攻击者早已将BP机和使用者对应起来。由于BP机不能主动发送信号，因此无法通过通信信号来定位。但攻击者可以通过寻呼中心定向给BP机发送信号，从而实现定向爆炸。

二是具体引爆方式，相关专业人士分析，攻击者可能是通过黑客手段对数千台寻呼机进行大规模的网络攻击，致使其锂电池短路或过载，从而引发爆炸。

三是供应链安全问题，从现有情况来看，仅仅依靠BP机电池产生爆炸不仅难度高，而且爆炸威力也不足，不太可能造成大量人员伤亡。因此有专家分析称，攻击者提前在真主党采购的BP机电池中内置微量高爆炸药（四硝酸季戊四醇）。

如前文所说，爆炸的BP机都是定向采购，那么很有可能是攻击者提前渗透了真主党的供应链，才能实现上述目标。

这意味着此次事件不是一次意外，而是一次极其缜密的网络战。这次事件证明了网络攻击不仅限于信息窃取和系统瘫痪，还可以通过控制物理设备，直接引发真实的物理伤害和人员伤亡。

有安全专家指出，这次攻击的精确度和复杂性表明，这不仅仅是普通的恶意软件攻击，而可能涉及到更为复杂的供应链攻击：“无论是通过恶意软件触发电池过热爆炸，还是在设备中放置了实际的爆炸装置，这次攻击都展示了对这些设备生产链的深层控制。无论具体手段如何，攻击的复杂性和精准度都表明了这是一次精心策划的行动。”

## **爆炸事件启示录**

1. 网络安全意识提升：事件引发了全球对网络安全的广泛关注，提醒人们即使是看似传统的通讯设备也可能成为网络攻击的目标。各组织和个人开始高度重视网络安全防护，加强通讯设备的防护能力，防止恶意软件或黑客的入侵。

2. 供应链安全重视：事件突显了供应链安全的重要性，提醒国家和企业在依赖全球供应链的同时，必须加强供应链管理，确保生产过程中的每个环节都在可控范围内，尤其是对于关乎国家安全的设备和技术，应加速自主研发和生产。

3. 科技发展的长远影响：这次事件开创了网络攻击的新模式，展示了信息战和网络战的威力，促使科技行业加大在安全技术研发、安全管理等方面的投入和改进，以提升产品的安全性和竞争力。

本次BP机大规模爆炸事件，开创了网络攻击的一个新模式，也再次展示了信息战和网络战的威力。虽然国内早已淘汰了BP机，但此次爆炸事件依旧值得警醒，在网络世界中依旧存在大量威胁，并且很有可能在现实世界引发巨大的危害，网络安全任重道远。

# 数据安全

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

网络攻击引发BP机爆炸？

爆炸事件启示录

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