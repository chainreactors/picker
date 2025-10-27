---
title: 12 K + KerioControl防火墙漏洞容易受到单击RCE漏洞利用
url: https://www.anquanke.com/post/id/304165
source: 安全客-有思想的安全新媒体
date: 2025-02-13
fetch_date: 2025-10-06T20:34:19.106402
---

# 12 K + KerioControl防火墙漏洞容易受到单击RCE漏洞利用

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

# 12 K + KerioControl防火墙漏洞容易受到单击RCE漏洞利用

阅读量**50442**

发布时间 : 2025-02-12 10:09:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/keriocontrol-firewall-1-click-rce/>

译文仅供参考，具体内容表达以及含义原文为准。

已在 GFI KerioControl 防火墙中发现一个严重的安全漏洞，编号为 CVE-2024-52875，受影响的版本为 9.2.5 至 9.4.5。

这个漏洞可被利用来进行远程代码执行（RCE），已经引起了网络犯罪分子的高度关注，全球数千台未打补丁的系统目前正处于危险之中。

该漏洞存在于 KerioControl Web 界面的几个无需身份验证的统一资源标识符（URI）路径中，包括 /nonauth/addCertException.cs、/nonauth/guestConfirm.cs 和 /nonauth/expiration.cs。

这些页面未能正确清理通过 dest GET 参数传递的用户输入，使得攻击者能够在 HTTP 响应中注入换行符（LF）。这种不当的输入处理为 HTTP 响应拆分攻击打开了方便之门，可能导致开放式重定向和反射型跨站脚本攻击（XSS）。

一个概念验证（PoC）漏洞利用示例展示了攻击者如何利用这一漏洞来执行恶意操作。具体而言，攻击者可以精心构造一个恶意 URL，当已认证的管理员点击该 URL 时，就会通过防火墙的固件升级功能触发恶意.img 文件的上传。这一过程最终会让攻击者获得系统的根权限。

由于该漏洞可通过无需身份验证的 URI 路径进行利用，因此特别危险，因为外部威胁行为者可以将其与社会工程策略相结合，诱骗管理员点击恶意链接。

**全球影响及漏洞利用情况**

截至 2025 年 2 月 9 日，影之服务器基金会（The Shadowserver Foundation）报告称，全球有 12229 台未打补丁的 KerioControl 设备暴露在外。影之服务器基金会分享的一张热度图显示，北美、欧洲和亚洲广泛存在这一漏洞。

该组织还在其蜜罐传感器中检测到针对这一特定漏洞的扫描活动，这表明威胁行为者正在积极尝试利用该漏洞。

自 2025 年 2 月 5 日起，我们每天都在报告存在 CVE-2024-52875 漏洞的 GFI Kerio Control 防火墙设备，该漏洞可能被用于远程代码执行。相关数据已分享在https://t.co/qxv0Gv5ELc。

2025 年 2 月 9 日，我们发现全球有 12229 台未打补丁的设备：https://t.co/LRMyelsSuL 图片网址：pic.twitter.com/9IOxPgmok4

—— 影之服务器基金会（@Shadowserver），2025 年 2 月 10 日

由于美国国家漏洞数据库（NVD）尚未发布官方公告，这进一步增加了漏洞缓解工作的复杂性。依赖这些防火墙的机构可能在遭遇数据泄露或收到像影之服务器这样的第三方安全监测机构的警报之前，都意识不到其中的风险。

未打补丁的 KerioControl 防火墙面临被攻击者攻陷的风险，攻击者可能会完全控制这些设备。一旦漏洞被利用，这些防火墙可能会成为更广泛的网络入侵的入口，或者被用于对连接的系统发动进一步攻击。

鉴于防火墙在保护机构网络安全方面的关键作用，成功利用该漏洞可能会导致数据泄露、勒索软件攻击或其他形式的网络犯罪。

**缓解措施及建议**

GFI 软件公司尚未发布针对 CVE-2024-52875 漏洞的公开补丁或公告。鉴于这一延迟，使用受影响版本 KerioControl 防火墙的机构应立即采取措施降低风险：

**1.限制访问**：仅允许受信任的 IP 地址访问 Web 界面，以此限制访问范围。

**2.监控指标**：检查防火墙系统上是否存在异常活动或被攻陷的迹象。

**3.应用更新**：定期检查 GFI 公司发布的固件更新，并在更新可用时立即应用。

**4.培训管理员**：对管理员进行培训，使其能够识别并避免点击可能利用该漏洞的可疑链接。

影之服务器基金会已敦促各机构迅速采取行动，核实其系统是否存在漏洞。他们建议各机构监控其控制面板以接收警报，并应用任何可用的补丁。

对 CVE-2024-52875 漏洞的利用凸显了及时进行补丁管理和采取主动安全措施的至关重要性。全球仍有超过 12000 台系统未打补丁，且已检测到野外存在的主动扫描行为，这一漏洞对依赖 GFI KerioControl 防火墙的机构构成了严重威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/keriocontrol-firewall-1-click-rce/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304165](/post/id/304165)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/keriocontrol-firewall-1-click-rce/)

如若转载,请注明出处： <https://cybersecuritynews.com/keriocontrol-firewall-1-click-rce/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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