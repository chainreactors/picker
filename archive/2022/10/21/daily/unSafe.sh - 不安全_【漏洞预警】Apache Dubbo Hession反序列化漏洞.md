---
title: 【漏洞预警】Apache Dubbo Hession反序列化漏洞
url: https://buaq.net/go-131854.html
source: unSafe.sh - 不安全
date: 2022-10-21
fetch_date: 2025-10-03T20:27:06.928056
---

# 【漏洞预警】Apache Dubbo Hession反序列化漏洞

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

【漏洞预警】Apache Dubbo Hession反序列化漏洞

1. 通告信息近日，安识科技A-Team团队监测到一则 Apache Dubbo组件存在Hession反序列化漏洞的信息，漏洞编号：CVE-2022-39198，漏洞威胁等级：高
*2022-10-20 17:49:13
Author: [www.secpulse.com(查看原文)](/jump-131854.htm)
阅读量:60
收藏*

---

##

1. **通告信息**

近日，安识科技A-Team团队监测到一则 Apache Dubbo组件存在Hession反序列化漏洞的信息，漏洞编号：CVE-2022-39198，漏洞威胁等级：高危。

该漏洞是由于Dubbo hessian-lite 3.2.12及之前版本中存在反序列化漏洞，成功利用此漏洞可在目标系统上执行恶意代码，最终获取服务器最高权限。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

##

2. **漏洞概述**

CVE：CVE-2022-39198

简述：Apache Dubbo是一款高性能、轻量级的开源服务框架，提供了RPC通信与微服务处理两大关键能力。由于Dubbo hessian-lite 3.2.12及之前版本中存在反序列化漏洞，成功利用此漏洞可在目标系统上执行恶意代码。

##

3. **漏洞危害**

攻击者可利用该漏洞在未授权的情况下，构造恶意数据执行远程代码执行攻击，最终获取服务器最高权限。

##

4. **影响版本**

目前受影响的Apache Dubbo 版本：

Apache Dubbo 2.7.x版本：<= 2.7.17

Apache Dubbo 3.0.x版本：<= 3.0.11

Apache Dubbo 3.1.x版本：<= 3.1.0

##

5. **解决方案**

目前该漏洞已经修复，受影响用户可以升级到Dubbo hessian-lite 版本 >=3.2.13；或升级Apache Dubbo到以下版本：

Apache Dubbo 2.7.x版本：>= 2.7.18

Apache Dubbo 3.0.x版本：>= 3.0.12

Apache Dubbo 3.1.x版本：>= 3.1.1

Apache Dubbo下载链接：

https://github.com/apache/dubbo/tags

Dubbo hessian-lite下载链接：

https://github.com/apache/dubbo-hessian-lite/releases

##

6. **时间轴**

【-】2022年10月18日 安识科技A-Team团队监测到Apache Dubbo Hession反序列化漏洞信息

【-】2022年10月19日 安识科技A-Team团队根据漏洞信息分析

【-】2022年10月20日 安识科技A-Team团队发布安全通告

**本文作者：[安识科技](https://www.secpulse.com/archives/newpage/author?author_id=3871)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/189435.html**](https://www.secpulse.com/archives/189435.html)

文章来源: https://www.secpulse.com/archives/189435.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)