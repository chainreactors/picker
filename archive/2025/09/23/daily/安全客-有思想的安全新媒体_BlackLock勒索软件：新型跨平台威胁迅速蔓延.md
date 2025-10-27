---
title: BlackLock勒索软件：新型跨平台威胁迅速蔓延
url: https://www.anquanke.com/post/id/312300
source: 安全客-有思想的安全新媒体
date: 2025-09-23
fetch_date: 2025-10-02T20:30:56.265402
---

# BlackLock勒索软件：新型跨平台威胁迅速蔓延

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

# BlackLock勒索软件：新型跨平台威胁迅速蔓延

阅读量**74549**

发布时间 : 2025-09-22 18:14:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/blacklock-ransomware-a-new-cross-platform-threat-spreading-rapidly/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安恒信息安全情报中心（ASEC）发布了对BlackLock勒索软件团伙的详细分析——这是一个相对较新的勒索软件组织，已在网络犯罪生态中迅速崛起。该团伙据信于2024年3月左右出现，2024年6月通过启动专用泄露站点（DLS）首次公开其活动。ASEC指出：“网站上已发布多家受影响公司的信息，表明该团伙已秘密活跃数月。”

该团伙最初以“El Dorado”为名活动，2024年9月左右更名为BlackLock。据ASEC分析：“BlackLock勒索软件使用跨平台编程语言Go开发，可攻击Windows、Linux和VMware ESXi环境，攻击面广泛，能够同时攻陷多种操作系统。”

已确认的受害者主要位于美国，涵盖企业和地方政府机构，但在韩国、日本等国家也出现攻击案例。受影响行业包括公共机构、咨询、教育科研、交通、制造，甚至高尔夫度假村等 hospitality 领域。

### **攻击特性：灵活执行与加密机制**

BlackLock设计注重**操作灵活性**，支持多种执行参数：

* `-path`：指定目标路径；
* `-perc`：设置文件块加密百分比；
* `-sort`：优先加密重要文件夹。

这些功能允许攻击者精确控制加密过程。ASEC强调：“执行时，BlackLock支持通过命令行参数启用或禁用特定功能。若不带任何选项启动，默认加密整个本地驱动器。”

文件加密方面，BlackLock使用Go的crypto库，为每个文件生成唯一的FileKey和Nonce，通过**XChaCha20流密码**加密数据。为保护解密密钥，团伙采用**椭圆曲线Diffie-Hellman（ECDH）算法**，确保只有攻击者能恢复共享密钥。

ASEC解释：“为确保支付赎金后文件可解密，BlackLock会将加密密钥和元数据附加到每个文件末尾……元数据随后通过secretbox.Seal()用共享密钥和Nonce加密。”

### **威胁升级：隐蔽删除备份与多平台风险**

受感染系统的每个受影响目录中都会显示名为**HOW\_RETURN\_YOUR\_DATA.TXT**的勒索信。ASEC指出：“若不支付赎金，攻击者威胁将破坏受害者的业务网站，或向客户和公众泄露敏感数据。”

![]()

与许多仅通过命令行指令操作的勒索软件家族不同，BlackLock以更隐蔽的方式删除备份：“它构造可执行WMI查询的COM对象实例，用于枚举和删除卷影副本。此过程由shellcode执行……增加了检测难度。”

尽管该团伙目前主要针对Windows和SMB网络共享，但恶意软件也可编译为Linux和VMware ESXi版本，对企业服务器和虚拟化环境均构成威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/blacklock-ransomware-a-new-cross-platform-threat-spreading-rapidly/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312300](/post/id/312300)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/blacklock-ransomware-a-new-cross-platform-threat-spreading-rapidly/)

如若转载,请注明出处： <https://securityonline.info/blacklock-ransomware-a-new-cross-platform-threat-spreading-rapidly/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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