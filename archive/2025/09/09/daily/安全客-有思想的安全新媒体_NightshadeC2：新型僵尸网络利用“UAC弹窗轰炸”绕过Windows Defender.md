---
title: NightshadeC2：新型僵尸网络利用“UAC弹窗轰炸”绕过Windows Defender
url: https://www.anquanke.com/post/id/311962
source: 安全客-有思想的安全新媒体
date: 2025-09-09
fetch_date: 2025-10-02T19:49:35.081385
---

# NightshadeC2：新型僵尸网络利用“UAC弹窗轰炸”绕过Windows Defender

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

# NightshadeC2：新型僵尸网络利用“UAC弹窗轰炸”绕过Windows Defender

阅读量**1237799**

发布时间 : 2025-09-08 17:46:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/nightshadec2-a-new-botnet-is-using-uac-prompt-bombing-to-bypass-windows-defender/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近日，eSentire威胁响应单元（TRU）发现了一个名为**NightshadeC2**的新型僵尸网络家族。该恶意软件通过**加载器**部署，融合**社会工程学**、**Windows Defender排除机制**及**复杂规避策略**，其最显著特征是采用TRU称为“**UAC弹窗轰炸**”的技术，强迫用户妥协并绕过**沙箱环境**。

TRU指出：“NightshadeC2的加载器使用一种简单却高效的技术，既能绕过恶意软件分析沙箱，又能通过‘UAC弹窗轰炸’将最终载荷排除在Windows Defender检测范围外。”

NightshadeC2的操作者正利用**ClickFix攻击**——向受害者展示伪造的**验证码（CAPTCHA）**，并诱导其在Windows“运行”对话框中执行**恶意命令**。TRU还观察到，感染通过**植入恶意代码的合法软件版本**传播，例如**Advanced IP Scanner**、**Express VPN**、**CCleaner**和**Everything**。

第二阶段的**PowerShell脚本**会解密一个\*\*.NET加载器\*\*，该加载器在最终有效载荷接触磁盘之前，就尝试在Windows Defender中为其添加**排除项**。如果PowerShell命令失败，加载器会**循环重试**，从而产生**大量UAC弹窗**，受害者为恢复系统可用性最终不得不接受。

TRU解释道：“如果PowerShell进程返回**非0的退出代码**，**while循环**将继续执行，这实际上迫使用户批准**用户账户控制（UAC）提示**，否则将面临系统可用性问题。”

这种策略还会困住**禁用了Windows Defender的恶意软件沙箱**，使其产生非零退出代码并阻止有效载荷交付。TRU证实该方法可绕过多种沙箱产品，包括**Joe Sandbox**、**CAPEv2**、**Hatching Triage**和**Any.Run**。

NightshadeC2的**C语言变体**通过**TCP端口7777、33336、33337和443**进行通信，而**Python变体**则使用**端口80**。其核心功能包括：

1. 通过**命令提示符/PowerShell实现反向shell**
2. **下载并执行DLL或EXE文件**
3. **屏幕捕获和隐藏浏览器启动**
4. 通过**模拟键盘/鼠标输入进行远程控制**
5. **键盘记录和剪贴板捕获**
6. 从**基于Chromium和Gecko的浏览器中窃取凭证**

TRU指出，Python变体的功能有所缩减（仅限于反向shell、下载/执行和自我删除），但由于**杀毒软件对其覆盖较少**，可能更难被检测到。

该恶意软件通过**多个注册表项（Winlogon、RunOnce和Active Setup）** 实现持久化。激活后，它会通过收集**外部IP、操作系统版本、MachineGuid、用户名和域**来识别受害者指纹。

捕获的击键和剪贴板数据被记录到**隐藏文件**中，文件名取决于权限级别。在一个案例中，高权限系统使用`%LOCALAPPDATA%\JohniiDepp`，而非高权限系统则使用`%LOCALAPPDATA%\LuchiiSvet`（俄语中意为“RaysLight”）。

部分变体通过**Steam个人资料元数据**获取其**命令与控制（C2）服务器**，使攻击者能够动态轮换基础设施。TRU观察到一个样本使用**Steam社区URL**解析至**programsbookss[.]com**。

**C2协议**以**RC4加密握手**开始，然后传输受害者指纹并接收命令，例如**文件上传、下载、反向shell和远程桌面操作**。

除了UAC弹窗轰炸外，TRU还发现了两种**UAC绕过方法**：

1. **2019年发现的RPC服务器滥用技术**，用于权限提升。
2. **基于加载器的绕过方法**，可检测版本早于Windows 11的操作系统，通过启动**LOLBin进程**来获取提升的权限，并无需重复提示即可添加Defender排除项。

TRU警告：“这种方法一个特别值得注意的方面是，**禁用了WinDefend（Windows Defender）服务的系统将生成非零退出代码**，导致恶意软件分析沙箱陷入执行循环。”

各组织应警惕**ClickFix式诱饵**，仔细检查**植入恶意代码的软件来源**，并监控**可疑的UAC提示和Defender排除项变更**。

本文翻译自securityonline [原文链接](https://securityonline.info/nightshadec2-a-new-botnet-is-using-uac-prompt-bombing-to-bypass-windows-defender/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311962](/post/id/311962)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/nightshadec2-a-new-botnet-is-using-uac-prompt-bombing-to-bypass-windows-defender/)

如若转载,请注明出处： <https://securityonline.info/nightshadec2-a-new-botnet-is-using-uac-prompt-bombing-to-bypass-windows-defender/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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