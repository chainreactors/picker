---
title: 黑客部署CRON#TRAP用于持久Linux系统后门
url: https://www.anquanke.com/post/id/301593
source: 安全客-有思想的安全新媒体
date: 2024-11-07
fetch_date: 2025-10-06T19:12:13.047582
---

# 黑客部署CRON#TRAP用于持久Linux系统后门

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

# 黑客部署CRON#TRAP用于持久Linux系统后门

阅读量**76764**

发布时间 : 2024-11-06 11:28:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/hackers-crontrap-persistent-linux-system-backdoors/>

译文仅供参考，具体内容表达以及含义原文为准。

**CRON#TRAP 是一种新型网络钓鱼攻击，它利用仿真 Linux 环境绕过安全性并建立持久性后门。黑客利用 QEMU 和 Chisel 获得隐蔽访问权限，从而窃取数据并控制系统。**

Securonix 威胁研究部门发现了一个复杂的网络钓鱼活动 “CRON#TRAP”，它利用一种独特的方法渗透系统并建立持久性后门。这种创造性的攻击方法涉及在被攻击的端点中部署模拟 Linux 环境，特别是 Tiny Core Linux。

**CRON#TRAP 的多阶段攻击过程**

CRON#TRAP 活动采用多阶段攻击方法入侵目标系统并建立持久性后门。最初的感染载体通常是一封包含恶意 ZIP 和快捷方式文件（名为 OneAmerica Survey.zip 和 OneAmerica Survey.lnk）的钓鱼电子邮件。

![Hackers Deploy CRON#TRAP for Persistent Linux System Backdoors]()
截图： Securonix

恶意附件通常伪装成调查或软件更新等合法文档，诱骗用户执行。执行后，该快捷方式文件会下载大型 ZIP 压缩包，其中包含模拟 Linux 环境的必要组件。

**仿真 Linux 环境部署**

下载的压缩包包括一个定制的 Linux 发行版（如 Tiny Core Linux）和 QEMU 虚拟化工具。批处理文件 “start.bat ”会显示服务器错误信息，表明存在服务器端调查链接问题。脚本执行 QEMU 进程和命令行，启动模拟 Linux 环境，为攻击者的活动创建隐蔽环境。

explorer.exe 进程会执行一个 HTTPS 托管图像，用户的默认浏览器会显示该图像。这样，攻击者就可以进一步将活动掩盖为合法的系统行为，从而避免被发现。

**安装 Chisel 隧道工具**

在模拟的 Linux 环境中，攻击者安装了一个预先配置好的 Chisel 客户端，这是一种隧道工具，可与远程命令与控制（C&C）服务器建立隐蔽的通信渠道。通过 Chisel 隧道工具，攻击者可在 HTTP 和 SSH 协议上建立安全隧道。

该工具配置了特定设置，如目标 C&C 服务器地址、端口号和加密参数，可自动连接到攻击者的基础设施。

Chisel 客户端在仿真 Linux 环境中执行，每当系统启动或启动时都会激活后门。这种安全的加密连接使攻击者能够在被入侵系统和攻击者的基础架构之间传输数据和命令。

通过这种安全连接，攻击者可以执行任意命令、下载恶意软件、窃取敏感数据、操纵系统设置、外泄敏感数据、部署持久化机制、修改注册表设置、创建计划任务、安装 rootkit，并扩散到其他网络系统。

**使用合法工具的规避技术**

通过在合法的虚拟化工具 QEMU 中伪装恶意活动，攻击者可以绕过传统的安全措施，建立隐秘的立足点。此外，利用 Chisel 隧道工具，攻击者还可以保持持续访问权限，并执行进一步的恶意行动。

报告指出：“攻击者对 QEMU 和 Chisel 等合法软件的依赖增加了一层规避手段，因为这些工具在许多环境中都不太可能触发警报。”

CRON#TRAP 活动凸显了网络犯罪分子不断演变的战术，包括模拟环境和滥用合法软件。这种方法允许攻击者持续访问被入侵的系统，强调了注意可疑电子邮件的重要性。

本文翻译自hackread [原文链接](https://hackread.com/hackers-crontrap-persistent-linux-system-backdoors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301593](/post/id/301593)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hackers-crontrap-persistent-linux-system-backdoors/)

如若转载,请注明出处： <https://hackread.com/hackers-crontrap-persistent-linux-system-backdoors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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