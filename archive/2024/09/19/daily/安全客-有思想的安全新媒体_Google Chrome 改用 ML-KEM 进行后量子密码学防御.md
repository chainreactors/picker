---
title: Google Chrome 改用 ML-KEM 进行后量子密码学防御
url: https://www.anquanke.com/post/id/300158
source: 安全客-有思想的安全新媒体
date: 2024-09-19
fetch_date: 2025-10-06T18:24:13.694939
---

# Google Chrome 改用 ML-KEM 进行后量子密码学防御

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

# Google Chrome 改用 ML-KEM 进行后量子密码学防御

阅读量**130708**

发布时间 : 2024-09-18 15:00:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html>

译文仅供参考，具体内容表达以及含义原文为准。

Google 宣布将在其 Chrome 网络浏览器中从 KYBER 切换到 ML-KEM，作为其持续努力的一部分，以抵御加密相关量子计算机 （CRQC） 带来的风险。

“Chrome 将为混合 ML-KEM（代码点 0x11EC）提供关键份额预测，”Chrome 团队的 David Adrian、David Benjamin、Bob Beck 和 Devon O’Brien 说。“PostQuantumKeyAgreementEnabled 标志和企业策略将适用于 Kyber 和 ML-KEM。”

这些更改预计将在 Chrome 版本 131 中生效，该版本有望于 2024 年 11 月初发布。谷歌指出，这两种混合后量子密钥交换方法本质上彼此不兼容，促使它放弃了 KYBER。

“对 ML-KEM 最终版本的更改使其与之前部署的 Kyber 版本不兼容，”该公司表示。“因此，TLS 中用于混合后量子密钥交换的码位从 Kyber768+X25519 的 0x6399 更改为 ML-KEM768+X25519 的 0x11EC。”

在美国国家标准与技术研究院 （NIST） 发布三种新加密算法的最终版本后不久，该开发过程使用量子技术保护当前系统免受未来攻击，标志着该机构八年努力的高潮。

有问题的算法是 FIPS 203（又名 ML-KEM）、FIPS 204（又名 CRYSTALS-Dilithium 或 ML-DSA）和 FIPS 205（又名 Sphincs+ 或 SLH-DSA）用于一般加密和保护数字签名。第四种算法 FN-DSA（最初称为 FALCON）计划于今年晚些时候完成。

ML-KEM 是 Module-Lattice-based Key-Encapsulation Mechanism 的缩写，源自 CRYSTALS-KYBER KEM 的第三轮版本，可用于在通过公共通道通信的两方之间建立共享密钥。

就 Microsoft 而言，它也通过宣布更新其 SymCrypt 加密库，支持 ML-KEM 和扩展默克尔签名方案 （XMSS），为后量子世界做好准备。

“向底层加密引擎添加后量子算法支持是迈向量子安全世界的第一步，”这家 Windows 制造商表示，并表示向后量子密码学 （PQC） 的过渡是一个“复杂的、多年的迭代过程”，需要仔细规划。

在英飞凌 SLE78、Optiga Trust M 和 Optiga TPM 安全微控制器中发现一个加密缺陷后，该漏洞可能允许从 YubiKey 硬件身份验证设备中提取椭圆曲线数字签名算法 （ECDSA） 私钥。

据信，Infineon 提供的库中的加密漏洞已经 14 年没有被注意到，并且经过了大约 80 次最高级别的通用标准认证评估。

NinjaLab 的 Thomas Roche 将侧信道攻击称为 **EUCLEAK**（CVE-2024-45678，CVSS 评分：4.9），它影响了所有嵌入加密库的 Infineon 安全微控制器和以下 YubiKey 设备 –

* YubiKey 5 系列5.7 之前的版本
* YubiKey 5 FIPS 系列，低于 5.7
* YubiKey 5 CSPN 系列，低于 5.7
* YubiKey Bio Series 5.7.2 之前的版本
* 安全密钥系列 5.7 之前的所有版本
* YubiHSM 2 2.4.0 之前的版本
* YubiHSM 2 FIPS 2.4.0 之前的版本

“攻击者需要实际拥有 YubiKey、安全密钥或 YubiHSM，了解他们想要针对的帐户，以及执行必要攻击的专用设备，”YubiKey 背后的公司 Yubico 在一份协调咨询中表示。

“根据用例，攻击者可能还需要其他知识，包括用户名、PIN、帐户密码或 [YubiHSM] 身份验证密钥。”

但是，由于具有易受攻击固件版本的现有 YubiKey 设备无法更新（这是一种有意的设计选择，旨在最大限度地提高安全性并避免引入新漏洞），因此它们永远容易受到 EUCLEAK 的影响。

此后，该公司宣布计划弃用对 Infineon 加密库的支持，转而将自己的加密库作为固件版本 YubiKey f5.7 和 YubiHSM 2.4 的一部分。

Roche 和 Victor Lomne 在 2021 年演示了针对 Google Titan 安全密钥的类似侧信道攻击，可能允许恶意行为者通过利用嵌入其中的芯片中的电磁侧信道来克隆设备。

“[EUCLEAK] 攻击需要对安全元件进行物理访问（很少的本地电磁侧信道采集，即几分钟就足够了）才能提取 ECDSA 密钥，”Roche 说。“在 FIDO 协议的情况下，这允许创建 FIDO 设备的克隆。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300158](/post/id/300158)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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