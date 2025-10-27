---
title: CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃
url: https://www.anquanke.com/post/id/308349
source: 安全客-有思想的安全新媒体
date: 2025-06-12
fetch_date: 2025-10-06T22:49:26.025215
---

# CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃

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

# CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃

阅读量**1152444**

发布时间 : 2025-06-11 16:08:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/coredns-dos-flaw-unauthenticated-attackers-can-crash-servers-via-dns-over-quic/>

译文仅供参考，具体内容表达以及含义原文为准。

![CoreDNS漏洞,DoS攻击]()

在CoreDNS中发现了一个关键的拒绝服务(DoS)漏洞,CoreDNS是模块化DNS服务器,广泛部署在云原生和容器化环境中。跟踪为CVE-2025-47950,此漏洞影响DNS-over-QUIC(DoQ)实现,并允许未经身份验证的攻击者通过流放大攻击耗尽服务器内存 – 可能导致Out Of Memory(OOM)崩溃。

*“服务器之前为每个传入的QUIC流创建了一个新的goroutine,而不对并发流或goroutine的数量施加任何限制*[,”CoreDNS团队在其安全咨询中解释道。](https://github.com/coredns/coredns/security/advisories/GHSA-cvx7-x8pj-x2gw)

该漏洞存在于 1.1.22 之前的 CoreDNS 版本中,特别是影响在 Corefile 中启用 quic / / 的部署。通过向服务器充斥大量 QUIC 流,远程攻击者可以触发无界的 goroutine 创建和快速内存消耗,从而崩溃服务,特别是在内存受限或容器化环境中。

*“单个攻击者可能导致CoreDNS实例使用最小的带宽和CPU变得无响应*,”该咨询警告说。

该补丁在1.12.2版本中发布[1.12.2](https://github.com/coredns/coredns/releases/tag/v1.12.2),引入了两个关键保护措施:

* `①max_streams`: 限制每个连接的并发 QUIC 流数。默认值:256。
* `②worker_pool_size：`建立一个有界的工人池来管理流处理。默认值:1024。

这些缓解措施有效地用更具可扩展性和内存弹性的设计取代了之前的1:1流到华丽模型。用户可以在以下情况下配置这些值。`quic`clock 在 Corefile 中:

```
quic {
    max_streams 256
    worker_pool_size 1024
}
```

这消除了1:1的流到Goroutine模型,并确保CoreDNS在高并发性下保持弹性。

对于无法立即升级的用户,CoreDNS建议采取以下临时措施:

* ①禁用 QUIC 通过删除或注释`quic://`在 Corefile 中块。
* ②使用容器运行时资源限制来检测和隔离内存过度使用。
* ③监控 QUIC 流量以识别异常连接模式。

只有明确启用 QUIC 支持的部署才会受到影响。使用标准 DNS-over-UDP/TCP 设置的组织不受此漏洞的影响。

本文翻译自securityonline [原文链接](https://securityonline.info/coredns-dos-flaw-unauthenticated-attackers-can-crash-servers-via-dns-over-quic/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308349](/post/id/308349)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/coredns-dos-flaw-unauthenticated-attackers-can-crash-servers-via-dns-over-quic/)

如若转载,请注明出处： <https://securityonline.info/coredns-dos-flaw-unauthenticated-attackers-can-crash-servers-via-dns-over-quic/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [漏洞预警](/tag/%E6%BC%8F%E6%B4%9E%E9%A2%84%E8%AD%A6)
* [安全漏洞](/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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