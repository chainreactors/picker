---
title: “SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具
url: https://www.anquanke.com/post/id/314518
source: 安全客-有思想的安全新媒体
date: 2026-01-26
fetch_date: 2026-01-27T03:36:56.518572
---

# “SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具

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

# “SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具

阅读量**23963**

发布时间 : 2026-01-26 14:14:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/sympy-imposter-typosquatting-attack-turns-math-library-into-crypto-miner/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Python 生态中出现了一起隐蔽的新型供应链攻击：一个伪装成知名数学库 **SymPy** 的恶意包正在将开发者的机器悄悄变成加密货币挖矿节点。Socket 威胁研究团队已将这个名为 **sympy-dev** 的恶意包标记为危险的 “拼写劫持（typosquatting）” 攻击，其目的是诱骗用户下载它而非正版 SymPy。

该攻击利用了开发者对开源仓库的信任。“Socket 威胁研究团队发现了一个恶意 PyPI 包 sympy-dev，它仿冒了 SymPy—— 一个每月下载量约 8500 万次的广泛使用的符号数学库。” 报告指出。

攻击者煞费苦心地让这个伪造包看起来十分逼真。“攻击者将 SymPy 的项目描述和品牌元素复制到 sympy-dev 的页面中，以增加用户误安装的概率。”

通过使用常见的命名方式 —— 在包名后加 -dev 以暗示这是开发版本 —— 攻击者在发布第一天就成功诱骗了 **超过 1000 次下载**。“下载量不等于实际感染量，但早期的下载数据表明该包很快进入了真实的开发者环境和 CI 系统。”

与粗暴的 “抢即跑” 攻击不同，该恶意软件的行为异常隐蔽。它不会在安装后立即执行，而是 “在特定多项式函数运行时才激活恶意代码；这种更隐蔽的方式能更好地混入正常的 SymPy 使用场景中”。

当开发者调用特定的数学函数（例如 Groebner 基计算）时，隐藏的恶意代码就会被触发。“被调用时，被植入后门的函数会从远程服务器获取 JSON 配置，下载由攻击者控制的 ELF 载荷，并通过匿名的内存文件描述符执行它。”

这种利用 **memfd\_create** 的执行方式可以帮助恶意软件绕过传统的基于磁盘扫描的杀毒软件。

与隐蔽的投放方式相比，载荷本身的行为则毫不掩饰：它是一个 **加密货币挖矿程序**。“在动态分析中获取的样本显示，下载的载荷是 XMRig 加密挖矿程序，其配置会通过 TLS 连接到挖矿池的 Stratum 端点。”

然而研究人员警告称，该攻击基础设施是模块化的。“在此次攻击中我们观察到的是 XMRig 挖矿行为，但同一执行链可以在 Python 进程权限下执行任意代码。” 这意味着攻击者可以在不修改包的情况下，随时将挖矿程序替换为勒索软件或数据窃取工具。

该恶意包于 **2026 年 1 月 17 日** 发布，在报告发布时仍存在于 PyPI 上。Socket 已申请将其下架，但这一事件再次提醒人们软件供应链的脆弱性。

“防御者应预期，嵌入分阶段下载器和内存执行的拼写劫持包将会持续存在并不断演变。” 研究人员警告说。他们建议团队 “优先采用依赖项锁定（dependency pinning）和完整性校验”，以避免未来成为类似攻击的受害者。

本文翻译自securityonline [原文链接](https://securityonline.info/sympy-imposter-typosquatting-attack-turns-math-library-into-crypto-miner/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314518](/post/id/314518)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sympy-imposter-typosquatting-attack-turns-math-library-into-crypto-miner/)

如若转载,请注明出处： <https://securityonline.info/sympy-imposter-typosquatting-attack-turns-math-library-into-crypto-miner/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **960**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30

### 相关文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30
* ##### [Mac 用户警惕：“MacSync”恶意软件诱导你“亲手”入侵自己的设备](/post/id/314522)

  2026-01-26 14:12:18
* ##### [CVE-2026-22822：External Secrets Operator严重漏洞破坏命名空间隔离机制](/post/id/314529)

  2026-01-26 14:11:37
* ##### [Google推出「个人智能」AI模式，打造专属个性化搜索体验](/post/id/314541)

  2026-01-26 14:07:37

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