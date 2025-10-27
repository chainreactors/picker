---
title: Grafana 0天漏洞让攻击者将用户重定向到恶意网站
url: https://www.anquanke.com/post/id/307690
source: 安全客-有思想的安全新媒体
date: 2025-05-24
fetch_date: 2025-10-06T22:27:13.899760
---

# Grafana 0天漏洞让攻击者将用户重定向到恶意网站

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

# Grafana 0天漏洞让攻击者将用户重定向到恶意网站

阅读量**133777**

发布时间 : 2025-05-23 16:58:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 卡维亚，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/grafana-0-day-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

[Grafana中的高严重跨站点脚本(XSS)](https://cybersecuritynews.com/cisa-adds-mdaemon-email-server-xss-vulnerability/)漏洞可能允许攻击者将用户重定向到恶意网站。

该漏洞在CVE-2025-4123收到7.6(HIGH)的CVSS分数时跟踪,允许攻击者利用客户端路径遍历和打开重定向,通过自定义前端插件执行任意JavaScript代码。

该漏洞最初计划于5月22日进行修补,但在该漏洞泄露给公众后提前发布。

安全研究员阿尔瓦罗·巴拉达(Alvaro Balada)通过该公司的漏洞赏金计划发现并报告了格拉法纳的漏洞。

### **Grafana XSS 漏洞**

该漏洞特别危险,因为与Grafana中的许多其他XSS漏洞不同,它不需要编辑器权限来利用。

如果在 Grafana 实例上启用了匿名访问,XSS 攻击将无需任何身份验证即可工作。

这大大扩展了许多使用Grafana进行监控解决方案的组织的潜在攻击面。

该漏洞影响Grafana OSS和Grafana Enterprise,所有当前支持和不受支持的版本至少可以追溯到Grafana 8。

但是,Grafana Cloud 实例不受此漏洞的影响,Grafana Labs 证实了这一点。

此漏洞的技术后果超出了简单的 XSS 攻击。与 Grafana Image Renderer 插件结合使用时,[该漏洞可能会被滥用为完整读取的 Server-Side 请求伪造 (SSRF](https://cybersecuritynews.com/400-ips-actively-exploiting-multiple-ssrf-vulnerabilities/))。

这种组合允许攻击者潜在地暴露内部服务和云元数据,为受影响的组织带来重大安全风险。

成功利用可能导致会话劫持或完成账户接管。该漏洞源于自定义前端插件中用户提供的路径处理不当,从而创建了XSS和开放重定向问题。

该漏洞遵循与之前 Grafana 安全问题类似的模式,其中利用了路径遍历和重定向漏洞。

2021年,[Grafana面临类似的零日漏洞](https://cybersecuritynews.com/windows-clfs-zero-day-vulnerability-actively-exploited-by-ransomware-group/)(CVE-2021-43798),允许攻击者在Grafana文件夹之外穿越并远程访问受限制文件。

![]()

### **可用补丁**

Grafana Labs 发布了所有支持版本的补丁版本:Grafana 12.0.0+security-01、11.6+security-01、11.5.4+security-01、11.4.4+security-01、11.3.6+security-01、11.9+security-01、11.4.1+security-01。

运行受影响版本的组织应立即更新。

对于无法立即升级的组织,可以通过在 Grafana 配置文件(grafana.ini)中实现内容安全策略配置来提供替代缓解:

此 CSP 配置有助于阻止攻击向量,即使在易受攻击的版本。

红帽还通过安全公告发布了 Enterprise Linux 8、9 和 10 中受影响版本的安全更新。

组织还应考虑审查其匿名访问设置,并在Grafana实例前实施额外的安全控制,如反向代理。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/grafana-0-day-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307690](/post/id/307690)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/grafana-0-day-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/grafana-0-day-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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