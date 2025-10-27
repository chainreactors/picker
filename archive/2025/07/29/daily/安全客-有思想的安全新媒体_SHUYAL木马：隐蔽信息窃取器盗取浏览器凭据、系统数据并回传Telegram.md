---
title: SHUYAL木马：隐蔽信息窃取器盗取浏览器凭据、系统数据并回传Telegram
url: https://www.anquanke.com/post/id/310643
source: 安全客-有思想的安全新媒体
date: 2025-07-29
fetch_date: 2025-10-06T23:50:17.883864
---

# SHUYAL木马：隐蔽信息窃取器盗取浏览器凭据、系统数据并回传Telegram

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

# SHUYAL木马：隐蔽信息窃取器盗取浏览器凭据、系统数据并回传Telegram

阅读量**77132**

发布时间 : 2025-07-28 16:40:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/shuyal-new-stealthy-infostealer-plunders-browser-credentials-system-data-screenshots-to-telegram/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在一次深入的技术调查中，Hybrid Analysis揭露了一种强大的新型信息窃取者——SHUYAL，这是一个之前未曾记录过的恶意软件家族，结合了广泛的凭证收集、系统侦察和隐蔽的外泄行为。

通过SHUYAL，网络犯罪分子获得了一款可以利用被窃取的浏览器凭证、系统元数据、截图甚至剪贴板内容的工具——所有这些数据都通过Telegram进行外泄，从而避开了传统的检测机制。

SHUYAL以其PDB路径中的唯一标识符命名，是一种凭证窃取者，具备间谍软件级别的行为。Hybrid Analysis的研究人员发现该窃取者针对19种浏览器，包括Chrome、Edge和Firefox等主流浏览器，以及Tor和Falkon等隐私浏览器。

“该窃取者尝试访问包括Google Chrome、Opera和Microsoft Edge在内的浏览器中的登录凭证，”分析中提到。

在启动其核心数据窃取操作之前，SHUYAL会执行一系列侦察行为：

1. **通过`wmic diskdrive`获取磁盘驱动器的序列号和型号**
2. **通过`Win32_Keyboard`和`Win32_PointingDevice`获取键盘和鼠标的详细信息**
3. **获取显示器配置和壁纸路径**
4. **通过`OpenClipboard`和`GetClipboardData`获取剪贴板内容**

“SHUYAL会生成多个进程…它检索可用磁盘驱动器的型号和序列号，键盘和鼠标信息…以及显示器的详细信息，”分析解释道。

为了维持持久性并避免检测：

1. SHUYAL通过修改注册表中的`DisableTaskMgr`来禁用Windows任务管理器。
2. 它终止任务管理器进程，并通过`SHGetSpecialFolderPathA`在启动文件夹中创建一个隐蔽的副本。
3. 它通过批处理文件（`util.bat`）在载荷完成后自我删除。
4. “该恶意软件非常隐蔽，因为它会删除浏览器数据库中新创建的文件，以及之前被外泄的‘runtime’目录中的所有文件，”分析中提到。

SHUYAL瞄准了广泛的基于Chromium的浏览器及其他浏览器。它定位并复制它们的“Login Data”文件，并使用DPAPI解密存储的密码。解密后的凭证存储在`saved_passwords.txt`中，浏览器历史记录则记录在`history.txt`中。

“解密通过从‘Local State’文件中提取主密钥来工作…然后使用DPAPI的`CryptUnprotectData`进行解密。”

除了密码，SHUYAL还窃取了：

* **来自常规、Canary和PTB版本的Discord令牌**
* **剪贴板内容，保存为`clipboard.txt`**
* **截图，保存为`ss.png`**

在将窃取的数据汇总到运行时目录后，SHUYAL使用PowerShell将该目录压缩为`runtime.zip`档案。然后，它通过Telegram机器人外泄该档案，绕过传统的C2检测机制。

最后，SHUYAL擦除其痕迹。它创建并运行一个批处理文件，删除恶意软件及所有相关数据，几乎不留下任何取证证据。

本文翻译自securityonline [原文链接](https://securityonline.info/shuyal-new-stealthy-infostealer-plunders-browser-credentials-system-data-screenshots-to-telegram/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310643](/post/id/310643)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/shuyal-new-stealthy-infostealer-plunders-browser-credentials-system-data-screenshots-to-telegram/)

如若转载,请注明出处： <https://securityonline.info/shuyal-new-stealthy-infostealer-plunders-browser-credentials-system-data-screenshots-to-telegram/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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