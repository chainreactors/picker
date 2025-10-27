---
title: HelloKitty 勒索软件重现，Windows、Linux 和 ESXi 环境安全告急
url: https://www.anquanke.com/post/id/306514
source: 安全客-有思想的安全新媒体
date: 2025-04-15
fetch_date: 2025-10-06T22:05:09.012498
---

# HelloKitty 勒索软件重现，Windows、Linux 和 ESXi 环境安全告急

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

# HelloKitty 勒索软件重现，Windows、Linux 和 ESXi 环境安全告急

阅读量**120858**

发布时间 : 2025-04-14 15:36:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hellokitty-ransomware-resurafced/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全专家检测到 HelloKitty 勒索软件出现了令人担忧的卷土重来之势，其新变种正同时积极瞄准 Windows、Linux 和 ESXi 环境。

HelloKitty 勒索软件最早于 2020 年 10 月被发现，它起源于 DeathRansom 勒索软件的一个分支，此后不断发展，扩大了其攻击目标范围，并完善了攻击技术。

自 2024 年 9 月以来，安全研究人员已识别出至少 11 个正在传播的 HelloKitty 新样本，这表明其活动出现了显著复苏。

经过改良的 HelloKitty 勒索软件保留了其核心功能，即加密受害者的文件，并在被加密的数据文件名后添加如 “CRYPTED”“CRYPT” 或 “KITTY” 等扩展名。

与许多会大肆展示自身品牌标识的勒索软件家族不同，HelloKitty 会定制勒索赎金通知，直接称呼受害者的名字，采用了一种更具个性化的敲诈方式。

该勒索软件使用 Visual C++ 编码，并经常利用 UPK 压缩工具来压缩可执行文件，增加了逆向工程的难度。

THE RAVEN FILE 的研究人员发现，最新的 HelloKitty 变种呈现出一种不寻常的地理传播模式。

根据他们为期一年的对 HelloKitty 样本的全面研究项目，该恶意软件在保留其独特加密方式的同时，进行了重大的技术改进。

这款勒索软件已持续多年活跃，有证据表明存在三个不同的活动批次：最初在 2020 年部署的版本，2020 年圣诞节期间的一批与 FiveHands 勒索软件有共同特征的版本，以及最新的、能力有所增强的 2024 年变种。

早期的攻击活动主要针对游戏公司、医疗保健服务机构和发电设施，而最新的攻击活动似乎将目标范围扩大到了更多行业。

尽管 HelloKitty 勒索软件曾有过一段时间处于休眠状态，但每次卷土重来时都会在技术上有所改进。

最近，安全分析师在 2025 年 2 月检测到了可能存在的新变种，这表明即便旧的命令与控制基础设施已从暗网消失，该勒索软件的开发仍在持续进行。

#### ****复杂的加密机制****

HelloKitty 的加密过程是其技术上最为先进的特征之一，它会根据目标环境采用不同的加密方法。

在 Windows 系统上，它结合使用 AES-128 和 NTRU 加密算法；而在 Linux 环境中，则采用 AES-256 加密算法搭配 ECDH 加密技术。

HelloKitty 的加密过程始于嵌入一个 RSA-2048 公钥，该公钥有双重用途：它会在经过 SHA256 哈希处理后成为受害者的标识符，出现在勒索赎金通知中，同时还用作每个文件对称密钥的加密密钥。

HelloKitty 会从 CPU 时间戳生成一个 32 字节的种子值，然后生成一个 Salsa20 密钥来加密第二个 32 字节的种子值。

这些值经过异或（XOR）运算，生成最终的 32 字节密钥，用于驱动 AES 文件加密。

// HelloKitty  密钥生成过程的简化表示

seed1 = GenerateFromCPUTimestamp(32);  // 基于32字节时间戳的种子值

seed2 = GenerateRandomBytes(32);       // 第二个32字节的种子值

salsa20\_key = DeriveSalsa20Key(seed1);

encrypted\_seed2 = Salsa20Encrypt(seed2, salsa20\_key);

final\_key = XOR(seed1, encrypted\_seed2);  // 最终的AES加密密钥

在加密每个文件后，HelloKitty 会附加元数据，包括原始文件大小、“DE C0 AD BA” 的魔数，以及 AES 密钥（用 RSA 公钥加密）。

加密过程的最后一步是在加密文件的末尾添加四个字节 “DA DC CC AB”，作为该勒索软件处理过的文件的签名。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hellokitty-ransomware-resurafced/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306514](/post/id/306514)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hellokitty-ransomware-resurafced/)

如若转载,请注明出处： <https://cybersecuritynews.com/hellokitty-ransomware-resurafced/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Gunra Ransomware集团声称从美国医院泄露了40 TB数据](/post/id/308534)

  2025-06-17 16:00:49
* ##### [新黑客组织利用 LockBit 勒索软件变种攻击俄罗斯公司](/post/id/308300)

  2025-06-10 13:29:14
* ##### [税务解决方案公司 Optima Tax Relief 遭勒索软件攻击，数据泄露](/post/id/308262)

  2025-06-09 17:29:27
* ##### [警惕！CatB 利用微软分布式事务协调器实施恶意攻击](/post/id/306484)

  2025-04-11 11:06:40
* ##### [开发人员警惕！勒索软件FreeFix投毒供应链 致软件生态安全告急](/post/id/305422)

  2025-03-26 10:09:24
* ##### [Medusa 勒索软件威胁：企业面临的持续挑战](/post/id/305035)

  2025-03-14 10:23:46
* ##### [勒索软件团伙在 Microsoft Teams 网络钓鱼攻击中冒充 IT 支持](/post/id/303779)

  2025-01-24 09:04:34

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