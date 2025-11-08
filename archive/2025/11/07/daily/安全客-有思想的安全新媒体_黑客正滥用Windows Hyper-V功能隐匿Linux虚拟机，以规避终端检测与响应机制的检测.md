---
title: 黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测
url: https://www.anquanke.com/post/id/313062
source: 安全客-有思想的安全新媒体
date: 2025-11-07
fetch_date: 2025-11-08T03:00:46.635275
---

# 黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测

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

# 黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测

阅读量**28809**

发布时间 : 2025-11-07 10:27:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

据Bitdefender最新报告，被称为**Curly COMrades**的威胁行为体正通过滥用虚拟化技术绕过安全解决方案，并执行定制化恶意软件。该攻击者会在特定受害系统上启用Hyper-V角色，部署一个极简的、基于Alpine Linux的虚拟机。

安全研究人员Victor Vrabie、Adrian Schipor与Martin Zugec在技术报告中指出：“**这个隐藏环境占用资源极低（仅120MB磁盘空间与256MB内存）**，内部运行着其自定义的反向Shell工具CurlyShell与反向代理工具CurlCat。”

攻击中使用的工具包括用于双向数据传输的CurlCat、实现持久远程访问的RuRat、凭据窃取工具Mimikatz，以及一款模块化.NET植入程序MucorAgent——其早期版本可追溯至2023年11月。

在与格鲁吉亚计算机应急响应小组（CERT）的联合分析中，研究人员进一步识别出与该组织相关的其他工具。**攻击者还试图在被感染的Windows 10主机上武器化Hyper-V，以构建隐藏的远程操作环境，从而建立长期访问权限。**

![]()

研究人员指出：“通过将恶意软件及其执行环境隔离在虚拟机中，**攻击者有效绕过了许多传统基于主机的EDR检测**。该威胁行为体表现出维持反向代理能力的明确意图，不断在环境中引入新工具。”

除使用Resocks、Rsockstun、Ligolo-ng、CCProxy、Stunnel及基于SSH的代理与隧道方法外，Curly COMrades还使用了多种其他工具，包括专为远程命令执行设计的PowerShell脚本，以及此前未被记录的ELF二进制文件CurlyShell。该文件部署于虚拟机中，用于提供持久化反向Shell。

**该恶意软件使用C++编写，以后台守护进程形式运行，可连接至命令与控制服务器并启动反向Shell**，使攻击者能够执行加密命令。其通信机制基于HTTP：通过GET请求轮询服务器以获取新指令，再通过POST请求将命令执行结果回传。

Bitdefender强调：“两个自定义恶意软件家族——CurlyShell与CurlCat——是本次攻击行动的核心。它们共享大量相同代码，但在处理接收数据时采用不同方式：CurlyShell直接执行命令，而CurlCat通过SSH转发流量。这些工具旨在实现灵活控制与高度适应性。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313062](/post/id/313062)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html)

如若转载,请注明出处： <https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **663**

* 粉丝
* **6**

### TA的文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13

### 相关文章

* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13
* ##### [恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载](/post/id/313076)

  2025-11-07 10:27:01
* ##### [远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测](/post/id/313056)

  2025-11-07 10:26:52
* ##### [二进制供应链安全平台Binarly Transparency Platform 3.5发布，新增对Java归档文件与JVM字节码的深度支持](/post/id/313053)

  2025-11-07 10:26:40

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