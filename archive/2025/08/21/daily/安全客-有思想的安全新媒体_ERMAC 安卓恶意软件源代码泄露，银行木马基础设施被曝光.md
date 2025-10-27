---
title: ERMAC 安卓恶意软件源代码泄露，银行木马基础设施被曝光
url: https://www.anquanke.com/post/id/311372
source: 安全客-有思想的安全新媒体
date: 2025-08-21
fetch_date: 2025-10-07T00:47:41.926378
---

# ERMAC 安卓恶意软件源代码泄露，银行木马基础设施被曝光

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

# ERMAC 安卓恶意软件源代码泄露，银行木马基础设施被曝光

阅读量**58918**

发布时间 : 2025-08-20 17:51:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/ermac-android-malware-source-code-leak-exposes-banking-trojan-infrastructure/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

ERMAC 安卓银行木马第 3 版源代码已在网上泄露，暴露了这一恶意软件即服务（MaaS）平台的内部机制及其运营者的基础设施。

研究人员在 2024 年 3 月进行资源暴露扫描时，通过 Hunt.io 在一个公开目录中发现了这份代码库。

### **Ermac 3.0.zip** 的压缩包

他们找到一个名为 **Ermac 3.0.zip** 的压缩包，其中包含该木马的完整代码，包括后端、前端（控制面板）、数据窃取服务器、部署配置，以及木马的生成器和混淆器。

研究人员对代码进行分析后发现，与之前的版本相比，该木马的攻击目标范围显著扩大，能够针对 **700 多款银行、购物和加密货币应用程序**。

![]()

ERMAC 最早于 **2021 年 9 月** 由在线支付防诈骗解决方案及金融情报提供商 **ThreatFabric** 披露，被认为是源自 **Cerberus 银行木马** 的变种，由名为“**BlackRock**”的威胁行为者操控。其 **2.0 版本** 于 **2022 年 5 月** 被 **ESET** 发现，以每月 **5000 美元**的租赁价格向网络犯罪分子提供，当时的攻击目标由前一版本的 378 款应用扩大至 **467 款**。

**2023 年 1 月**，ThreatFabric 观察到 BlackRock 推广一款名为 **Hook** 的新型安卓恶意软件工具，被认为是 ERMAC 的进一步演变。

Hunt.io 在分析过程中发现并研究了 **ERMAC v3.0** 的完整组件，包括基于 PHP 的 **命令与控制（C2）后端**、React 构建的 **前端控制面板**、基于 Go 的 **数据窃取服务器**、Kotlin 编写的 **后门程序**，以及用于生成定制化木马 APK 的 **构建面板**。

研究人员表示，**ERMAC v3.0** 的攻击目标已扩展至 **700 多款应用中的敏感用户信息**。此外，该版本在此前记录的表单注入技术基础上进一步扩展，采用 **AES-CBC** 加密通信，全面改造了操控面板，并在数据窃取与设备控制功能方面进行了强化。

具体而言，Hunt.io 记录了 **ERMAC v3.0** 的以下主要功能：

**·** 窃取 **短信、联系人及已注册账户信息；**

**·** 提取 **Gmail 邮件主题与正文内容；**

**·** 通过 “list” 和 “download” 命令实现 **文件访问；**

**·** 发送短信与 **呼叫转发**，用于滥用通信功能；

**·** 调用前置摄像头进行 **拍照；**

**·** 完整的应用管理能力（启动、卸载、清除缓存）；

**·** 显示 **伪造推送通知** 用于欺骗用户；

**·** 支持远程卸载（“killme” 指令），以实现逃避检测。

### **基础设施暴露**

Hunt.io 分析人员通过 **SQL 查询** 识别出仍在被威胁行为者使用的暴露型基础设施，包括 **C2 端点、控制面板、数据窃取服务器和木马构建部署**。

![]()

除了恶意软件源代码被泄露之外，ERMAC 的操作者还存在多项严重的 **运维安全（OpSec）失误**，例如：硬编码的 **JWT 令牌**、默认的 **root 凭证**，以及管理面板缺乏注册保护机制，导致任何人都可以访问、操纵甚至破坏 ERMAC 的控制面板。

此外，面板名称、页面标题、软件包名称以及其他多种操作特征指纹，几乎毫无疑问地指向了其归属，并大大降低了发现与映射该基础设施的难度。

![]()

ERMAC v3.0 源代码的泄露削弱了该木马的整体运营，首先在于削弱了购买者对其 **恶意软件即服务（MaaS）平台**的信任，怀疑其无法有效保护客户免受执法机构追踪，或无法在低检测风险下安全运行攻击活动。

同时，**威胁检测解决方案**也有望更容易识别 ERMAC。然而，如果源代码落入其他威胁行为者之手，未来可能会出现经过修改的 **变种版本**，其隐蔽性和抗检测能力将更为增强。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/ermac-android-malware-source-code-leak-exposes-banking-trojan-infrastructure/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311372](/post/id/311372)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/ermac-android-malware-source-code-leak-exposes-banking-trojan-infrastructure/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/ermac-android-malware-source-code-leak-exposes-banking-trojan-infrastructure/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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