---
title: 黑客利用 GitHub 代码仓库托管 Amadey 恶意软件与数据窃取程序，绕开过滤机制
url: https://www.anquanke.com/post/id/310230
source: 安全客-有思想的安全新媒体
date: 2025-07-19
fetch_date: 2025-10-06T23:39:03.272276
---

# 黑客利用 GitHub 代码仓库托管 Amadey 恶意软件与数据窃取程序，绕开过滤机制

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

# 黑客利用 GitHub 代码仓库托管 Amadey 恶意软件与数据窃取程序，绕开过滤机制

阅读量**86397**

发布时间 : 2025-07-18 17:32:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/07/hackers-use-github-repositories-to-host.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员发现，黑客正利用**公开的GitHub存储库**托管**恶意载荷**，并**通过Amadey恶意软件进行传播。**据观察，这一攻击活动发生在2025年4月。

思科Talos威胁情报团队研究人员Chris Neal与Craig Jackson于今日发布的报告称：“这些‘恶意软件即服务（MaaS）’的运营者**使用伪造的GitHub账号托管恶意载荷、工具以及Amadey插件**，显然是试图**绕过网络过滤机制**，同时**便于部署**使用。”

思科指出，攻击链中采用名为**“Emmenhtal（又称PEAKLIGHT）”**的恶意加载器来投递Amadey，而后者再从这些黑客控制的GitHub公开存储库中下载多个定制化载荷。

此次活动在战术上与2025年2月针对乌克兰实体的钓鱼邮件攻击存在相似之处，后者通过**发票支付与账单诱饵**传播SmokeLoader，并同样借助**Emmenhtal加载器**。

Emmenhtal与Amadey均为**二级恶意载荷的下载器**，可投递信息窃取程序，而Amadey过去还曾被发现用于**传播如LockBit 3.0等勒索软件**。

两者间的**关键区别**之一在于：Amadey具备**收集系统信息**的能力，且支持通过一系列DLL插件拓展功能，如**窃取凭证或截取屏幕**。

在对2025年4月攻击活动的分析中，思科Talos发现**三个GitHub账号**（Legendary99999、DFfe9ewf 和 Milidmdds）被用于**托管Amadey插件、二级载荷以及其他恶意攻击脚本**，涉及Lumma Stealer、RedLine Stealer和Rhadamanthys Stealer等知名窃密工具。这些账号目前已被GitHub平台移除。

部分GitHub存储库中的JavaScript文件与此前SmokeLoader攻击中使用的Emmenhtal脚本完全相同，唯一区别在于其**所下载的载荷内容**发生了改变。具体而言，存储库中的Emmenhtal加载器文件被用于**投递Amadey、AsyncRAT**，甚至还有**合法的PuTTY.exe程序**。

研究人员还在这些存储库中发现一个Python脚本，疑似为Emmenhtal的变种，内嵌的PowerShell命令可**从硬编码IP地址下载Amadey**，显示出该恶意软件正在**持续演进**。

研究指出，这些用于部署载荷的GitHub账号，可能是**更大规模MaaS运营**的一部分，黑客正滥用微软旗下的代码托管平台进行恶意活动。

该披露正值Trellix公司揭露另一场通过**恶意加载器SquidLoader**发起的钓鱼攻击行动，目标是中国香港的金融服务机构。该安全厂商还发现了更多攻击线索，显示新加坡和澳大利亚也可能正在遭受类似攻击。

![]()

*“SquidLoader” 攻击链*

SquidLoader威胁性极高，其**内置多种反分析、反沙箱、反调试技术**，使其能够成功规避检测并妨碍安全分析。此外，SquidLoader还能**与远程服务器建立通信**，传送受感染主机的信息，并注入下一阶段的恶意载荷。

安全研究员Charles Crofford表示：“SquidLoader攻击链最终会部署Cobalt Strike信标，实现远程访问与控制。其复**杂的反检测技术与极低的查杀率**，对目标组织构成严重威胁。”

这一系列发现还伴随着多个社会工程攻击活动的披露，这些攻击利用多样化手段传播各类恶意软件，包括但不限于：

* • 一个被称为UNC5952的金融驱动型攻击组织，利用**发票类邮件**诱导受害者下载恶意程序，最终部署下载器CHAINVERB，并进一步投递ConnectWise ScreenConnect远程访问软件；
* • 利用**税务相关诱饵**误导收件人点击链接，最终下载伪装成PDF文档的ConnectWise ScreenConnect安装程序；
* • 利用**美国社会保障局（SSA）主题**窃取用户凭证，或安装被植入木马的ConnectWise ScreenConnect程序，并诱导用户同步微软Phone Link应用，以窃取短信与双因素认证码；
* • 使用Logokit钓鱼工具包**建立伪造登录页面**，托管于亚马逊AWS基础设施上，借此绕过检测，同时嵌入Cloudflare Turnstile CAPTCHA，制造安全假象；
* • 利用**自制的Python Flask钓鱼工具包**实现低技术门槛的凭证窃取；
* • 名为Scanception的攻击行动，采用**嵌入PDF邮件附件的二维码**，引导用户访问伪装成微软登录页的钓鱼页面；
* • 通过名为**ClickFix**的手法投递Rhadamanthys Stealer与NetSupport RAT；
* • 利用**“CaaS（Cloaking-as-a-Service）”**服务（如Hoax Tech与JS Click Cloaker）隐藏钓鱼网站，仅向目标用户展示真实内容，从而规避安全扫描；
* • 使用HTML与JavaScript**构建具有迷惑性的邮件**，能够避开用户警觉与传统检测机制；
* • 针对**B2B服务供应商**的攻击，邮件中嵌入SVG格式图像，内含混淆JavaScript代码，在浏览器中打开后通过window.location.href函数跳转至攻击者控制的基础设施。

据Cofense数据统计，2024年使用高级TTP的攻击活动中，有**57%采用了二维码手段**。其他典型手法包括**在邮件中使用加密压缩包**以绕过安全邮件网关（SEG）检测。

Cofense研究员Max Gannon指出：“通过加密压缩包的方式，攻击者可**阻止SEG及其他安全机制扫描其中内容**，从而隐藏本应被识别为恶意的文件。”

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/07/hackers-use-github-repositories-to-host.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310230](/post/id/310230)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/07/hackers-use-github-repositories-to-host.html)

如若转载,请注明出处： <https://thehackernews.com/2025/07/hackers-use-github-repositories-to-host.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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