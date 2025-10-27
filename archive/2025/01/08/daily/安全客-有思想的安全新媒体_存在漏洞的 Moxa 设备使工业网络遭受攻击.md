---
title: 存在漏洞的 Moxa 设备使工业网络遭受攻击
url: https://www.anquanke.com/post/id/303300
source: 安全客-有思想的安全新媒体
date: 2025-01-08
fetch_date: 2025-10-06T20:08:33.033404
---

# 存在漏洞的 Moxa 设备使工业网络遭受攻击

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

# 存在漏洞的 Moxa 设备使工业网络遭受攻击

阅读量**49691**

发布时间 : 2025-01-07 09:56:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/vulnerable-moxa-devices-expose-industrial-networks-to-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Vulnerable Moxa devices expose industrial networks to attacks]()

工业网络和通信提供商 Moxa 警告称，其蜂窝路由器、安全路由器和网络安全设备的不同型号存在一个高度严重漏洞和一个关键漏洞。

这两个安全问题允许远程攻击者在有漏洞的设备上获得 root 权限并执行任意命令，从而导致任意代码执行。

**Moxa 路由器的风险**

Moxa设备被用于交通、公用事业、能源和电信部门的工业自动化和控制系统环境中。

周五，该供应商针对以下两个漏洞发布了紧急警告：

**CVE-2024-9138（8.6，严重程度高）**： 硬编码凭证使通过验证的用户能够将权限升级到 root

**CVE-2024-9140（9.3，严重程度分值）**： 利用不当输入限制造成的操作系统命令注入漏洞，导致任意代码执行

第二个缺陷特别危险，因为它可被远程攻击者利用。

Moxa 已发布固件更新来解决这些漏洞，并指出 “强烈建议立即采取行动，以防止潜在的漏洞利用并降低这些风险”。

以下设备受到 CVE-2024-9140 和 CVE-2024-9138 的影响：

* 固件 3.13.1 及更早版本的 EDR-8010 系列
* 固件 3.13.1 及更早版本的 EDR-G9004 系列
* 固件 3.13.1 及更早版本上的 EDR-G9010 系列
* EDF-G1002-BP 系列，固件 3.13.1 及更早版本
* 固件 1.0.5 及更早版本的 NAT-102 系列
* OnCell G4302-LTE4 系列，固件 3.13 及更早版本
* 固件为 3.13 及更早版本的 TN-4900 系列

此外，固件 5.12.37 及更早版本的 EDR-810 系列、固件 5.7.25 及更早版本的 EDR-G902 系列，以及固件 3.13 及更早版本的 TN-4900 系列只受 CVE-2024-9138 影响。

EDR-8010 系列、EDR-G9004 系列、EDR-G9010 和 EDF-G1002-BP 系列用户应升级到 2024 年 12 月 31 日发布的固件 3.14 版，以解决该问题。

建议按照 Moxa 公告中提供的各设备型号下载链接获取官方固件镜像。

建议 OnCell G4302-LTE4 系列和 TN-4900 系列的管理员联系 Moxa 支持部门以获得补丁指导。

对于 NAT-102 系列，目前没有可用的补丁，建议管理员应用缓解措施。

Moxa 建议限制设备的网络暴露和 SSH 访问，并使用防火墙、IDS 或入侵防御系统 (IPS) 来监控和阻止利用尝试。

该公告明确提到，MRC-1002 系列、TN-5900 系列和 OnCell 3120-LTE-1 系列设备不存在这两个漏洞。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/vulnerable-moxa-devices-expose-industrial-networks-to-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303300](/post/id/303300)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/vulnerable-moxa-devices-expose-industrial-networks-to-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/vulnerable-moxa-devices-expose-industrial-networks-to-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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