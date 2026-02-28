---
title: 未修补的ActiveMQ漏洞引发二次入侵与LockBit勒索攻击
url: https://www.anquanke.com/post/id/314906
source: 安全客-有思想的安全新媒体
date: 2026-02-27
fetch_date: 2026-02-28T03:50:02.218948
---

# 未修补的ActiveMQ漏洞引发二次入侵与LockBit勒索攻击

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

# 未修补的ActiveMQ漏洞引发二次入侵与LockBit勒索攻击

阅读量**18823**

发布时间 : 2026-02-27 10:29:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/unpatched-activemq-flaw-leads-to-repeat-breach-and-lockbit-ransomware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在网络安全领域，将攻击者 “逐出网络” 往往并不代表事件终结。《DFIR Report》发布的最新案例显示，某企业因**Apache ActiveMQ 高危漏洞未修复**，被攻击者先后**两次入侵**，即便首次成功驱逐入侵者，最终仍遭 **LockBit 勒索软件** 加密。

入侵事件始于 2024 年 2 月中旬，攻击者针对一台**暴露在公网的 Apache ActiveMQ 服务器**发起攻击，所利用漏洞为 **CVE-2023-46604**，这是一个**高危远程代码执行（RCE）漏洞**，现已成为勒索组织最常用的突破口之一。

报告指出：“攻击者通过 Java Spring 类与自定义的 Spring Bean 配置 XML 文件，成功实现**远程代码执行**。”

攻击者借助 Windows 自带的 `CertUtil` 工具，从远程服务器下载恶意 XML 文件与攻击载荷，**拿下第一处立足点**。

尽管企业安全团队在首次入侵后**发现并驱逐了攻击者**，但**并未修补该漏洞**。

研究人员提到：“首次入侵被清理后，攻击者在 **18 天后再次攻破同一台服务器**，入侵成功。”

而这第二次入侵，直接开启了快速攻击链。

获得新的控制权后，攻击者使用 **Metasploit** 和 **Meterpreter** 进一步深入内网，成功**提权**，读取 **LSASS 进程内存**窃取凭证，并在内网中**横向移动**。

在完成网络拓扑探测与凭证收集后，攻击者 “**迅速部署勒索软件**”。

他们通过 **远程桌面协议（RDP）** 和窃取到的账号密码，在全网范围内分发加密载荷。

此次使用的勒索软件为 **LockBit Black（即 LockBit 3.0）** 变种。

调查人员判断，作案者更可能是**独立攻击者**，而非官方 LockBit 核心团伙。

报告提到：“勒索信并未采用标准 LockBit 格式，未指引受害者访问 Tor 泄密站点或通过 TOX/Jabber 沟通，而是要求其使用 Session 私密通讯软件。”

据此研究人员判断，此次攻击是 “**独立威胁分子利用泄露的勒索生成器，自行发起的攻击活动**”。

攻击者还在勒索信中使用了颇为 “专业” 的话术试图降低对抗情绪：

“相比其他勒索软件，我们收费低得多，别舍不得！”

甚至还把 “安全审计” 打包进赎金服务：

“我们会告诉你入侵所用的服务器漏洞，我们诚信经营！”

整个事件的核心教训十分清晰：

企业虽然 “赶走了” 攻击者，但**根本漏洞 —— 未打补丁的公网 ActiveMQ 服务器**依然存在，导致不到三周就被**一模一样的方式再次入侵**。

报告强烈建议各类机构：

必须**优先修补暴露在公网的应用**，并清醒认识到：

在漏洞彻底修复前，任何 “驱逐攻击者” 的操作都只是**临时措施**。

本文翻译自securityonline [原文链接](https://securityonline.info/unpatched-activemq-flaw-leads-to-repeat-breach-and-lockbit-ransomware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314906](/post/id/314906)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/unpatched-activemq-flaw-leads-to-repeat-breach-and-lockbit-ransomware/)

如若转载,请注明出处： <https://securityonline.info/unpatched-activemq-flaw-leads-to-repeat-breach-and-lockbit-ransomware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1030**

* 粉丝
* **6**

### TA的文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42

### 相关文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42
* ##### [Claude Code推出远程控制功能 实现移动端全自主开发](/post/id/314902)

  2026-02-27 10:28:57
* ##### [思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用](/post/id/314880)

  2026-02-27 10:28:35

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