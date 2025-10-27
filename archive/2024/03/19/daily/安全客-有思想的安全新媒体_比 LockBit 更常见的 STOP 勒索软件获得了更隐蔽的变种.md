---
title: 比 LockBit 更常见的 STOP 勒索软件获得了更隐蔽的变种
url: https://www.anquanke.com/post/id/294040
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:46.985786
---

# 比 LockBit 更常见的 STOP 勒索软件获得了更隐蔽的变种

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

# 比 LockBit 更常见的 STOP 勒索软件获得了更隐蔽的变种

阅读量**104969**

发布时间 : 2024-03-18 11:08:29

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.scmagazine.com/news/stop-ransomware-more-common-than-lockbit-gains-stealthier-variant>

译文仅供参考，具体内容表达以及含义原文为准。

StopCrypt 是 2023 年最常见的勒索软件系列，它有一个利用更先进的规避策略的新变体。

根据趋势科技上周发布的2023 年年度网络安全报告，StopCrypt（也称为 STOP/DJVU）在 2023 年的检测量中超过了 LockBit 勒索软件家族。根据 Chainaanalysis 的年中报告， STOP 通常针对较小的目标，2023 年上半年平均支付赎金金额为 619 美元。

SonicWall周二报道称，新的 StopCrypt 变种在多阶段 shellcode 部署过程中采用了多种规避策略，包括长延迟循环、动态 API 解析和进程空洞，或者将合法可执行文件中的代码替换为恶意代码。

**“Msjd”StopCrypt 勒索软件试图躲避防病毒保护**

SonicWall 捕获实验室研究的 StopCrypt 变体通过在延迟循环中将相同数据复制到某个位置超过 6500 万次来开始其秘密任务，这可能是为了躲避沙箱等时间敏感的防病毒机制。

然后，它采用动态 API 解析的多个阶段 – 在运行时调用 API，而不是直接链接它们。这可以防止反病毒检测到由恶意软件代码中的静态链接直接 API 调用创建的工件。

在使用 CreateToolHelp32Snapshot 拍摄当前进程的快照、使用 Module32First 提取信息并调用 VirtualAlloc 分配具有读、写和执行权限的内存后，恶意软件进入第二阶段，动态调用其他 API 来执行进程空洞。

Ntdll\_NtWriteVirtualMemory 用于将恶意代码写入使用 kernel32\_CreateProcessA 创建的挂起进程中。

当暂停的进程恢复时，最终的勒索软件负载会启动 icacls.exe 来修改访问控制列表，以防止修改或删除 StopCrypt 创建的新目录和文件。勒索软件会加密用户的文件并添加扩展名“.msjd”。

SonicWall 研究的变体中发现的勒索软件注释包括 980 美元的索价，如果受害者在 72 小时内联系威胁行为者，则可享受 490 美元的“折扣”优惠。

SonicWall 描述的 STOP 变种与PCrisk 研究人员去年发现的变种有相似之处，该变种最初是通过 VirusTotal 提交的。相似之处包括“.msjd”文件扩展名和勒索信息，其中包括威胁行为者的联系信息。

本文翻译自 [原文链接](https://www.scmagazine.com/news/stop-ransomware-more-common-than-lockbit-gains-stealthier-variant)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294040](/post/id/294040)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.scmagazine.com/news/stop-ransomware-more-common-than-lockbit-gains-stealthier-variant>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**5赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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