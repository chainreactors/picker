---
title: 0bj3ctivityStealer：隐秘信息窃取木马利用图像隐写术与 PowerShell 规避检测
url: https://www.anquanke.com/post/id/310679
source: 安全客-有思想的安全新媒体
date: 2025-07-31
fetch_date: 2025-10-06T23:16:34.653154
---

# 0bj3ctivityStealer：隐秘信息窃取木马利用图像隐写术与 PowerShell 规避检测

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

# 0bj3ctivityStealer：隐秘信息窃取木马利用图像隐写术与 PowerShell 规避检测

阅读量**81852**

发布时间 : 2025-07-30 17:09:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/0bj3ctivitystealer-stealthy-info-stealer-uses-steganography-powershell-to-evade-detection/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**Trellix 高级研究中心（ARC**）近期发布的一项分析披露了一款高度隐蔽的信息窃取恶意软件 **0bj3ctivityStealer**。该恶意软件通过精心设计的钓鱼攻击、自定义 PowerShell 加载器以及图像隐写术，实现了绕过安全检测并从多种应用中窃取用户敏感数据的目的，展现出极强的隐蔽性与复杂性。

## 攻击链条：从伪装订单到多层次载荷投递

攻击最初通过一封主题为**“报价单”**的钓鱼邮件展开，附件中包含一张模糊的伪订单图片，诱导受害者点击“下载”链接获取高清版本。该链接指向文件分享平台 MediaFire，下载的则是一个经过严重混淆的 JavaScript 文件，作为第一阶段的恶意载荷。

![]()

*恶意钓鱼邮件 | 图片来源：Trellix*

“该 JavaScript 文件总计超过 3000 行代码，真正起作用的代码**仅有约 60 行**，其余部分均为混淆内容，目的是隐藏真正的 PowerShell 载荷。”报告指出。

随后，脚本会通过 PowerShell 下载一张看似普通的 JPG 图片（托管于 Archive.org），但这张图片中却隐藏着下一阶段的有效载荷——一个 .NET DLL 加载器。攻击者采用了**图像隐写术**，将代码藏匿在像素数据中。

“脚本会逐像素读取 RGB 值，提取并还原出包含有效载荷和干扰数据的缓冲区。”报告进一步解释道。

## 反分析与规避机制

虽然核心代码本身没有采用极端混淆手段，但 **0bj3ctivityStealer** 运用了多种防分析技术，增加逆向工程的难度：

**· 基于 Base64 的字符串编码，辅以简单的减法加密**

**· 函数与变量名称随机化**

**· 添加冗余代码并平坦化执行流程混淆逻辑**

**· 虚拟环境与调试器检测，如发现运行在沙箱或虚拟机中将自动终止并删除自身**

“一旦检测到调试或虚拟化环境，木马会立即停止执行并自我删除。”报告指出。

## 广泛的数据窃取范围

该木马具备极强的信息收集能力，覆盖范围广泛，包括：

**· 系统信息：**设备名、操作系统、公网 IP、硬件配置、已安装应用等

**· 浏览器数据：**密码、Cookie、浏览历史、信用卡信息（支持 Chromium 与 Gecko 内核）

**· 通信应用：**Telegram、Signal、Discord、Element、Pidgin 等多款聊天工具

**· 邮件客户端：**Outlook、Windows Messaging、Foxmail 等账户凭证

**· 加密货币钱包：**支持本地钱包应用和浏览器插件（如 MetaMask、Phantom、Binance）

其中，针对加密通讯工具的攻击不会尝试解密，而是**直接窃取相关文件**。

此外，该木马还内置了剪贴板监听功能，虽然尚未完全实现，但具有未来**劫持加密钱包地址的潜力**，这是金融类恶意软件常用的手段之一。

## 通信方式：不与 C2 服务器互动，依赖 Telegram Bot 单向通信

不同于传统木马通过动态命令与控制（C2）服务器进行双向交互，**0bj3ctivityStealer**采用更加隐秘的**单向信息上传**方式，主要依赖 Telegram Bot 进行数据传输。

“所有功能将被循环执行，数据在每轮收集后立即通过 Telegram 发出。”报告称。

虽然样本中也包含 SMTP（邮件）传输模块，但此次分析中该功能尚未激活。

## 攻击范围广泛，但不具定向性

遥测数据显示，该木马攻击面广泛，主要在**美国、德国和黑山**等国家被检测到，且攻击目标并不具有明显定向性，更像是机会主义式攻击。

然而，值得关注的是，**被感染的目标多集中于政府机构与制造业公司**，这也引发了人们对于关键基础设施数据泄露可能造成严重后果的担忧。

**这场针对性不强但技术精湛的信息窃取活动，再次敲响了网络安全警钟，提醒政府与企业在日常运营中加强钓鱼邮件防范与系统安全加固，尤其要警惕利用隐写术与 PowerShell 的多层次恶意载荷组合攻击。**

本文翻译自securityonline [原文链接](https://securityonline.info/0bj3ctivitystealer-stealthy-info-stealer-uses-steganography-powershell-to-evade-detection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310679](/post/id/310679)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/0bj3ctivitystealer-stealthy-info-stealer-uses-steganography-powershell-to-evade-detection/)

如若转载,请注明出处： <https://securityonline.info/0bj3ctivitystealer-stealthy-info-stealer-uses-steganography-powershell-to-evade-detection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [攻击链条：从伪装订单到多层次载荷投递](#h2-0)
* [反分析与规避机制](#h2-1)
* [广泛的数据窃取范围](#h2-2)
* [通信方式：不与 C2 服务器互动，依赖 Telegram Bot 单向通信](#h2-3)
* [攻击范围广泛，但不具定向性](#h2-4)

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