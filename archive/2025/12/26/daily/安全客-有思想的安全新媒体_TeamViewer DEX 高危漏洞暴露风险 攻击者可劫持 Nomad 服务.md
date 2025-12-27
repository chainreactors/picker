---
title: TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务
url: https://www.anquanke.com/post/id/314053
source: 安全客-有思想的安全新媒体
date: 2025-12-26
fetch_date: 2025-12-27T03:20:41.299098
---

# TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务

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

# TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务

阅读量**19542**

发布时间 : 2025-12-26 14:50:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/high-severity-flaws-in-teamviewer-dex-allow-attackers-to-hijack-nomad-services/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

TeamViewer 发布重要安全公告，披露其数字员工体验（DEX）产品线（前身为 1E）存在多项漏洞。本次更新修复了 Windows 客户端与中央管理平台中存在的高危漏洞，这些漏洞可能被攻击者利用以绕过完整性校验、执行任意代码并提升权限。

漏洞影响内容分发服务（Nomad Branch.exe）及多款 DEX 指令，使企业面临来自局域网入侵者与恶意内部人员的双重威胁。

客户端软件中被标记为最严重的漏洞为 **CVE-2025-44016**，其通用漏洞评分系统（CVSS）得分为 8.8，属于高危级别。该漏洞存在于内容分发服务中，影响所有版本低于 25.11 的 Windows 客户端。

漏洞成因是输入验证机制存在缺陷，局域网内的恶意行为者可借此对该服务实施欺骗。安全公告中解释道：“攻击者只需为恶意文件提供一个合法的哈希值，即可诱导服务错误地将该文件判定为可信文件并执行处理流程。”

一旦系统将恶意文件标记为可信，攻击者就能以 Nomad Branch 服务的权限执行任意代码，进而完全劫持这款负责内容分发的后台进程。

除上述高危漏洞外，TeamViewer 还修复了以下两项问题：

* **CVE-2025-12687**（CVSS 评分 6.5）：这是一项拒绝服务（DoS）漏洞，攻击者可通过构造特定命令导致应用程序崩溃。
* **CVE-2025-46266**（CVSS 评分 4.3）：这是一项数据泄露漏洞，攻击者可强制服务向任意内部 IP 地址传输数据。

另一组独立漏洞则针对 TeamViewer DEX 平台本身，无论 SaaS 云端部署版本还是本地部署版本均受影响。这些漏洞存在于部分用于设备管理的脚本（即 “指令”）中，属于命令注入类漏洞。

相关漏洞编号为 **CVE-2025-64986** 至 **CVE-2025-64989**，CVSS 评分均为 7.2。安全公告指出，这些漏洞的成因是 “输入验证不当…… 导致拥有‘执行者’权限的已认证攻击者可注入任意命令”，进而能够在已接入的设备上远程执行高权限命令。

此外，研究人员还在`1E-Nomad-SetWorkRate`等指令中发现了权限提升漏洞（**CVE-2025-64994**与**CVE-2025-64995**）。这些漏洞利用 “不受控搜索路径” 机制，允许拥有特定目录写入权限的本地攻击者劫持进程，并以系统权限执行代码。

TeamViewer 已针对所有已发现的漏洞发布修复补丁，具体修复方案如下：

* **客户端修复**：运维人员需立即将 TeamViewer DEX 客户端升级至 25.11 或更高版本。
* **平台修复**：SaaS 客户在平台版本更新至 25.12 后，多数指令将自动完成更新，但部分指令需通过应用市场手动操作更新；本地部署客户则需联系专属客户成功经理（CSM）获取更新后的指令文件。

目前暂无证据表明这些漏洞已被用于野外攻击，但鉴于漏洞存在代码执行风险，相关方应尽快采取修复措施。

本文翻译自securityonline [原文链接](https://securityonline.info/high-severity-flaws-in-teamviewer-dex-allow-attackers-to-hijack-nomad-services/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314053](/post/id/314053)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/high-severity-flaws-in-teamviewer-dex-allow-attackers-to-hijack-nomad-services/)

如若转载,请注明出处： <https://securityonline.info/high-severity-flaws-in-teamviewer-dex-allow-attackers-to-hijack-nomad-services/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **860**

* 粉丝
* **6**

### TA的文章

* ##### [威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统](/post/id/314037)

  2025-12-26 14:51:33
* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务](/post/id/314053)

  2025-12-26 14:50:09
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24

### 相关文章

* ##### [威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统](/post/id/314037)

  2025-12-26 14:51:33
* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24
* ##### [潜伏熊猫 APT 组织：劫持Dictionary.com+ 应用更新，展开长达两年疯狂攻击](/post/id/314062)

  2025-12-26 14:49:22
* ##### [“莲花陷阱”（LotusBail）恶意软件：5.6 万开发者下载假 WhatsApp API，功能正常却暗中窃取全部数据](/post/id/314059)

  2025-12-26 14:48:34
* ##### [英特尔 14A/18A 超级芯片：挑战台积电的 AI “系统代工” 标杆](/post/id/314055)

  2025-12-26 14:47:49

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