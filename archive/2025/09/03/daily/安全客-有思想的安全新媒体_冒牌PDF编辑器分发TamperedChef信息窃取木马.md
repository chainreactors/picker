---
title: 冒牌PDF编辑器分发TamperedChef信息窃取木马
url: https://www.anquanke.com/post/id/311798
source: 安全客-有思想的安全新媒体
date: 2025-09-03
fetch_date: 2025-10-02T19:32:36.679872
---

# 冒牌PDF编辑器分发TamperedChef信息窃取木马

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

# 冒牌PDF编辑器分发TamperedChef信息窃取木马

阅读量**43840**

发布时间 : 2025-09-02 15:45:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ionut Ilascu，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/tamperedchef-infostealer-delivered-through-fraudulent-pdf-editor/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期，研究人员发现网络威胁团伙利用 **Google 广告** 推广多个伪造网站，以“免费 PDF 编辑软件”为诱饵，向用户投递名为 **TamperedChef** 的信息窃取型恶意软件。

此次行动规模庞大，至少涉及 **50 个域名**，这些站点托管着伪装应用，并使用来自 **至少四家公司** 的欺诈性数字签名证书。研究人员指出，攻击者手法精心策划，甚至在广告投放初期并未立刻激活恶意功能，而是等广告覆盖一定用户量后再远程下发恶意更新，从而提高感染率。

## 恶意更新触发信息窃取

来自网络安全公司 Truesec 的技术分析显示，TamperedChef 主要通过一个名为 **AppSuite PDF Editor** 的应用传播。

调查发现，该活动最早可追溯至 **6 月 26 日**，当时多个相关网站开始注册或上线推广。然而，早在 **5 月 15 日**，这款恶意应用就已经通过 VirusTotal 的检测提交。

初期的 PDF 编辑器看似功能正常，直到 **8 月 21 日** 收到更新后，才激活了恶意模块，开始窃取用户敏感数据，包括凭证与浏览器 Cookies。

![]()

Truesec 发现，恶意功能通过给 PDF 编辑器的可执行文件加入 **“-fullupdate” 参数**来触发。木马会在宿主设备上检测安全防护软件，并调用 Windows **DPAPI（数据保护应用编程接口）** 解密并提取浏览器数据库中的敏感信息。

研究人员还追踪到，该恶意程序的推广依赖 **Google 广告投放**，至少关联 **5 个不同的广告系列 ID**，表明攻击范围广泛。攻击者还精心计算投毒时机——选择在广告生命周期约 **60 天**的临近结束时才释放信息窃取木马，以确保最大下载量。

更令人担忧的是，不同版本的 AppSuite PDF Editor 使用了来自 **ECHO Infini SDN BHD、GLINT By J SDN BHD、SUMMIT NEXUS Holdings LLC** 等公司的签名证书，显示攻击者已获取或伪造了多家企业的数字身份。

## 隐秘的代理网络诱导

Truesec 进一步调查发现，该威胁团伙至少自 **2024 年 8 月**以来就已活跃，除 PDF 编辑器外，还曾推广 **OneStart、Epibrowser** 等应用。

其中 **OneStart 浏览器**常被标记为“潜在有害程序（PUP）”，但研究人员发现，它与 AppSuite PDF Editor 等工具一样，会下载可疑文件、执行异常命令，甚至将用户设备注册进 **住宅代理网络**。

另一家网络安全公司 Expel 也发现了类似现象：包括 **AppSuites PDF Editor、ManualFinder 和 OneStart** 在内的应用，都存在投递可疑文件、执行恶意操作并强制主机加入代理网络的行为。

研究还发现，在某些版本的 PDF Editor 中，应用会直接弹窗，要求用户同意将其设备用作 **住宅代理节点**，以换取免费使用软件的权利。值得注意的是，相关代理服务提供商可能是合法企业，并不直接参与攻击，而恶意应用开发者则通过 **代理联盟获利**。

换句话说，攻击者正试图以用户资源为代价，最大化自身经济收益。

## “PUP”外衣下的恶意本质

虽然这些应用可能被部分安全厂商标注为 PUP，但其实际行为已接近甚至完全符合恶意软件特征，应被视为 **高风险威胁**。

Truesec 和 Expel 的研究均表明，这一行动涉及的应用范围更大，其中部分尚未“武器化”，但未来可能被用来 **分发恶意软件、执行远程命令或窃取数据**。

研究人员提醒，目前用于该活动的签名证书已被吊销，但已安装的应用仍然存在风险。两家机构也在报告中提供了大量 **妥协指标（IoCs）**，供防御方检测和阻止相关威胁。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/tamperedchef-infostealer-delivered-through-fraudulent-pdf-editor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311798](/post/id/311798)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/tamperedchef-infostealer-delivered-through-fraudulent-pdf-editor/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/tamperedchef-infostealer-delivered-through-fraudulent-pdf-editor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [恶意更新触发信息窃取](#h2-0)
* [隐秘的代理网络诱导](#h2-1)
* [“PUP”外衣下的恶意本质](#h2-2)

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