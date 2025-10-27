---
title: Akira勒索软件利用SonicWall VPN账户发起急速入侵
url: https://www.anquanke.com/post/id/312438
source: 安全客-有思想的安全新媒体
date: 2025-09-30
fetch_date: 2025-10-02T12:03:38.547184
---

# Akira勒索软件利用SonicWall VPN账户发起急速入侵

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

# Akira勒索软件利用SonicWall VPN账户发起急速入侵

阅读量**45035**

发布时间 : 2025-09-29 18:03:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/akira-ransomware-exploits-sonicwall-vpn-accounts-with-lightning-fast-intrusions/#google_vignette>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

ctic Wolf观察到，自2025年7月下旬以来，**Akira勒索软件活动大幅增加**，攻击者正积极针对**SonicWall SSL VPN账户**。该活动目前仍在持续，截至2025年9月20日，已发现与其相关的新基础设施。

Akira附属团伙利用窃取的凭证进行攻击，**即使在启用多因素认证（MFA）的环境中也能得手**。报告指出：“威胁行为者通过可能已利用**CVE-2024-40766**漏洞窃取的凭证访问SSL VPN账户，包括启用了OTP MFA的账户。”

此次活动反映了Akira长期以来对VPN的关注。过去的攻击曾滥用Cisco ASA的**CVE-2023-20269**和Cisco AnyConnect的**CVE-2020-3259**等漏洞。

或许最令人担忧的是**极短的驻留时间**。Arctic Wolf警告：“在近期数十起入侵事件中，攻击者从获取凭证到横向移动、数据渗出再到加密，整个过程**不到4小时**——部分案例甚至仅需**55分钟**。”

这种加速的时间线使防御者在勒索软件触发前几乎没有检测和响应的空间。

为躲避检测，该团伙**持续更换基础设施**：“威胁行为者不断轮换基于VPS的客户端基础设施，试图逃避检测。”

入侵指标包括**来自VPS托管提供商的登录**（而非传统宽带或企业网络）——这一异常情况可供防御者监控。

受害者涵盖多个行业和公司规模，表明这是**大规模利用而非针对性入侵**。报告指出：“受害者跨越多个行业和组织规模，表明这是机会主义的大规模利用，而非针对性入侵。”

SonicWall已确认此次活动与**CVE-2024-40766**漏洞利用相关，并提醒：**即使已打补丁的设备，若凭证在更新前已被盗，仍可能面临风险**。公司建议：

1. **重置防火墙存储的所有凭证**，包括SSL VPN密码和OTP MFA密钥；
2. **更新至SonicOS 7.3.0版本**，该版本引入了暴力破解防护和MFA强化措施；
3. 删除未使用账户，并对所有远程访问**强制启用MFA**；
4. 启用僵尸网络防护和其他安全服务。

本文翻译自securityonline [原文链接](https://securityonline.info/akira-ransomware-exploits-sonicwall-vpn-accounts-with-lightning-fast-intrusions/#google_vignette)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312438](/post/id/312438)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/akira-ransomware-exploits-sonicwall-vpn-accounts-with-lightning-fast-intrusions/#google_vignette)

如若转载,请注明出处： <https://securityonline.info/akira-ransomware-exploits-sonicwall-vpn-accounts-with-lightning-fast-intrusions/#google_vignette>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53

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