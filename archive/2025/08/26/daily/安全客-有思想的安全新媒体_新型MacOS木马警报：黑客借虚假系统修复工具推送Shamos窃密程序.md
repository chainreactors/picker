---
title: 新型MacOS木马警报：黑客借虚假系统修复工具推送Shamos窃密程序
url: https://www.anquanke.com/post/id/311456
source: 安全客-有思想的安全新媒体
date: 2025-08-26
fetch_date: 2025-10-07T00:18:03.142615
---

# 新型MacOS木马警报：黑客借虚假系统修复工具推送Shamos窃密程序

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

# 新型MacOS木马警报：黑客借虚假系统修复工具推送Shamos窃密程序

阅读量**45849**

发布时间 : 2025-08-25 17:49:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/fake-mac-fixes-trick-users-into-installing-new-shamos-infostealer/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

新型窃密恶意软件**Shamos**正针对Mac设备发起攻击，该恶意软件通过模仿故障排除指南和修复方案的**ClickFix攻击**传播。

这种名为\*\*“Shamos”\*\* 的新型恶意软件是**Atomic macOS窃密程序（AMOS）的变种**，由网络犯罪团伙\*\*“COOKIE SPIDER”\*\*开发，专门窃取：

1. **Web浏览器存储的数据和凭证**
2. **Keychain密钥库项目**
3. **Apple Notes内容**
4. **加密货币钱包数据**

发现该恶意软件的**CrowdStrike**报告称，自2025年6月以来，在其监控的全球范围内已有**超过三百个环境**遭受感染尝试。

### **通过ClickFix攻击传播**

受害者通过**恶意广告**或**虚假GitHub仓库**被诱导，这些渠道利用**ClickFix攻击**诱使用户在**macOS终端执行shell命令**。

攻击者诱骗用户运行这些命令来安装软件或修复虚假错误，但实际执行时会在设备上**下载并运行恶意软件**。

![]()

恶意广告或伪造页面（**mac-safer[.]com**, **rescue-mac[.]com**）声称提供用户可能搜索的macOS问题解决方案，其中包含指示用户**复制粘贴命令**以修复问题的说明。

![]()

这些命令不仅无法修复任何问题，反而会**解码Base64编码的URL**，从远程服务器获取**恶意Bash脚本**。

![]()

该脚本执行以下操作：

1. **捕获用户密码**
2. **下载Shamos的Mach-O可执行文件**
3. 使用以下命令准备并执行恶意软件：**`xattr`**（移除隔离标志），**`chmod`**（赋予二进制文件执行权限）
   以此绕过**Gatekeeper防护机制**。

新型macOS恶意软件Shamos正通过精密攻击链对苹果用户构成严重威胁。一旦在设备上执行，该恶意软件会率先执行**反虚拟机检测命令**以确认未在沙箱环境中运行，随后通过AppleScript命令进行主机侦察和数据收集。

Shamos在设备上搜索多种敏感数据，包括：

1. 加密货币钱包文件
2. 密钥链数据
3. Apple Notes笔记数据
4. 浏览器存储的敏感信息

完成收集后，所有数据被打包命名为`out.zip`的压缩文件，并通过curl工具传输给攻击者。当恶意软件以sudo权限运行时，还会创建Plist文件（`com.finder.helper.plist`）并将其存储在用户的LaunchDaemons目录中，确保在系统启动时自动执行实现持久化。

CrowdStrike进一步指出，Shamos可将额外载荷下载至受害者主目录。研究人员已观察到威胁分子投递伪造Ledger Live钱包应用和僵尸网络模块的案例。

安全专家强烈建议macOS用户：

1. **切勿在线执行来源不明的命令**
2. **审慎对待GitHub存储库**（该平台存在大量针对不知情用户的恶意项目）
3. **避免点击赞助商搜索结果**，应通过Apple社区论坛或系统内置帮助（Cmd+空格键→”帮助”）寻求支持

值得注意的是，ClickFix攻击已成为恶意软件分发的流行策略，威胁分子通过TikTok视频、伪装验证码或虚假Google Meet错误修复等方式实施攻击。该策略在部署恶意软件方面效果显著，已被用于勒索软件攻击甚至国家资助的黑客活动中。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/fake-mac-fixes-trick-users-into-installing-new-shamos-infostealer/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311456](/post/id/311456)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/fake-mac-fixes-trick-users-into-installing-new-shamos-infostealer/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/fake-mac-fixes-trick-users-into-installing-new-shamos-infostealer/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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