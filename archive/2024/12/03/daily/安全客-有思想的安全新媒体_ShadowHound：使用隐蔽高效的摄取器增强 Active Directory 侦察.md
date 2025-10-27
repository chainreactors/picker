---
title: ShadowHound：使用隐蔽高效的摄取器增强 Active Directory 侦察
url: https://www.anquanke.com/post/id/302339
source: 安全客-有思想的安全新媒体
date: 2024-12-03
fetch_date: 2025-10-06T19:33:10.760550
---

# ShadowHound：使用隐蔽高效的摄取器增强 Active Directory 侦察

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

# ShadowHound：使用隐蔽高效的摄取器增强 Active Directory 侦察

阅读量**48385**

发布时间 : 2024-12-02 15:00:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/shadowhound-enhancing-active-directory-reconnaissance-with-a-stealthy-and-efficient-ingestor/>

译文仅供参考，具体内容表达以及含义原文为准。

![ShadowHound]()

**摘要**

在进攻性安全评估领域，最需要的是谨慎而有效的活动目录（AD）侦察。传统方法往往依赖于引入外部二进制文件，从而增加了被高级端点检测和响应（EDR）系统检测到的风险。ShadowHound 是一种解决方案，它利用本机 PowerShell 功能和合法工具获取用于 BloodHound 分析的 AD 数据，同时最大限度地减少其占用空间并躲避检测。

**简介**

BloodHound 是一种广泛采用的工具，用于可视化 AD 关系和识别潜在的攻击路径，它依赖于有关用户、组、计算机及其复杂连接的全面数据。从历史上看，这些数据都是通过 SharpHound 等工具收集的。然而，随着 EDR 解决方案的复杂性不断提高，有必要采用优先考虑隐蔽性的替代方法。

ShadowHound 利用 PowerShell 和合法 AD 工具的固有功能来收集必要的数据，从而解决了这一难题。这种方法避免了将可疑的外部二进制文件引入目标环境，从而大大降低了检测风险。

**方法论**

ShadowHound 提供两种不同的数据采集方法：

1. **活动目录 Web 服务 (ADWS)：** 该方法利用 Active Directory 模块中的 Get-ADObject cmdlet，通过 9389 端口通过 ADWS 与 AD 通信。这种方法充分利用了 PowerShell 和 AD 模块的内置功能，与环境完美融合。
2. **轻量级目录访问协议（LDAP）：** 这种方法利用 DirectorySearcher 类对 AD 域控制器执行直接 LDAP 查询。通过利用这一本地功能，ShadowHound 避免了对外部工具的依赖，最大限度地减少了占用空间并降低了触发警报的可能性。

**ShadowHound 的优势**

* **规避 EDR 检测：** 通过利用本机 PowerShell 和合法工具，ShadowHound 有效地减少了占用空间，避免了触发 EDR 解决方案的警报，这些解决方案通常会标记已知的恶意二进制文件。
* **大型域的可扩展性：** ShadowHound 在大型 AD 环境中表现出强大的性能，克服了可能阻碍 ADExplorer 等替代工具的连接难题。即使在复杂的网络拓扑结构中，也能确保高效可靠的数据收集。
* **规避身份防御者：** ShadowHound 采用了精心挑选的 LDAP 过滤器，如 (objectGuid=\*) 等，不易触发 Microsoft Defender for Identity 中的警报，该安全解决方案专门用于监控 AD 活动。
* **与 pyLdapSearch 集成：** ShadowHound 具有后处理脚本的功能，可将其输出转换为与 pyLdapSearch 兼容的格式，pyLdapSearch 是一款用于 LDAP 侦查的多功能工具。这种集成为安全专业人员提供了高级分析功能，而无需在目标系统上安装 Python。

**结论**

ShadowHound 是 AD 侦查领域的一大进步，它为 BloodHound 分析提供了一种隐蔽、高效的关键数据收集解决方案。通过利用本地 PowerShell 功能和精心设计的 LDAP 查询，ShadowHound 使安全专业人员能够进行全面评估，同时最大限度地降低检测风险。在现代环境中，规避先进的安全措施对成功的进攻性安全行动至关重要，因此该工具证明是非常有价值的。

本文翻译自securityonline [原文链接](https://securityonline.info/shadowhound-enhancing-active-directory-reconnaissance-with-a-stealthy-and-efficient-ingestor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302339](/post/id/302339)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/shadowhound-enhancing-active-directory-reconnaissance-with-a-stealthy-and-efficient-ingestor/)

如若转载,请注明出处： <https://securityonline.info/shadowhound-enhancing-active-directory-reconnaissance-with-a-stealthy-and-efficient-ingestor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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