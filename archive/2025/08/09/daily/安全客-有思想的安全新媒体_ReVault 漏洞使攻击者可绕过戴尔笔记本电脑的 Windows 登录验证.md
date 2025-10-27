---
title: ReVault 漏洞使攻击者可绕过戴尔笔记本电脑的 Windows 登录验证
url: https://www.anquanke.com/post/id/310944
source: 安全客-有思想的安全新媒体
date: 2025-08-09
fetch_date: 2025-10-07T00:17:38.655018
---

# ReVault 漏洞使攻击者可绕过戴尔笔记本电脑的 Windows 登录验证

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

# ReVault 漏洞使攻击者可绕过戴尔笔记本电脑的 Windows 登录验证

阅读量**70481**

发布时间 : 2025-08-08 17:03:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/revault-flaws-let-hackers-bypass-windows-login-on-dell-laptops/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

超过百款戴尔笔记本电脑型号受到 ControlVault3 固件漏洞影响，黑客可借此绕过 Windows 登录并植入在系统重装后依然存在的恶意软件。

**Dell ControlVault** 是一款基于硬件的安全解决方案，用于在专用子板（称为统一安全中心，Unified Security Hub，简称 USH）的固件中存储密码、生物识别数据和安全代码。

由思科 Talos 安全团队披露的这五个漏洞统称为 “**ReVault**”，影响范围包括 ControlVault3 固件本身以及其在 Windows 系统上的应用程序接口（API）。受影响产品主要为戴尔面向企业市场的 Latitude 和 Precision 系列笔记本电脑。

这些设备在网络安全、政府和工业环境中广泛使用，常见的身份验证手段还包括智能卡、指纹识别和近场通信（NFC）等。

ReVault 漏洞列表如下：

* **越界漏洞：CVE-2025-24311、CVE-2025-25050；**
* **任意释放漏洞：CVE-2025-25215；**
* **堆栈溢出漏洞：CVE-2025-24922；**
* **不安全反序列化漏洞：CVE-2025-24919（影响 ControlVault 的 Windows API）。**

这些漏洞可能被利用来获取系统权限、绕过认证流程，甚至实现持久化恶意控制，构成严重安全风险。

戴尔已于今年3月至5月期间发布安全更新，修复 ControlVault3 驱动和固件中的 ReVault 漏洞。受影响型号的完整列表可在戴尔的安全公告中查阅。

### 绕过 Windows 登录及权限提升

通过串联利用这些漏洞，攻击者可能在固件上**执行任意代码**，进而创建能够**在 Windows 重装后依然存在**的持久化恶意植入。

攻击者还可以利用物理接触权限，绕过 Windows 登录，或将本地用户权限提升至管理员级别。

思科 Talos 表示：“具有物理访问权限的本地攻击者可以撬开用户笔记本，使用定制连接器直接通过 USB 访问 USH 主板。”

“从此，之前描述的所有漏洞都在攻击者的攻击范围内，无需登录系统或知道全盘加密密码。”

成功利用漏洞还可能让攻击者**操控指纹认证**，使设备接受任何指纹，而不仅限于合法用户的指纹。

Talos 建议通过 Windows Update 或戴尔官网及时更新系统，禁用未使用的安全外设（如指纹识别器、智能卡读卡器和 NFC 读卡器），并在高风险环境中关闭指纹登录功能。

为缓解部分物理攻击，研究人员还建议在计算机 BIOS 设置中启用机箱入侵检测，以便及时发现物理篡改尝试；同时启用 Windows 的增强登录安全（ESS）功能，以检测异常的控制器固件。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/revault-flaws-let-hackers-bypass-windows-login-on-dell-laptops/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310944](/post/id/310944)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/revault-flaws-let-hackers-bypass-windows-login-on-dell-laptops/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/revault-flaws-let-hackers-bypass-windows-login-on-dell-laptops/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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