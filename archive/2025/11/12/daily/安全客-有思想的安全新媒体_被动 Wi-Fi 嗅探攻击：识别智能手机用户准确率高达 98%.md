---
title: 被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%
url: https://www.anquanke.com/post/id/313167
source: 安全客-有思想的安全新媒体
date: 2025-11-12
fetch_date: 2025-11-13T03:14:06.454538
---

# 被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%

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

# 被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%

阅读量**23668**

发布时间 : 2025-11-12 17:55:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Mann，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/passive-wi-fi-sniffing-attack-identifies-smartphone-users-with-98-accuracy/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为 **U-Print** 的新型攻击技术，通过捕获并分析**加密 Wi-Fi 流量**，能够在**被动监听**的情况下准确识别智能手机用户。

与以往依赖于应用识别或需要 IP 层访问的攻击不同，**U-Print 仅在无线 MAC 层上运行**，无需解密数据包或破解 MAC 地址随机化机制，就能推断出不仅是用户正在使用哪些应用，还包括**具体的应用内操作**，甚至**识别出使用者本人**。

![]()

## U-Print 威胁模型：通过 Wi-Fi 元数据进行行为画像

这项由中国研究人员提出的 U-Print 威胁模型假设：攻击者只需在目标环境（如办公室或家庭）**Wi-Fi 信号覆盖范围内**放置一个被动嗅探设备即可。整个过程**无需网络密码，也无需加入网络**。系统随后会根据个人的应用交互模式构建行为画像，从而推断出诸如**年龄、性别甚至心理状态**等隐私特征。

此前的相关攻击虽然能检测到应用的使用情况，但在 **MAC 地址随机化** 普及之后，仍无法可靠地识别出背后的具体用户。而 U-Print 的创新之处在于，它利用了用户在使用应用时的**独特行为模式**——例如偏好的应用类型、使用频率、操作习惯等，这些差异会在 **MAC 层元数据**（如数据包大小、时间间隔、上下行方向）中留下独特的“指纹”。

举例来说，两个用户都使用 WhatsApp，但一位主要进行文字聊天，另一位则偏爱语音消息——两者的流量特征便会有微妙差异。

![]()

## U-Print 的三大关键步骤

**1.流量预处理**：捕获 802.11 帧并筛选出数据帧，提取如到达时间、帧大小、方向（上行或下行）等元数据。

**2.应用与操作分类**：利用 **时序卷积网络（TCN）** 与 **OpenMax 扩展机制**，即使面对模型训练时未出现的新应用，也能实现“开放世界”分类，准确识别应用及其具体操作。

**3.用户画像与识别**：将流量转化为行为序列，运用聚类算法生成用户画像，并在未来的流量会话中识别出相同个体，即使其 MAC 地址已被随机化。

![]()

## 真实环境实验结果

研究人员在真实办公环境中进行了测试，使用一台联想笔记本和搭载 Kali Linux 的网卡被动捕获来自 **12 位智能手机用户、40 款移动应用**的 Wi-Fi 流量，结果令人震惊：

**1.应用识别准确率**：封闭环境下达 **98.7%**，开放环境下为 **87.6%**

**2.操作识别准确率**：封闭环境下达 **96.8%**，开放环境下为 **86.1%**

**3.用户识别准确率**：高达 **98.4%**，F1 分数为 **0.983**，即便在 MAC 地址随机化的情况下仍能准确识别个体

更令人关注的是，U-Print 的性能在多种现实条件下仍保持稳定：

**1.抗丢包能力强**：在 15% 数据包丢失情况下，性能几乎无明显下降

**2.抗背景噪声干扰**：即使多个应用同时产生流量，仍能准确识别用户行为

**3.环境迁移性强**：在三个不同办公场景中表现一致

![]()

## 研究意义与防御建议

虽然 U-Print 目前仍处于理论研究阶段，但该成果揭示了一个关键事实：**即便是使用 WPA3 加密和 MAC 地址随机化的现代 Wi-Fi 网络，也无法完全防御基于流量特征的身份推断攻击**。这表明，传统的加密与随机化机制在面对更高级的行为分析技术时，存在潜在的隐私泄露风险。

为防御类似 U-Print 的指纹识别攻击，研究人员建议可采取以下措施：

**1.流量混淆与扰动**：随机化数据包大小与时间间隔

**2.强化 MAC 地址随机化策略**

**3.引入行为信号混合**，在通信层面打乱特征一致性

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/passive-wi-fi-sniffing-attack-identifies-smartphone-users-with-98-accuracy/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313167](/post/id/313167)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/passive-wi-fi-sniffing-attack-identifies-smartphone-users-with-98-accuracy/)

如若转载,请注明出处： <https://cyberinsider.com/passive-wi-fi-sniffing-attack-identifies-smartphone-users-with-98-accuracy/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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
* **683**

* 粉丝
* **6**

### TA的文章

* ##### [一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证](/post/id/313153)

  2025-11-12 17:56:49
* ##### [Devolutions Server存在严重漏洞（CVE-2025-12485，CVSS 9.4），可通过预MFA Cookie劫持实现用户冒充](/post/id/313156)

  2025-11-12 17:56:29
* ##### [CMMC新规出台，国防供应链面临网络安全合规挑战](/post/id/313163)

  2025-11-12 17:56:08
* ##### [被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%](/post/id/313167)

  2025-11-12 17:55:43
* ##### [黑客入侵网站注入恶意链接，借机操纵搜索引擎优化](/post/id/313169)

  2025-11-12 17:55:21

### 相关文章

* ##### [一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证](/post/id/313153)

  2025-11-12 17:56:49
* ##### [Devolutions Server存在严重漏洞（CVE-2025-12485，CVSS 9.4），可通过预MFA Cookie劫持实现用户冒充](/post/id/313156)

  2025-11-12 17:56:29
* ##### [CMMC新规出台，国防供应链面临网络安全合规挑战](/post/id/313163)

  2025-11-12 17:56:08
* ##### [黑客入侵网站注入恶意链接，借机操纵搜索引擎优化](/post/id/313169)

  2025-11-12 17:55:21
* ##### [DragonForce勒索软件进化：利用BYOVD终结EDR并修复Conti V3加密缺陷](/post/id/313189)

  2025-11-12 17:55:04
* ##### [SuiteCRM中存在SQL注入漏洞（CVE-2025-64492与CVE-2025-64493），致客户数据面临泄露风险](/post/id/313150)

  2025-11-12 17:54:44
* ##### [Triofox零日漏洞（CVE-2025-12480）正遭积极利用：主机头验证绕过可导致未授权管理员接管](/post/id/313147)

  2025-11-12 17:54:22

### 热门推荐

文章目录

* [U-Print 威胁模型：通过 Wi-Fi 元数据进行行为画像](#h2-0)
* [U-Print 的三大关键步骤](#h2-1)
* [真实环境实验结果](#h2-2)
* [研究意义与防御建议](#h2-3)

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