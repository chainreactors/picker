---
title: Scalpel：解构API复杂参数Fuzz的「手术刀」
url: https://www.anquanke.com/post/id/282840
source: 安全客-有思想的安全新媒体
date: 2022-11-10
fetch_date: 2025-10-03T22:12:06.170403
---

# Scalpel：解构API复杂参数Fuzz的「手术刀」

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Scalpel：解构API复杂参数Fuzz的「手术刀」

阅读量**469796**

发布时间 : 2022-11-09 10:30:54

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## Scalpel 简介

Scalpel是一款自动化Web/API漏洞Fuzz引擎，该工具采用被动扫描的方式，通过流量中解析Web/API参数结构，对参数编码进行自动识别与解码，并基于树结构灵活控制注入位点，让漏洞Fuzz向量能够应对复杂的编码与数据结构，实现深度漏洞挖掘。

1. 详细技术原理可参考KCon 2022议题：[《自动化API漏洞Fuzz实战》](http://mp.weixin.qq.com/s?__biz=Mzg3NDcwMDk3OA==&mid=2247484068&idx=1&sn=89ea1b1be48a0cb7f93a4750765719d1&chksm=cecd8b79f9ba026f7fbf52771e41272d684fc3af5175587f768082f8dbaee12d6d33bb892ceb&scene=21#wechat_redirect)
2. 目前我们的Fuzz引擎端已打包为一个小工具，内置100+漏洞POC，供大家试用：
3. https://github.com/StarCrossPortal/scalpel

## 深度参数注入原理

随着Web应用复杂度的提升与API接口的广泛使用，在HTTP应用漏洞Fuzz过程中，**传统的「Form表单明文传参的模式」已经逐渐变为「复杂、嵌套编码的参数传递」。**在此情况下，直接对参数内容进行注入或替换，无法深入底层的漏洞触发点。

漏洞Fuzz过程中需要对这些「结构体、编码」进行抽离，找到真正的注入点位，方可进行自动化漏洞测试。

![]()

**Scalpel拥有一个强大的数据解析和变异算法，它可以将常见的数据格式（json, xml, form等）解析为树结构，然后根据poc中的规则，对树进行变异，包括对叶子节点和树结构的变异。变异完成之后，将树结构还原为原始的数据格式。**

Scalpel主体结构分为被动代理、Fuzz向量生成与验证、结果输出三个阶段：

![]()

漏洞检测部分，采用解析算法，深度解析流量请求中的参数，通过POC中设定的注入点和变异方式生成测试请求，发送请求之后，再通过POC中的验证规则进行成功性判断，最终输出Fuzz结果。

以下面这个JSON请求包为例，解析算法会将其转换为右边所示的树结构，无论其嵌套的层次有多深，解析算法会将其中的所有键值对都解析为一个树结构。然后可以对树中的叶子节点进行变异，也可以对树的整体结构上进行变异。在树上进行变异之后，将树按照原始的数据格式再还原回去，填充到请求报文中，形成变异的请求报文之后再发送出去。

![]()

在原始参数结构解析之后，我们可以基于树结构来设定我们的测试向量注入方式：

对节点的变异方式有：

1. 按数据类型注入payload

2. 注入通用型payload

3. 畸形数据替换

4. 类型转换

![]()

对树结构的变异方式有：

1. 替换object类型结构

2. 插入节点

3. 删除节点

![]()

## Scapel 功能介绍

Scalpel扫描器支持以下漏洞检测或者挖掘场景：

1、检测目标已知安全的漏洞，包括CVE漏洞，热门框架、组件、中间件安全漏洞。

2、通用安全漏洞，包括但不限于SQL注入、XSS漏洞、文件上传、命令执行、文件读取等。

3、未知0day漏洞或者安全问题

同时支持多个参数位置的变异，包括：path、query、header、body等部分，具体可以参考Scalpel

漏洞POC编写指南（https://github.com/StarCrossPortal/scalpel/wiki/POC%E7%BC%96%E5%86%99%E6%8C%87%E5%8D%97）

![]()

## 案例1：CVE-2022-1388F5 BIG-IPAPIUnauthenticated RCE漏洞的检测

简单了解下漏洞，具体可以参考之前[分析文章](https://mp.weixin.qq.com/s?__biz=Mzg3NDcwMDk3OA==&mid=2247483735&idx=1&sn=0b6ffbf45338fdac74d644bd4895c2c7&scene=21#wechat_redirect)（[【技术干货】F5 BIG-IP API Unauthenticated RCE(CVE-2022-1388)分析](http://mp.weixin.qq.com/s?__biz=Mzg3NDcwMDk3OA==&mid=2247483735&idx=1&sn=0b6ffbf45338fdac74d644bd4895c2c7&chksm=cecd888af9ba019ce1bd8c218d821874e275aa77287966087ad045c99b8ff27419b92836db2b&scene=21#wechat_redirect)），我们要实现RCE，需要构造如下特殊的请求：

1、访问路径为/mgmt/tm/util/bash

2、Host为localhost或者127.0.0.1时，绕过验证赋予用户身份

3、Connection头加上X-F5-Auth-Token

4、body部分添加json形式的执行命令

![]()

为了检测到CVE-2022-1388漏洞是否存在，我们需要在发送构造的特殊请求后，识别响应中是否进行了命令执行。

了解到整个检测的步骤后，开始编写漏洞POC一一对应，在URL部分变异，变异方式为替换，变异值为/mgmt/tm/util/bash

![]()

![]()

在Host部分变异，变异方式为替换，变异值为localhost

![]()

![]()

对body部分的变异，变异方式为替换，变异值为我们需要执行的命令，这里执行id命令。

![]()

![]()

最后对响应的匹配，使用正则识别id命令之后的结果。

![]()

在编辑好漏洞POC之后，运行扫描器进行检查。

![]()

在被动扫描的过程，实际获取到的数据包如下：

![]()

如果存在漏洞，将会以html文件的形式记录存在漏洞的信息，查看此次扫描结果。

成功扫描出CVE-2022-1388F5 BIG-IP API Unauthenticated RCE漏洞，漏洞的请求也变异无误，最后的响应中也是执行了id命令。

![]()

## 案例二：利用Scalpel工具挖掘多个0day漏洞

Scalpel工具使用较为灵活，通过对检测目标变异响应的check，可以发现检测目标中未知的安全问题。

例如为发现某些API接口是否存在账号密码的泄露，可以在check部分利用正则表达式匹配具体的泄露数据。

![]()

为发现目标是否存在文件读取漏洞，可以在多个变异位置插入或者替换payload

![]()

![]()

为发现SQL注入漏洞，可以在query、Heder、body中的参数插入’ and 1=1类似的payload

![]()

![]()

星阑实验室成员利用如上的类似通用检测规则，挖掘多个0day漏洞，已提交给CNVD国家信息安全共享平台并被收录。

![]()

![]()

同时发现某Apache开源项目的CVE漏洞，报告被该团队接受并正在修复，尚未披露。

![]()

## 工具地址

**GitHub地址下载地址：**https://github.com/StarCrossPortal/scalpel

目前已支持100+常见漏洞Fuzz向量与POC，持续维护中。

![]()

Scalpel支持多个平台，请根据您的平台或者需求下载相应的版本。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**星阑科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282840](/post/id/282840)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全工具](/tag/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7)
* [安全漏洞](/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)
* [Scalpel](/tag/Scalpel)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)星阑科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t010136e53e1b35516c.png)

[![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)](/member.html?memberId=147620)

[星阑科技](/member.html?memberId=147620)

星阑科技

* 文章
* **119**

* 粉丝
* **46**

### TA的文章

* ##### [保护敏感数据的艺术：数据安全指南](/post/id/290760)

  2023-10-18 10:57:25
* ##### [受邀演讲 | 确保数字化生态安全稳健](/post/id/290528)

  2023-09-05 17:48:29
* ##### [技术专题：API资产识别大揭秘（一）](/post/id/290471)

  2023-09-05 17:37:14
* ##### [解密与探究：理解WebSocket协议与报文格式](/post/id/290500)

  2023-08-30 14:36:15
* ##### [创新护航：萤火助力守护数据跨境安全](/post/id/290512)

  2023-08-29 16:10:15

### 相关文章

* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃](/post/id/308349)

  2025-06-11 16:08:49
* ##### [“欧洲版CVE”上线，EUVD释放漏洞治理新信号](/post/id/307472)

  2025-05-16 18:04:21
* ##### [CVE-2025-24977:OpenCTI平台中的关键RCE缺陷将基础设施暴露为根级攻击](/post/id/307143)

  2025-05-07 16:32:13
* ##### [僵尸网络通过CVE-2024-6047和CVE-2024-11120开发旧GeoVision物联网设备](/post/id/307139)

  2025-05-07 16:27:26
* ##### [CVE-2025-47241:浏览器使用中的关键白名单绕过暴露了内部服务](/post/id/307134)

  2025-05-07 16:17:59
* ##### [CISA将Microsoft .NET和Apache OFBiz错误标记为在攻击中被利用](/post/id/303897)

  2025-02-06 15:03:21

### 热门推荐

文章目录

* [Scalpel 简介](#h2-0)
* [深度参数注入原理](#h2-1)
* [Scapel 功能介绍](#h2-2)
* [案例1：CVE-2022-1388F5 BIG-IPAPIUnauthenticated RCE漏洞的检测](#h2-3)
* [案例二：利用Scalpel工具挖掘多个0day漏洞](#h2-4)
* [工具地址](#h2-5)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)