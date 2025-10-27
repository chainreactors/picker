---
title: Salat Stealer通过复杂C2基础设施窃取浏览器凭证
url: https://www.anquanke.com/post/id/312036
source: 安全客-有思想的安全新媒体
date: 2025-09-11
fetch_date: 2025-10-02T19:56:56.889763
---

# Salat Stealer通过复杂C2基础设施窃取浏览器凭证

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

# Salat Stealer通过复杂C2基础设施窃取浏览器凭证

阅读量**213678**

发布时间 : 2025-09-10 17:23:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/salat-stealer-exfiltrates-browser-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Salat Stealer已成为针对Windows端点的主流威胁，专注于窃取**浏览器存储的凭证**和**加密货币钱包数据**。

该恶意软件于**2025年8月**首次被发现，基于Go语言开发，采用**UPX加壳**和**进程伪装**等多种规避技术，以绕过传统防御机制。

攻击者通过主流平台的**社会工程活动**传播恶意软件，推广伪造的**软件破解工具**和**游戏作弊器**，以此投放初始有效载荷。

执行后，Salat Stealer会静默注入可信目录，伪装成**Lightshot.exe** 、**Procmon.exe** 等合法进程名，以降低被察觉的风险。

Cyfirma研究人员在其出现后数天内便识别出该恶意软件的**多层攻击链**。

该威胁通过**注册表运行项**和**计划任务**实现持久化，创建如RuntimeBroker、Lightshot等名称的条目，在用户登录时执行，并**每三分钟重复运行一次**，持续较长时间。

恶意软件经**UPX 4.1.0**加壳处理，熵值高达**7.999**，在运行前掩盖其真实行为。

动态分析显示，子进程会在熟悉的文件路径下生成（例如**C:\Program Files (x86)\Windows NT\Lightshot.exe** ），增加端点防护软件的检测难度。

Cyfirma分析师指出，Salat Stealer与**命令控制（C2）基础设施**的通信既具备弹性又隐蔽。

初始接触时，恶意软件会向IP **104.21.80.1**发送约**45字节的轻量级UDP数据包**，可能用作保活信标。

同时，该窃取器会通过加密HTTPS通道连接**salat.cn/salat** ，DNS解析指向**172.67.194.254**和**104.21.60.88**。

当主域名无法访问时，内置的JavaScript例程会从**sniff\_domain\_list.txt** 中获取备用域名列表（如‘webrat.in ’‘webrat.top ’等），通过调用\*\*/alive.php\*\* 遍历每个域名，直至找到活跃面板进行重定向。

Salat Stealer的影响不止于简单的凭证窃取，它还会针对**MetaMask、Trust Wallet、Phantom**等加密货币钱包浏览器扩展。

![]()

通过扫描**Chrome扩展设置目录**，恶意软件可提取**助记词**和**私钥**，使用户面临不可逆的财务损失风险。

针对**Electrum、Exodus、Coinomi**等桌面钱包应用，该窃取器采用类似手段窃取钱包数据库和配置文件。

所有泄露的数据会先临时存储在**Temp文件夹**下的随机文件名中，随后再传输至**C2面板**。

## 感染与持久化机制

Salat Stealer的感染链始于社会工程学诱饵，诱骗受害者执行恶意压缩包。

程序启动后，可执行文件通过**UPX自解压**，并立即生成伪装成合法工具的子进程。

![]()

恶意软件通过**双重机制实现持久化**：注册表运行项和计划任务。

以下代码片段来自C2面板中的“Defender Excluder”脚本模块，展示了恶意软件如何加固其立足点：

```
if (Get-Command Add-MpPreference -ErrorAction SilentlyContinue) {
  $ProgramFilesX86 = [System.Environment]::GetFolderPath("ProgramFilesX86")
  Add-MpPreference -ExclusionPath $ProgramFilesX86
  $AppData = [System.Environment]::GetFolderPath("ApplicationData")
  Add-MpPreference -ExclusionPath $AppData
  $LocalAppData = [System.Environment]::GetFolderPath("LocalApplicationData")
  Add-MpPreference -ExclusionPath $LocalAppData
}
```

该脚本会**静默将关键目录添加至Windows Defender排除列表**，确保主有效载荷及其辅助工具均不被扫描。

![]()

同时，名为**Lightshot**和**RuntimeBroker**的计划任务条目被配置为在每次登录时及按计划间隔触发。

通过结合注册表与任务 scheduler 技术，Salat Stealer实现了长期访问与持续规避，凸显了现代**恶意软件即服务（MaaS）** 运营的日益复杂化。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/salat-stealer-exfiltrates-browser-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312036](/post/id/312036)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/salat-stealer-exfiltrates-browser-credentials/)

如若转载,请注明出处： <https://cybersecuritynews.com/salat-stealer-exfiltrates-browser-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [感染与持久化机制](#h2-0)

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