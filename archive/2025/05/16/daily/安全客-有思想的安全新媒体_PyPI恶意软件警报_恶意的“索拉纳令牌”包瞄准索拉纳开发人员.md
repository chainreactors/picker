---
title: PyPI恶意软件警报:恶意的“索拉纳令牌”包瞄准索拉纳开发人员
url: https://www.anquanke.com/post/id/307421
source: 安全客-有思想的安全新媒体
date: 2025-05-16
fetch_date: 2025-10-06T22:23:19.809395
---

# PyPI恶意软件警报:恶意的“索拉纳令牌”包瞄准索拉纳开发人员

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

# PyPI恶意软件警报:恶意的“索拉纳令牌”包瞄准索拉纳开发人员

阅读量**138208**

发布时间 : 2025-05-15 16:41:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pypi-malware-alert-malicious-solana-token-package-targets-solana-developers/>

译文仅供参考，具体内容表达以及含义原文为准。

![PyPI恶意软件,Solana开发人员]()

ReversingLabs研究团队发现了另一个针对加密货币生态系统的软件供应链攻击,这次涉及一个名为solana-token的流氓Python包。作为Solana开发人员的合法实用程序,该软件包在Python包索引(PyPI)上被发现,在删除之前已被下载超过600次。

Solana是一个受欢迎的区块链平台,以高速,低费用交易而闻名,继续吸引开发人员和威胁行为者的兴趣。[malicious](https://securityonline.info/mcafee-premium-review-all-around-protection-for-your-digital-life-but-is-it-the-best/)恶意的solana-toked包利用了这种受欢迎程度,伪装成开发人员在基于Solana的应用程序上的工具。

*“虽然该软件包的PyPI着陆页没有包含描述,但包名称和功能表明,希望创建自己区块链的开发人员可能是目标*[,”ReversingLabs团队写道。](https://www.reversinglabs.com/blog/same-name-different-hack-pypi-package-targets-solana-developers)

恶意软件包包含妥协的迹象,包括:

* 用于窃取被盗数据的硬编码IP地址
* 非标准网络端口的出站通信
* 读取本地文件的代码,在 infostealers 中经常看到的行为

*包中一个特别阴险的方法“扫描了Python执行堆栈,然后将执行链中所有文件中包含的源代码复制和泄露到远程服务器。*

目的是窃取开发人员的秘密和硬编码的加密凭据,这些凭证通常不在源代码中未受保护。[information](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/)[attackers](https://securityonline.info/bitdefender-gravityzone-small-business-security-review-enterprise-grade-protection-without-the-enterprise-headache/)这种敏感信息可能会让攻击者未经授权访问加密货币钱包和关键基础设施。

这不是这个包名第一次浮出水面。事实上,之前的同名软件包在2024年发布并删除。但由于早期删除的方式 – 由软件包作者,而不是PyPI安全人员 – 名称再次可用。

*“这使得软件包名称可用于重用……这表明相同的恶意行为者删除了早期的solana-token包可能是新的恶意版本的背后[malicious](https://securityonline.info/mcafee-premium-review-all-around-protection-for-your-digital-life-but-is-it-the-best/)*,”报告指出。

本文翻译自securityonline [原文链接](https://securityonline.info/pypi-malware-alert-malicious-solana-token-package-targets-solana-developers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307421](/post/id/307421)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pypi-malware-alert-malicious-solana-token-package-targets-solana-developers/)

如若转载,请注明出处： <https://securityonline.info/pypi-malware-alert-malicious-solana-token-package-targets-solana-developers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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