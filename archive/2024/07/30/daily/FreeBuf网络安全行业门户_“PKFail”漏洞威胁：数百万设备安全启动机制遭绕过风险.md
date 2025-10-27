---
title: “PKFail”漏洞威胁：数百万设备安全启动机制遭绕过风险
url: https://www.freebuf.com/articles/paper/407214.html
source: FreeBuf网络安全行业门户
date: 2024-07-30
fetch_date: 2025-10-06T17:44:25.086849
---

# “PKFail”漏洞威胁：数百万设备安全启动机制遭绕过风险

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

“PKFail”漏洞威胁：数百万设备安全启动机制遭绕过风险

* ![]()
* 关注

* [咨询](https://www.freebuf.com/consult)

“PKFail”漏洞威胁：数百万设备安全启动机制遭绕过风险

2024-07-29 12:00:54

所属地 上海

darkreading网站消息，攻击者可以绕过数百万基于英特尔和ARM微处理器的计算系统（来自多家厂商）的安全启动过程，因为它们共享了一个在设备启动过程中使用的、之前已经泄露的加密密钥。

![](https://image.3001.net/images/20240729/1722225840_66a714b01ed9bcd52ed35.png!small)美国AMI公司提供的所谓平台密钥PK (Platform Key)在安全启动的个人电脑启动链中扮演信任根的角色，用于验证设备固件和启动软件的真实性和完整性。

不幸的是，固件安全供应商Binarly的研究人员发现，该密钥已在2018年的一次数据泄露事件中被曝光。上周，Binarly在关于该问题的一篇帖子中表示:“该密钥可能包含在AMI的参考实现中，预期供应链中的下游实体会用另一个安全生成的密钥替换它。”

## PKFail安全启动问题

原来的设备制造商(OEM)为不同的基于Intel和ARM的设备制造商生产的固件使用AMI测试密钥。Binarly的首席执行官兼创始人Alex Matrosov表示，其结果是，目前全球可能有数以百万计的消费者和企业设备在安全启动过程中使用相同的AMI PK。受影响的供应商包括联想、惠普、华硕和超微。

Matrosov说:“一个能够访问PK私有部分的攻击者可以很容易地通过操纵密钥交换密钥数据库、签名数据库和禁止签名数据库来绕过安全启动。”他将这个问题称为“PKFail”。这个问题使得攻击者更容易部署统一可扩展固件接口(UEFI)引导包，比如去年的BlackLotus，它提供持久的内核访问和权限。

Matrosov表示，解决方法很简单，只需更换受损的密钥，设备供应商提供固件更新，目前已经有几个国家已经这么做了。然而，在某些情况下，比如数据中心服务器或者关键应用程序中使用的系统，固件更新可能需要一些时间来部署。

针对Binarly为PKFail开发的概念验证漏洞(PoC)，Matrosov指出，在设备受到影响的情况下，利用这个问题将变得非常简单。Matrosov建议企业在能够部署固件升级之前，将带有泄漏AMI PK的设备与关键网络断开连接。

## 一把万能钥匙和一件大事

总部位于荷兰的Hadrian公司的首席执行官Rogier Fischer在一封电子邮件中评论说，PKfail问题是一个大问题，因为它使黑客能够轻松绕过安全启动，这就像拥有一把打开许多房子的万能钥匙。由于相同的密钥在不同的设备上使用，一次违规可能会影响许多系统，使问题变得普遍。

Matrosov说，PKFail是一个存在了十多年的问题的最新表现，即OEM和设备制造商倾向于在生产固件和设备中使用非生产和测试加密密钥。以AMI PK为例，它显然是被视为完全不可信的，但它最终出现在了多个供应商的设备中。

Binarly的报告指出，2016年的一个漏洞被追踪为CVE-2016-5247，安全研究人员发现多个联想设备共享相同的AMI测试PK。当时，国家漏洞数据库将该问题描述为允许“本地用户或物理上接近的攻击者利用AMI测试密钥绕过安全启动保护机制。”

而PKFail是设备供应链中不良的加密密钥管理实践的表现。Matrosov说，想象一下现在有一栋公寓大楼，所有的门锁用的都是相同的钥匙，如果丢失了一把钥匙，可能会给所有人带来麻烦。

**参考来源：**

https://www.darkreading.com/endpoint-security/millions-of-devices-vulnerable-to-pkfail-secure-boot-bypass-issue

# 加密密钥 # 安全密钥 # 密钥管理

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

PKFail安全启动问题

一把万能钥匙和一件大事

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