---
title: Mac 用户警惕：“MacSync”恶意软件诱导你“亲手”入侵自己的设备
url: https://www.anquanke.com/post/id/314522
source: 安全客-有思想的安全新媒体
date: 2026-01-26
fetch_date: 2026-01-27T03:37:02.554271
---

# Mac 用户警惕：“MacSync”恶意软件诱导你“亲手”入侵自己的设备

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

# Mac 用户警惕：“MacSync”恶意软件诱导你“亲手”入侵自己的设备

阅读量**16081**

发布时间 : 2026-01-26 14:12:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/mac-users-beware-macsync-malware-tricks-you-into-hacking-yourself/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种高度复杂的新型恶意软件攻击正瞄准 macOS 用户，它将**社会工程学**与**技术隐蔽性**结合得极为致命。这个名为 **MacSync** 的恶意软件被包装成 “恶意软件即服务”（MaaS），伪装成合法的云存储安装程序，诱骗用户**亲手**感染自己的设备，并专门窃取加密货币钱包和各类凭据。

该攻击在一次例行威胁狩猎中被发现，采用了 “ClickFix” 诱导手段 —— 即通过伪造错误提示，迫使受害者在终端中粘贴恶意命令来 “修复问题” 或完成安装。

感染通常从伪装成可信下载门户的网站开始。在一个被观察到的案例中，一个 “模仿 Microsoft 登录页面的域名” 将用户重定向到一个伪装成 “合法 macOS 云存储安装程序” 的站点。

与常规下载不同，该网站指示 “高级用户” 进行 “终端安装”。“页面强迫用户复制并粘贴一条具有欺骗性的终端命令。” 报告解释道。

这条看似无害的单行命令实际上会从远程服务器获取脚本，从而绕过 macOS 的安全机制，包括 **Gatekeeper** 和 **软件公证（notarization）**。“通过诱使受害者自愿执行恶意 shell 命令，攻击者可以完全绕过 Gatekeeper、公证检查和签名验证。”

一旦进入系统，MacSync 不仅窃取数据，还会进行长期驻留。该恶意软件会 “有条件地植入（trojanize）受害者设备上广泛使用的基于 Electron 的加密货币应用”。

通过覆盖 Ledger Live 或 Trezor Suite 等应用的关键组件，恶意软件会将这些受信任的硬件钱包配套软件变成钓鱼工具。“这两类被植入的应用的主要目标，是呈现一个高度逼真的多步骤钓鱼向导，以窃取设备 PIN 和完整的助记词（recovery phrase）。”

受害者可能会在最初感染数周后看到一个看似友好的 “Something went wrong…” 提示，诱导他们重新输入助记词以 “修复问题”—— 从而交出其加密资产的全部控制权。

MacSync 在地下论坛上被当作一种 “经济实惠” 的恶意软件即服务出售。“由于价格低廉，MacSync 在低级别附属攻击者中迅速流行。”

尽管成本不高，其功能却相当先进。它会系统性地窃取 “浏览器凭据、加密货币钱包数据、钥匙串（Keychain）内容以及敏感文件”，对个人用户和企业组织都构成严重威胁。

报告最后发出警告：技术防御在社会工程学面前作用有限。“MacSync 证明，在 macOS 上，最危险的恶意软件不是利用零日漏洞的那种，而是利用信任的那种。”

最有效的防御仍然很简单：“永远不要将随机命令粘贴到终端中，无论它看起来多么‘官方’。”

本文翻译自securityonline [原文链接](https://securityonline.info/mac-users-beware-macsync-malware-tricks-you-into-hacking-yourself/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314522](/post/id/314522)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/mac-users-beware-macsync-malware-tricks-you-into-hacking-yourself/)

如若转载,请注明出处： <https://securityonline.info/mac-users-beware-macsync-malware-tricks-you-into-hacking-yourself/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30
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