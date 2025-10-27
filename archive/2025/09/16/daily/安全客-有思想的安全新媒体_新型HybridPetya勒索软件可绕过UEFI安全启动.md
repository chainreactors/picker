---
title: 新型HybridPetya勒索软件可绕过UEFI安全启动
url: https://www.anquanke.com/post/id/312163
source: 安全客-有思想的安全新媒体
date: 2025-09-16
fetch_date: 2025-10-02T20:11:19.336124
---

# 新型HybridPetya勒索软件可绕过UEFI安全启动

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

# 新型HybridPetya勒索软件可绕过UEFI安全启动

阅读量**45927**

发布时间 : 2025-09-15 18:20:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-hybridpetya-ransomware-can-bypass-uefi-secure-boot/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期发现的名为HybridPetya的勒索软件变种能够绕过UEFI安全启动功能，在EFI系统分区安装恶意应用程序。

HybridPetya的设计灵感似乎源自具有破坏性的Petya/NotPetya恶意软件——后者曾在2016年和2017年的攻击中加密计算机并阻止Windows启动，且未提供恢复选项。

网络安全公司ESET的研究人员在VirusTotal上发现了HybridPetya样本，指出其可能是一个研究项目、概念验证，或是仍在有限测试阶段的网络犯罪工具早期版本。尽管如此，ESET表示，该样本的出现与BlackLotus、BootKitty、Hyper-V Backdoor等案例一样，证明**具备安全启动绕过功能的UEFI bootkit是真实存在的威胁**。

HybridPetya融合了Petya和NotPetya的特征，包括这些早期恶意软件的视觉风格和攻击链。然而，开发者增加了新功能，例如**安装至EFI系统分区**，以及通过利用**CVE-2024-7344漏洞**实现绕过安全启动的能力。ESET于今年1月发现该漏洞，其问题在于**微软签名的应用程序可能被滥用于部署bootkit，即使目标设备已启用安全启动保护**。

![]()

启动后，HybridPetya会检测主机是否使用**UEFI与GPT分区**，并向**EFI系统分区**投放包含多个文件的**恶意bootkit**。这些文件包括配置与验证文件、修改后的引导加载程序、备用UEFI引导加载程序、漏洞利用载荷载体，以及跟踪加密进度的状态文件。

ESET列出了所分析的HybridPetya变种中使用的文件：

1. \EFI\Microsoft\Boot\config（**加密标识+密钥+随机数+受害者ID**）
2. \EFI\Microsoft\Boot\verify（用于验证**解密密钥正确性**）
3. \EFI\Microsoft\Boot\counter（**加密簇进度追踪器**）
4. \EFI\Microsoft\Boot\bootmgfw.efi.old （**原始引导加载程序备份**）
5. \EFI\Microsoft\Boot\cloak.dat （在绕过安全启动的变种中保存**XOR混淆的bootkit**）

此外，恶意软件会用存在漏洞的“**reloader.efi** ”替换\EFI\Microsoft\Boot\bootmgfw.efi ，并删除\EFI\Boot\bootx64.efi 。原始Windows引导加载程序会被保存，以便在受害者**支付赎金**后恢复系统时激活。

部署完成后，HybridPetya会像早期Petya一样触发**蓝屏死机（BSOD）** 并显示虚假错误，强制系统重启，使恶意bootkit在启动时执行。此时，勒索软件会利用从config文件中提取的**Salsa20密钥和随机数**加密所有**MFT簇**，同时显示类似NotPetya的**伪造CHKDSK界面**。加密完成后，系统再次重启，启动时显示勒索信，要求支付**1000美元比特币赎金**。作为交换，受害者会获得一个**32字符密钥**，可在勒索信界面输入以恢复原始引导加载程序、解密簇并提示重启。

尽管目前尚未发现HybridPetya在真实攻击中使用，但类似的概念验证项目可能随时被**武器化**，针对**未打补丁的Windows系统**发起大规模攻击。相关入侵指标已在GitHub仓库发布，供防御使用。微软已在2025年1月的“补丁星期二”中修复**CVE-2024-7344漏洞**，安装该更新或更高版本安全补丁的Windows系统可免受HybridPetya攻击。防范勒索软件的另一有效措施是对重要数据进行**离线备份**，以便自由且轻松地恢复系统。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-hybridpetya-ransomware-can-bypass-uefi-secure-boot/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312163](/post/id/312163)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-hybridpetya-ransomware-can-bypass-uefi-secure-boot/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-hybridpetya-ransomware-can-bypass-uefi-secure-boot/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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