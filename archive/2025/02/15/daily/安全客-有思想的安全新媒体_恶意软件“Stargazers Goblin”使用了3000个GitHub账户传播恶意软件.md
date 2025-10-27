---
title: 恶意软件“Stargazers Goblin”使用了3000个GitHub账户传播恶意软件
url: https://www.anquanke.com/post/id/304345
source: 安全客-有思想的安全新媒体
date: 2025-02-15
fetch_date: 2025-10-06T20:32:58.146280
---

# 恶意软件“Stargazers Goblin”使用了3000个GitHub账户传播恶意软件

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

# 恶意软件“Stargazers Goblin”使用了3000个GitHub账户传播恶意软件

阅读量**99242**

发布时间 : 2025-02-14 16:52:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Matthew Connatser，文章来源：theregister

原文地址：<https://www.theregister.com/2024/07/26/github_stargazers_goblin_malware/>

译文仅供参考，具体内容表达以及含义原文为准。

信息安全研究人员发现了一个由三千多个恶意的 GitHub 账户组成的网络，该网络被用于传播恶意软件，目标群体包括游戏玩家、恶意软件研究人员，甚至还有其他试图传播恶意软件的威胁行为者。

这项由 Check Point 软件公司的安东尼奥斯・泰雷福斯（Antonis Terefos）撰写的研究，将这些 GitHub 账户的集合命名为 “观星者幽灵网络”，并声称它是由一个被这家网络安全公司称为 “占星者地布林” 的威胁行为者所操控。

不管怎么称呼它，推动这一行动的乌合之众采用了两种新奇的策略。

其一是无邮件钓鱼攻击。泰雷福斯认为，人们对电子邮件心存疑虑，所以 “占星者地布林” 会在诸如 Discord 这样的服务平台上发布恶意链接。目标对象是那些 “想要在 Twitch、Instagram、YouTube、Twitter、Trovo 和 TikTok 上增加‘粉丝数量’，或者想要使用与 Kick Chat、Telegram、电子邮件和 Discord 相关的其他工具功能” 的人。

如果这些目标对象点击了链接，他们就会遇到 “占星者地布林” 的第二个邪恶 “发明”：一个由看似无害实则具有欺骗性的 GitHub 账户组成的网络。实际上，这些账户执行着不同的功能来帮助传播恶意软件，但又没有明显到让这个代码协作服务平台将它们封禁。

其中一些账户甚至还被其他 GitHub 账户标记为 “星标” 或通过了验证，这让它们看起来颇具合法性。

但它们暗藏危险。研究人员观察到，一些代码库中包含一个文件，其中的 README.md 文件里有 “一个网络钓鱼下载链接，该链接甚至不会重定向到代码库自身的发布内容。相反，它使用了三个具有不同‘职责’的 GitHub 幽灵账户”。

第一个账户提供 “网络钓鱼” 代码库模板；

第二个账户提供用于网络钓鱼模板的 “图片”；

第三个账户在发布内容中以受密码保护的存档形式提供恶意软件。

而当受害者访问那个存档时…… 你知道接下来会发生什么。

泰雷福斯写道，这种多账户结构意味着 “占星者地布林” 能够 “迅速‘修复’任何可能因账户或代码库因恶意活动被封禁而出现的无效链接”。这也意味着该网络能够迅速替换被攻破的组件，很可能是通过自动化手段实现的，也就是说，关停危险账户并不会干扰恶意软件的传播操作。

生成式人工智能可能也被用于创建看似合法的代码库和账户，甚至可能还用于针对真实用户生成定制化的回复。

**这招还真有效**

其中一次行动大获成功。在 2024 年 1 月的四天时间里，Check Point 观察到 “观星者幽灵网络” 传播了 “阿特兰蒂达” 窃取器 —— 这是一种新型恶意软件家族，能够窃取用户凭证、加密货币钱包以及其他个人身份信息，并且成功导致了 1300 多起感染事件。

大约在同一时间，另一次行动启动，目的是通过表面上用于破解软件和加密货币交易工具的代码库来传播 “拉达曼迪斯” 恶意软件。研究人员称，根据他们在恶意软件所在的托管网站上找到的一个统计页面显示，在两周内有超过一千名用户下载了该恶意软件。

泰雷福斯认为，该团伙的一些行动甚至可能将目标对准了信息安全研究人员，或者是与之竞争的恶意软件团伙，因为那个网络钓鱼链接指向的是一个已知信息窃取软件 “RisePro” 的破解版本，而且这个版本已被修改，用于传播恶意软件。

不管目标是谁，事实证明这些行动利润丰厚：泰雷福斯认为，在过去一年里，这个恶意软件业务可能已经赚取了大约 10 万美元。

但这只是在 GitHub 平台上的情况 —— 研究人员怀疑该团伙可能也在其他网站上活动。有一个 GitHub 代码库链接到了一个 YouTube 教程，而这个教程所教的如何安装的程序实际上是恶意软件，这可能就表明了这一点。该研究还表明，“阿特兰蒂达” 恶意软件的传播行动针对的是对社交媒体感兴趣的用户，目的是获取其他平台上的账户，这些账户可以像 GitHub 账户一样被用于传播恶意软件。

GitHub 的一位发言人在向《登记簿》（The Register）发表的一份声明中表示，该平台 “…… 致力于调查所报告的安全问题。我们会根据 GitHub 的可接受使用政策禁用用户账户，该政策禁止发布直接支持非法主动攻击或正在造成技术危害的恶意软件活动的内容”。

本文翻译自theregister [原文链接](https://www.theregister.com/2024/07/26/github_stargazers_goblin_malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304345](/post/id/304345)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/07/26/github_stargazers_goblin_malware/)

如若转载,请注明出处： <https://www.theregister.com/2024/07/26/github_stargazers_goblin_malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**1赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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