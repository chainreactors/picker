---
title: Windows远程桌面网关UAF漏洞允许远程代码执行
url: https://www.anquanke.com/post/id/307503
source: 安全客-有思想的安全新媒体
date: 2025-05-20
fetch_date: 2025-10-06T22:23:56.237185
---

# Windows远程桌面网关UAF漏洞允许远程代码执行

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

# Windows远程桌面网关UAF漏洞允许远程代码执行

阅读量**115500**

发布时间 : 2025-05-19 15:18:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 古鲁 巴兰，文章来源：cybersecuritynews

原文地址：<http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/>

译文仅供参考，具体内容表达以及含义原文为准。

微软的远程桌面网关(RD Gateway)中的一个关键漏洞,可能允许攻击者在受影响的系统上远程执行恶意代码。

[该漏洞被跟踪为CVE-2025-21297](https://cybersecuritynews.com/microsoft-january-2025-patch-tuesday/),由微软在2025年1月的安全更新中披露,此后一直被野外积极利用。

昆仑实验室的VictorV(Tang Tianwen)发现并报告的缺陷源于远程桌面网关服务初始化期间由并发套接连接触发的无使用(UAF)错误。

具体来说,该漏洞存在于 aaedge.dll 库中,在 CTsgMsgServer::GetCTsgMsgServerInstance 函数中,其中全局指针(m\_pMsgSvrInstance)在没有正确线程同步的情况下初始化全局指针(m\_pMsgSvrInstance)。

“当多个线程可以覆盖相同的全局指针,损坏参考计数并最终导致悬空指针的延迟 – 经典的UAF场景时,就会发生漏洞[security advisory](https://v-v.space/2025/05/15/CVE-2025-21297/),”安全咨询解释说。

比赛条件允许攻击者利用内存分配和指针分配不同步的定时问题,可能导致任意代码执行。Microsoft 已将该漏洞的 CVSS 分数分配为 8.1,表明其严重程度很高。

### **Windows 远程桌面网关 UAF 漏洞**

根据研究人员的说法,成功的利用需要攻击者:

1. 连接到运行 [RD Gateway](https://cybersecuritynews.com/what-is-border-gateway-protocol-bgp/) 角色的系统。
2. 触发与 RD 网关的并发连接(通过多个套接字 ) 。
3. 利用内存分配和指针分配发生不同步的定时问题。
4. 导致一个连接在另一个连接完成引用之前覆盖指针。

该漏洞涉及线程之间堆碰撞的九步时间线,导致最终使用自由内存块,为任意代码执行打开大门。

使用 RD 网关进行安全远程访问的多个版本的 Windows Server 都容易受到攻击,包括:

* Windows Server 2016(核心和标准安装)。
* Windows Server 2019(核心和标准安装)。
* Windows Server 2022(核心和标准安装)。
* Windows Server 2025(核心和标准安装)。

使用 RD Gateway 作为远程工作的员工、承包商或合作伙伴的关键接入点的组织尤其面临风险。

![]()

微软在2025年5月通过引入基于互动器的同步来解决该漏洞[,](https://cybersecuritynews.com/microsoft-patch-tuesday-may-2025/)确保在任何给定时间只有一个线程可以初始化全局实例。提供以下安全更新:

* Windows Server 2016:更新KB5050011。
* Windows Server 2019:更新KB5050008(Build 10.0.17763.6775)。
* Windows Server 2022:更新KB5049983(Build 1.0.2.0348.30391)。
* Windows Server 2025:更新KB5050009(Build 10.0.26100.2894)。

安全专家强烈敦促组织立即应用这些补丁。“对于依赖远程桌面网关进行安全远程访问的企业环境来说,此漏洞构成了关键风险,”一位熟悉该问题的安全研究人员指出。

在应用补丁之前,建议组织监控RD Gateway日志以查找异常活动,并考虑实施网络级保护,以限制与可信源的传入连接。

本文翻译自cybersecuritynews [原文链接](http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307503](/post/id/307503)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/)

如若转载,请注明出处： <http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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