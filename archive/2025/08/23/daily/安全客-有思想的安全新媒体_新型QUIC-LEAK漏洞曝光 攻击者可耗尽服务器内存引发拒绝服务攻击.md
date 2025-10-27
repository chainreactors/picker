---
title: 新型QUIC-LEAK漏洞曝光 攻击者可耗尽服务器内存引发拒绝服务攻击
url: https://www.anquanke.com/post/id/311428
source: 安全客-有思想的安全新媒体
date: 2025-08-23
fetch_date: 2025-10-07T00:18:01.717872
---

# 新型QUIC-LEAK漏洞曝光 攻击者可耗尽服务器内存引发拒绝服务攻击

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

# 新型QUIC-LEAK漏洞曝光 攻击者可耗尽服务器内存引发拒绝服务攻击

阅读量**62434**

发布时间 : 2025-08-22 17:14:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Florence Nightingale，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/quic-leak-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

### **QUIC-LEAK漏洞警报：LSQUIC实现存在内存耗尽缺陷 可致服务器拒绝服务**

LSQUIC的QUIC协议实现中发现一个关键握手前漏洞，远程攻击者可通过内存耗尽攻击使服务器崩溃。该漏洞被命名为”CVE-2025-54939″（QUIC-LEAK），影响全球第二大QUIC实现方案，可能波及**超过34%启用HTTP/3的网站**（基于LiteSpeed技术栈）。

核心发现：

1. CVE-2025-54939允许通过内存耗尽实施远程拒绝服务攻击
2. 影响14%使用LSQUIC/LiteSpeed技术的网站
3. 建议立即升级修复

据Imperva报告，QUIC-LEAK利用了LSQUIC在处理UDP数据报中聚合数据包的根本缺陷——该漏洞存在于连接握手建立之前。当攻击者构造包含多个QUIC初始数据包的恶意UDP数据报时（仅首个数据包包含有效目标连接ID，后续数据包使用无效DCID），就会触发此漏洞。

在`lsquic_engine.c`的漏洞代码路径中，实现方案能正确识别并忽略DCID不匹配的数据包，将其大小计入垃圾数据计数以防范放大攻击。然而，**关键缺陷在于未能通过lsquic\_mm\_put\_packet\_in函数正确释放packet\_in结构**，导致持续内存泄漏。

![]()

每个泄漏的packet\_in结构约占用96字节内存，而UDP数据报最多可携带10个聚合数据包，攻击者能以约70%的带宽速率持续消耗服务器内存。该攻击绕过了所有标准QUIC连接级防护措施——包括连接数限制、流控制和流量调控——因为这些保护机制仅在握手完成后激活。

![]()

### **缓解措施**

该漏洞CVSS 3.1基础评分为7.5分，研究人员指出其可用性影响应归类为”高危”，因为可能导致服务完全中断。全球占比超过14%的LiteSpeed服务器尤其脆弱，因其直接集成了受影响的LSQUIC库。

![]()

在采用512 MiB内存配置的受控测试中，研究人员证实：当内存使用率达到100%时，攻击可使OpenLiteSpeed服务器完全瘫痪。该攻击的有效性源于其**无状态特性**——无需建立有效QUIC会话或时间依赖。

立即缓解措施需升级至LSQUIC 4.3.1或更高版本（包含于OpenLiteSpeed 1.8.4和LiteSpeed Web Server 6.3.4）。无法立即升级的组织应实施网络层UDP流量过滤，对暴露服务执行严格内存使用限制，并持续监控针对QUIC端点的异常流量模式。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/quic-leak-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311428](/post/id/311428)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/quic-leak-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/quic-leak-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

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