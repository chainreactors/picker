---
title: 新型网络攻击滥用DeskSoft软件部署恶意软件，利用RDP访问执行命令
url: https://www.anquanke.com/post/id/312045
source: 安全客-有思想的安全新媒体
date: 2025-09-11
fetch_date: 2025-10-02T19:56:57.596372
---

# 新型网络攻击滥用DeskSoft软件部署恶意软件，利用RDP访问执行命令

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

# 新型网络攻击滥用DeskSoft软件部署恶意软件，利用RDP访问执行命令

阅读量**212501**

发布时间 : 2025-09-10 17:22:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-cyber-attack-weaponizes-desksoft/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种复杂的网络攻击通过恶意伪装DeskSoft公司的合法EarthTime应用程序，针对企业发起协同勒索软件攻击，部署多种恶意软件家族。

此次攻击标志着威胁行为者战术的危险演进，展示了合法软件如何被武器化以在企业网络中建立持久访问。

### **攻击链与技术细节**

入侵始于用户下载并执行看似DeskSoft正版EarthTime世界时钟工具的恶意程序。然而，该恶意可执行文件实际会部署**SectopRAT远程访问木马**，建立初始命令控制通道。

![]()

这种欺骗手段利用了用户对合法软件的信任，使其能有效绕过初始安全意识防护措施。

攻击展现出显著的技术复杂性：威胁行为者部署了包括**SystemBC代理隧道工具**和**Betruger后门**在内的多种恶意软件家族。

DFIR Report分析师发现其与三大勒索软件团伙（Play、RansomHub、DragonForce）存在关联，暗示存在跨团伙附属机构在多个勒索软件即服务（RaaS）平台上活动。

### **持久化与横向移动**

初始入侵后，攻击者通过**启动文件夹快捷方式**实现持久化，并创建本地管理员账户以维持访问权限。

![]()

恶意软件链包含**AdFind、SharpHound、SoftPerfect NetScan**等侦察工具，在横向移动前对目标环境进行全面测绘。

攻击的主要横向移动机制严重依赖**远程桌面协议（RDP）连接**，辅以Impacket的wmiexec工具。

通过结合这些技术，攻击者可穿越网络网段，同时借助SystemBC的代理功能维持操作安全，有效隐藏其真实网络来源。

**高级持久化与规避机制**

该恶意软件展现出复杂的防御规避技术，显著增加了检测与 remediation 难度。

初始的 EarthTime.exe 可执行文件通过**进程注入**攻陷合法 Windows 进程，专门针对**MSBuild.exe** 执行有效载荷。

此技术使恶意软件能在受信任的微软二进制文件上下文中运行，可能绕过依赖进程信誉的安全解决方案。

持久化机制通过**Windows 后台智能传输服务（BITS）** 实现多阶段操作。

恶意软件将自身迁移至 **C:\Users<USER>\AppData\Roaming\QuickAgent2\ChromeAlt\_dbg.exe** ，伪装成 Chrome 调试工具。

同时，它在 **C:\Users<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ChromeAlt\_dbg.lnk** 创建启动快捷方式，确保系统重启后仍能持续执行。

攻击中融入**时间戳操纵技术**，自动修改文件创建时间戳以干扰取证分析。

研究人员观察到 GT\_NET.exe 二进制文件将生成文件的时间戳设为 **2037 年**等未来日期，可能破坏事件响应中的时间线重建。

注册表修改针对 Windows Defender 核心功能，系统性禁用**实时扫描、行为监控和网络保护**特性。

这些修改通过 \**HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\** 策略级键值生效，确保影响覆盖整个系统，且在重启后持续存在并作用于所有用户账户。

恶意软件通过**元数据伪造**冒充合法安全产品，二进制文件包含伪造的版本信息，引用 **SentinelOne** 和 **Avast 杀毒软件**。

这种复杂的伪装技术旨在降低用户和自动化安全系统对恶意可执行文件的怀疑。

数据泄露通过**未加密的 FTP 连接**进行，使网络监控解决方案能捕获明文传输的凭证和传输细节，为调查类似攻击的事件响应团队提供有价值情报。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-cyber-attack-weaponizes-desksoft/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312045](/post/id/312045)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-cyber-attack-weaponizes-desksoft/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-cyber-attack-weaponizes-desksoft/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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