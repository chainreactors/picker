---
title: 安全顶会NDSS2023|针对安卓用户身份隐私泄露的分析研究
url: https://www.freebuf.com/articles/endpoint/359439.html
source: FreeBuf网络安全行业门户
date: 2023-03-07
fetch_date: 2025-10-04T08:49:08.557659
---

# 安全顶会NDSS2023|针对安卓用户身份隐私泄露的分析研究

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

安全顶会NDSS2023|针对安卓用户身份隐私泄露的分析研究

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

安全顶会NDSS2023|针对安卓用户身份隐私泄露的分析研究

2023-03-06 15:16:51

所属地 北京

## 一、背景

2月27日-3月3日，国际安全顶会NDSS 2023在美国加州举办，来自字节跳动无恒实验室的研究论文《Post-GDPR Threat Hunting on Android Phones: Dissecting OS-level Safeguards of User-unresettable Identifiers》被NDSS 2023收录。

NDSS网络与分布式系统安全会议（the Network and Distributed System Symposium, NDSS )，是国际公认的网络和系统安全四大顶级学术会议（BIG4）之一，录用率常年保持在15%左右，具有非常高的学术影响力。

3月1日，来自无恒实验室的安全研究员张清在NDSS 2023会议现场发表演讲，分享关于安卓操作系统在用户身份标识追踪等方面的隐私问题，主要包括WiFi相关，蓝牙相关，以及常见的uuid（IMEI/MEID/Serial number）等信息在获取方面缺陷的相关研究成果，该研究可促进Android操作系统对于这些信息获取的防护体系建设，助力用户隐私安全保护。

![1678086710_64059236e6288408e3c79.png!small?1678086711552](https://image.3001.net/images/20230306/1678086710_64059236e6288408e3c79.png!small?1678086711552)

## 二、研究介绍

近年来，各国政府越来越重视用户数据与隐私的问题，相继制定了以隐私为重点的数据保护法规。高度的开放性是安卓的典型特性，然而，开放性也是一把双刃剑，高度的开放性，也随之带来了人们对于Android生态下用户隐私保护的担忧。同时随着安卓手机应用的爆发式增长，用户身份识别信息也随时面临着被泄漏的风险。尤其是一些用户不可修改的设备识别信息，一旦遭到泄露，将带给用户身份追踪方面的困扰，并造成长期的隐私泄露。

据悉，谷歌已经采取措施，实施新的隐私功能，以限制应用程序对用户数据的使用，尤其是在一些用户不可重置的识别信息 （User-unresettable Identifiers, 后文简称UUI）上，在系统层面针对UUI的读取权限日益收紧，并且从10.0版本开始，第三方Apps被限制，甚至禁止读取一些常用的手机设备识别信息，例如手机序列号，IMEI，ICCID等。

### 2.1 了解UUI

为了识别UUI，无恒实验室参考了Android的官方文档和相关文献，确定了六种类型的UUI。本研究将分析这六种UUI 是否受到良好保护；并在此基础上，以这六种UUI作为目标，探索一个UUI是如何被应用程序访问的，以及还有多少我们从未见过的UUI存在隐私泄露的风险。

基于上述背景，无恒实验室联合昆士兰大学、新加坡国立大学等科研机构研发了一款名叫U2I2的分析工具，U2I2 不仅评估这六个已知 UUI 的保护情况，还要评估其他以前未报告的 UUI 的保护情况。通过检测可编程接口，非系统应用程序可以在没有所需权限的情况下，恶意通过该接口访问 UUI。无恒实验室对市面上多款最新Android设备进行分析后发现，即使用户的手机安装了最新的Android版本（10.0或更高），一些UUI仍然可以被第三方App轻易获取。最终在13款不同型号的Android设备上共发现了65处系统级别（OS-level）的UUI保护漏洞。

![1678086836_640592b4eba5e16a343fa.png!small?1678086837977](https://image.3001.net/images/20230306/1678086836_640592b4eba5e16a343fa.png!small?1678086837977)

（List of 6 recognized Android UUIs）

### 2.2 主要发现

根据研究发现，UUI处理不当的问题在最新的Android手机中仍然普遍存在，截止本论文发表前，总共发现51个独立的漏洞（将多个厂商设备中发现的相同漏洞定义为一个独立漏洞），导致了65次系统级UUI泄露。这51个漏洞中，其中有47个漏洞涉及到我们预先锁定的6个目标UUI，还有18个泄露是通过U2I2分析工具经过差异分析后确定的全新UUI（即Misc UUIs）。在分析获取渠道时，我们发现有45个漏洞是通过undocumented渠道获取的，同时有30个漏洞是通过读取系统属性实现的。从漏洞产生者角度统计，只有一个独立漏洞是源于AOSP代码的，即Google在编写Android系统时造成的，剩余50个漏洞均为厂商定制ROM过程中产生。AOSP的漏洞也毫不意外地出现在所有的厂商ROM当中。

### 2.3 白名单问题

在研究过程中，无恒实验室还发现了一个滥用白名单的问题，白名单机制本来不是为第三方App设计，设备厂商更应该谨慎使用该机制。但在对手机厂商分析过程中，发现存在过度使用白名单机制来规范敏感API调用的问题， 由于身份验证存在缺陷，恶意应用程序可以欺骗白名单机制并绕过权限控制来收集 UUI。 这样会导致处在白名单中的APP可以越过Android系统对其进行的鉴权机制，在用户不知情的情况下获取其隐私。

![1678086852_640592c4368825a6a9e64.png!small?1678086852821](https://image.3001.net/images/20230306/1678086852_640592c4368825a6a9e64.png!small?1678086852821)

## 三、小结

为了解操作系统级别的UUI保护，无恒实验室联合昆士兰大学、新加坡国立大学等科研机构对Android操作系统中的UUI进行了全面研究分析，也将研究成果补充到关于应用程序级数据收集行为的现有研究中，助力Android生态系统中的PII保护研究。

无恒实验室秉持负责任的漏洞披露政策，已将所有发现的漏洞提交至相关厂商，目前已收到8个CVE。同时呼吁监管机构、厂商和开发者等加强合作，共同打造一个安全合规的Android生态，为用户的安全上网保驾护航。

![1678086859_640592cb882d410e19815.png!small?1678086860063](https://image.3001.net/images/20230306/1678086859_640592cb882d410e19815.png!small?1678086860063)

想阅读完整论文的朋友，欢迎点击自取：[https://baigd.github.io/files/NDSS23-U2I2.pdf﻿](https://baigd.github.io/files/NDSS23-U2I2.pdf)

# 数据安全 # 安卓安全 # 隐私保护 # 个人身份信息（PII） # 无恒实验室

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

一、背景

二、研究介绍

* 2.1 了解UUI
* 2.2 主要发现
* 2.3 白名单问题

三、小结

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