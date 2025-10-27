---
title: 从 UnitedHealth 勒索软件攻击中吸取的五个备份教训
url: https://www.anquanke.com/post/id/302030
source: 安全客-有思想的安全新媒体
date: 2024-11-21
fetch_date: 2025-10-06T19:13:56.321960
---

# 从 UnitedHealth 勒索软件攻击中吸取的五个备份教训

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

# 从 UnitedHealth 勒索软件攻击中吸取的五个备份教训

阅读量**44727**

发布时间 : 2024-11-20 14:47:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Gil Hecht，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/11/20/backup-strategies/>

译文仅供参考，具体内容表达以及含义原文为准。

今年早些时候发生的针对 UnitedHealth 的勒索软件攻击正迅速成为医疗保健行业的 “殖民地管道”，引发国会作证、立法者审查和潜在立法。

在过去的几个月里，国会就此次攻击举行了两次听证会–一次在参议院，另一次在众议院–多位参议员呼吁调查政府如何应对此次事件，更不用说对联合健康的首席信息安全官史蒂文-马丁（Steven Martin）的批评了，他于 2023 年 6 月加入该公司。

在支付了 2200 万美元的赎金以防止被盗数据泄露后，联合健康不得不对系统进行全面重建，甚至在解密文件后也是如此

联合健康首席执行官安德鲁-威蒂（Andrew Witty）在证词中指出，该公司的备份没有通过网络分段或基础架构间隙进行隔离，因此攻击者也能够锁定这些备份，从而阻断了最初攻击的恢复路径。

**备份： 网络犯罪分子最有利可图的目标**

过去，很少有 CISO 会关注他们的备份。如今情况已不再如此。

勒索软件已将备份和恢复重新提上了 IT 和企业的议事日程，甚至在今年早些时候联合健康保险公司（UnitedHealth）遭受攻击之前也是如此。

攻击者意识到，成功入侵备份环境是企业是否支付赎金的最大决定因素。

一些勒索软件集团–例如 BlackCat、Akira、Lockbit、Phobos 和 Crypto–已经完全绕过了生产系统，直接攻击备份。

这迫使企业重新审视其安全网中的潜在漏洞，重新审视其备份和恢复策略。

![backup strategies]()

**那么，IT 基础设施和安全团队应该如何应对这种威胁呢？**

**确保备份安全的 5 个技巧**

**1. 网络分段和气隙备份**

在联合健康保险公司（UnitedHealth）遭受的勒索软件攻击中，该公司承认他们的备份没有通过网络分段或基础架构间隙进行隔离，因此攻击者能够锁定这些备份，阻断初始攻击的任何恢复路径。

网络分段是一种可以大大降低勒索软件攻击影响的策略。通过将网络分割成更小的、不同的区域，即使一个区域受到攻击，恶意软件的传播也会降到最低。

**2. 多因素身份验证（MFA）**

缺乏 MFA 是 UnitedHealth 勒索软件攻击的核心。

这次攻击是由黑客精心策划的，他们利用窃取的凭证潜入了公司缺乏 MFA 的系统。

StorageGuard 等解决方案可以审核和验证 MFA 是否在所有备份系统中实施和执行。通过确保始终如一地应用 MFA，有助于保护敏感数据免遭未经授权的访问–即使用户凭据已经泄露。

**3. 限制管理访问**

限制管理权限是可靠的备份安全策略的重要组成部分，因为这些权限可能成为攻击者的主要目标。 这包括

* 确保只有真正需要的人才能对组织的备份进行管理访问
* 将 IP ACL 应用于管理界面
* 为关键备份更改设置双人规则

这些建议可大大有助于减少攻击面。

**4. 不可变备份**

确保至少有一个备份副本存储在不可变存储上。这将确保您的备份数据不会被恶意行为者（包括勒索软件）更改、删除或加密。它还能保证网络恢复时备份数据的完整性和可用性。

5. 安全配置基线

正如 DORA 最近和 NIST 之前规定的那样，为备份和存储环境建立安全配置基线并使用工具检测基线偏差至关重要。这将确保您的备份设备遵守本建议部分提出的原则，以及更多原则。

其中一项建议是对备份系统的安全性进行定期审核，以验证备份平台是否经过加固，并防止篡改和未经授权的访问。

审计应包括

* 多因素身份验证
* 不可变性最佳实践
* CISA #StopRansomware 指南
* 关键变更的双重授权
* 限制管理访问
* 登录最佳实践
* 账户锁定设置
* 备份隔离
* NAS 安全指南
  安全快照
* 加密
* 遵守 NIST、ISO、NERC CIP、HIPAA 和其他标准
* 还有更多…

实施这些策略并利用安全态势管理工具，可确保备份系统保持安全、可靠，并能抵御不断变化的网络威胁。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/11/20/backup-strategies/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302030](/post/id/302030)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/11/20/backup-strategies/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/11/20/backup-strategies/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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