---
title: 攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址
url: https://www.anquanke.com/post/id/314467
source: 安全客-有思想的安全新媒体
date: 2026-01-23
fetch_date: 2026-01-24T03:29:50.968241
---

# 攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址

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

# 攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址

阅读量**26681**

发布时间 : 2026-01-23 10:21:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/attackers-abuse-discord-to-deliver-clipboard-hijacker/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款新型**剪贴板劫持程序**正利用 Discord 社区的用户信任，暗中盗取游戏玩家与直播博主的加密货币资产。

此次攻击活动的核心是一款伪装成直播辅助工具或安全工具的恶意 Windows 程序，一经安装便会在后台静默监控用户剪贴板，伺机捕获用户复制的**加密货币钱包地址**。

当受害者将钱包地址粘贴至加密货币交易所、钱包应用或支付输入框时，该恶意软件会将其替换为攻击者控制的地址，在**无明显痕迹**的情况下完成资金转移。

被安全研究人员标记为**RedLineCyber**的攻击团伙，将目标锁定在与游戏、博彩及加密货币直播相关的 Discord 服务器。

该团伙会主动与服务器成员建立信任关系，伪装成工具开发者，通过私下渠道发送名为**Pro.exe**或**peeek.exe**的恶意文件。

他们向受害者谎称，这款工具能在直播过程中协助管理或保护钱包地址，让程序看似具备实用价值，从而降低用户的警惕性。

在这番看似友好的推销背后，实则是一场针对性极强的盗窃行动 —— 受害者只需一次粘贴操作的疏忽，账户内的交易资金就可能被悄悄转空。

CloudSEK 的安全分析师在监控网络犯罪分子活跃的地下社区与 Discord 频道时，发现了这一攻击活动。

在此次人工情报排查工作中，研究人员识别出该团伙伪造的**RedLine Solutions**虚假身份，并追溯到这款恶意软件的本源：一款由**PyInstaller**打包的 Python 基可执行程序。

研究人员的分析证实，该程序并非传统的信息窃取类恶意软件，其攻击行为高度聚焦于单一目标：**篡改与主流加密货币相关的剪贴板数据**。

![]()

此次攻击的危害性极大，原因在于其精准瞄准了用户**注意力最薄弱**的操作环节。许多直播博主与高频交易用户在复制粘贴冗长的钱包地址时，并不会逐一核对每一个字符。

该恶意软件运行时**无命令与控制通信流量**，且仅占用极少的系统资源，因此能在设备中长期潜伏，伺机等待高价值的资金转账操作。

从攻击者预置钱包地址关联的区块链交易记录来看，比特币、以太坊、索拉纳、狗狗币、莱特币及波场等主流加密货币，均已出现资产被盗的相关记录。

### 感染机制与剪贴板劫持逻辑

受害者运行**Pro.exe**后，恶意软件会在 Windows 系统的 \*\*% APPDATA%\*\* 目录下创建名为**CryptoClipboardGuard**的文件夹，并将自身添加至当前用户注册表的开机启动项中。

这一操作能确保恶意软件随系统开机自动运行，在后台持续潜伏且**无任何可视窗口**。

该可执行程序内置了独立的 Python 运行环境与经过混淆处理的字节码，即便目标设备未安装 Python 环境，程序仍能正常运行。

程序启动后会进入高频检测循环，**每秒约三次**扫描用户的剪贴板内容。

![]()

每当剪贴板内容发生变化，恶意软件会通过**Base64 编码的正则表达式**，对内容进行扫描，匹配各大主流加密货币的钱包地址格式。

一旦检测到有效钱包地址，程序会立即将剪贴板内容替换为该加密货币对应的**攻击者预置钱包地址**，并将此次替换操作记录在 \*\*% APPDATA%\CryptoClipboardGuard\*\* 目录下的**activity.log**日志文件中。

![]()

由于地址替换发生在**复制与粘贴的间隙**，大多数受害者直到发现资金转入错误的钱包，才会察觉地址被篡改 —— 而此时，资金转账操作已无法撤销。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/attackers-abuse-discord-to-deliver-clipboard-hijacker/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314467](/post/id/314467)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/attackers-abuse-discord-to-deliver-clipboard-hijacker/)

如若转载,请注明出处： <https://cybersecuritynews.com/attackers-abuse-discord-to-deliver-clipboard-hijacker/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **950**

* 粉丝
* **6**

### TA的文章

* ##### [威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件](/post/id/314458)

  2026-01-23 10:23:22
* ##### [遭野外利用：思科关键RCE漏洞（CVE-2026-20045）已被攻击](/post/id/314457)

  2026-01-23 10:22:51
* ##### [CVE-2025-13878：高严重性BIND漏洞可致服务器远程崩溃](/post/id/314469)

  2026-01-23 10:22:16
* ##### [攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址](/post/id/314467)

  2026-01-23 10:21:16
* ##### [带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件](/post/id/314481)

  2026-01-23 10:20:42

### 相关文章

* ##### [威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件](/post/id/314458)

  2026-01-23 10:23:22
* ##### [遭野外利用：思科关键RCE漏洞（CVE-2026-20045）已被攻击](/post/id/314457)

  2026-01-23 10:22:51
* ##### [CVE-2025-13878：高严重性BIND漏洞可致服务器远程崩溃](/post/id/314469)

  2026-01-23 10:22:16
* ##### [带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件](/post/id/314481)

  2026-01-23 10:20:42
* ##### [蓝色起源推出太赫兹波卫星网络：6Tbps速率对标星链](/post/id/314480)

  2026-01-23 10:19:44
* ##### [勒索软件组织RansomHub攻击苹果供应商立讯精密，窃取1TB未发布产品数据](/post/id/314487)

  2026-01-23 10:19:09
* ##### [攻击者盯上飞塔刚修复的高危漏洞](/post/id/314490)

  2026-01-23 10:18:21

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