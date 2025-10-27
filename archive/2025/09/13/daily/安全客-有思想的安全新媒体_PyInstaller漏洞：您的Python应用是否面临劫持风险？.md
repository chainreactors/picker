---
title: PyInstaller漏洞：您的Python应用是否面临劫持风险？
url: https://www.anquanke.com/post/id/312071
source: 安全客-有思想的安全新媒体
date: 2025-09-13
fetch_date: 2025-10-02T20:04:21.580784
---

# PyInstaller漏洞：您的Python应用是否面临劫持风险？

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

# PyInstaller漏洞：您的Python应用是否面临劫持风险？

阅读量**74928**

发布时间 : 2025-09-12 17:36:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pyinstaller-flaw-are-your-python-apps-vulnerable-to-hijacking/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

PyInstaller项目已发布针对本地权限提升漏洞的修复程序，该漏洞影响使用6.0.0版本之前打包的应用。该漏洞编号为**CVE-2025-59042**，CVSS评分为**7.0**，攻击者可利用此漏洞在PyInstaller打包应用的引导过程中执行任意代码。

PyInstaller通过打包解释器和依赖项，将Python应用转换为独立可执行文件。然而，安全公告指出：“由于PyInstaller打包应用在引导过程中会向`sys.path` 添加特殊条目，且引导脚本会在该条目仍存在的情况下尝试加载可选的字节码解密模块，因此使用PyInstaller < 6.0.0版本构建的应用可能被非特权攻击者诱骗执行任意Python代码。”

该漏洞的成因是：如果满足特定条件，攻击者可在可执行文件旁创建伪造目录或ZIP归档，模仿PyInstaller引导程序传输PYZ归档位置的格式，导致引导脚本错误导入恶意模块。

若可执行文件以高权限运行（例如启用setuid位），则任意代码也将以高权限执行，从而实现**完全本地权限提升**。

### **攻击前提条件**

1. 应用使用**PyInstaller < 6.0.0**版本打包（单文件夹和单文件模式均受影响）。
2. **未启用**可选字节码加密功能。
3. 攻击者可在可执行文件**同一目录**创建文件/目录。
4. 文件系统允许文件名包含`?`（非Windows系统）。
5. 攻击者能够确定嵌入式PYZ归档的偏移量。

满足上述条件时，攻击者可诱骗引导过程导入恶意模块，而非预期的内部组件。

### **修复措施与缓解建议**

PyInstaller团队分两阶段修复了该问题：

1. **PyInstaller 6.0.0**：移除字节码加密支持，消除攻击向量（引导脚本不再尝试加载字节码解密模块）。
2. **PyInstaller 6.10.0**：进一步强化引导过程，不再使用`sys.path` 传输PYZ归档位置。

对于无法立即升级的环境，公告建议：

1. 对包含高权限可执行文件（如setuid二进制文件）的目录应用**严格权限控制**。
2. 确保攻击者无法在敏感可执行文件旁创建任意文件。

本文翻译自securityonline [原文链接](https://securityonline.info/pyinstaller-flaw-are-your-python-apps-vulnerable-to-hijacking/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312071](/post/id/312071)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pyinstaller-flaw-are-your-python-apps-vulnerable-to-hijacking/)

如若转载,请注明出处： <https://securityonline.info/pyinstaller-flaw-are-your-python-apps-vulnerable-to-hijacking/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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