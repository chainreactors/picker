---
title: 新型攻击“nRootTag”将15亿部iPhone变为免费追踪器
url: https://www.freebuf.com/vuls/423102.html
source: FreeBuf网络安全行业门户
date: 2025-02-28
fetch_date: 2025-10-06T20:37:42.420716
---

# 新型攻击“nRootTag”将15亿部iPhone变为免费追踪器

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

新型攻击“nRootTag”将15亿部iPhone变为免费追踪器

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

新型攻击“nRootTag”将15亿部iPhone变为免费追踪器

2025-02-27 12:03:04

所属地 上海

![image](https://image.3001.net/images/20250227/1740664972165011_6d15e1267f1643c88d7b05c368707ef4.webp!small)

一种名为“nRootTag”的新型攻击，将超过15亿台苹果设备（包括iPhone、iPad、Apple Watch和Mac）暴露在恶意攻击者的隐蔽追踪之下。这项攻击由研究人员Junming Chen、Xiaoyue Ma、Lannan Luo和Qiang Zeng在即将发布的2025年USENIX安全研讨会论文中详细阐述，它通过利用苹果的“查找我的”网络，将非苹果设备变为无需root访问权限的隐秘追踪信标。该攻击利用了蓝牙低功耗（BLE）协议，对全球隐私构成了前所未有的威胁。

## **nRootTag如何劫持苹果的“查找我的”网络**

苹果的“查找我的”网络原本设计用于通过附近苹果设备发出的众包蓝牙信号来定位丢失的设备，其依靠AirTags广播的加密“丢失消息”。这些消息由附近的设备中继到苹果云端，方便设备所有者获取位置数据。而nRootTag攻击通过伪造合法的AirTag广播，绕过了该系统的安全防护。

攻击的第一步是在目标设备（如Windows PC、Android手机或基于Linux的物联网设备）上安装木马化代码。该代码会收集设备的BLE广播地址，并从攻击者控制的服务器请求匹配的公钥/私钥对。一旦配置完成，设备便会广播与真实AirTag信号不同的伪造“丢失消息”。

![](https://image.3001.net/images/20250227/1740664974081144_d7f82f4ef61d4b8d83368b3cec186444!small)攻击概述

附近的苹果设备在无意中充当了“发现者”角色，将这些消息中继到苹果的服务器，使攻击者能够追踪设备的实时位置。研究人员开发了两种生成有效加密密钥的方法：预计算彩虹表和实时GPU辅助密钥搜索。

![](https://image.3001.net/images/20250227/1740664975058515_c53500cd9935481d9d97dacbba5be67a!small)nRootTag的架构

预计算的彩虹表可以实现即时密钥检索，而NVIDIA RTX 3080等GPU集群或数据中心级A100可以以每秒210万密钥的速度进行暴力破解。这种高效性将攻击成本降低至“每目标不到5美元”，同时在几分钟内实现了90%的成功率。

值得注意的是，该漏洞的跨平台兼容性使其扩展到智能手表、笔记本电脑和医疗物联网设备，进一步扩大了其威胁范围。

## **补丁与持续风险**

苹果已在iOS 18.2、macOS Sequoia 15.2等更新中发布了补丁以缓解nRootTag攻击。然而，这些补丁只能防止已更新的苹果设备中继恶意信号。全球仍有超过15亿台活跃设备，其中许多运行过时的软件，因此攻击仍然有效。论文指出：“只要附近存在未更新的iPhone，追踪链就会持续。”

这项由美国国家科学基金会（NSF）和联邦网络倡议资助的研究敦促企业分离蓝牙流量并实施严格的设备认证。对于消费者而言，立即更新软件至关重要。然而，研究人员警告称，nRootTag的低成本和可扩展性使其“必然会被网络犯罪分子采用”。

nRootTag揭示了众包追踪网络的系统性缺陷。通过利用对苹果生态系统的信任，该攻击侵蚀了匿名性保障，并展示了良性的基础设施如何被武器化。随着蓝牙设备的普及，这项研究呼吁重新评估离线查找系统的加密设计，以防止恶意追踪成为普遍问题。

苹果尚未对此发表评论，仅确认了研究人员的披露。随着漏洞的蓝图公开，保护数十亿设备安全的斗争才刚刚开始。

**参考来源：**

> [New “nRootTag” Attack Turns 1.5 Billion iPhones as Free Tracking Agents for Attacker](https://cybersecuritynews.com/new-attack-nroottag-iphones/)

# 无线安全 # 移动安全

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